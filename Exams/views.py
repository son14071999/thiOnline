from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Exams
from Questions.models import Questions
from History.models import History
import unidecode
import re
from django.core.paginator import Paginator
import random


class create_exam(LoginRequiredMixin, View):
    login_url = '/user/login/'
    list_subject = ['Toán', 'Lý', 'Hoá', 'Sinh', 'Sử', 'Địa', 'Công dân', 'Tiếng anh']

    def get(self, request):
        return render(request, 'Exams/create_exam.html', {'subjects': self.list_subject})

    def post(self, request):
        message = ''
        alphabet = 'ABCD'
        name = request.POST['name_exam']
        if name == '':
            message = 'Tên đề không được để trống'
            return render(request, 'Exams/create_exam.html', {'message': message})
        subject = request.POST['subject']
        time = request.POST['time']
        if int(time) < 10 or int(time) > 300:
            message = 'Thời gian làm bài không nhỏ hơn 10 phút và lớn hơn 30 phút'
            return render(request, 'Exams/create_exam.html', {'message': message})
        us = request.user

        exam = Exams.objects.create(
            name=name,
            slug=re.sub(r'[ ]+', '-', unidecode.unidecode(name)),
            subject=subject,
            time=time,
            id_author=us
        )
        if us.list_id_exam != None:
            us.list_id_exam = us.list_id_exam + " " + str(exam.id)
        else:
            us.list_id_exam = str(exam.id)
        us.save()
        list_id_questions = []
        i = 1
        while (True):
            try:
                question = request.POST['question-' + str(i)]
                level = request.POST['level-' + str(i)]
                if question == '':
                    break
                id_exam = exam
                try:
                    correct_answer = request.POST['correct-answer-' + str(i)]

                except:
                    Exams.objects.remove(exam)
                    message = 'Vui lòng nhập đáp án đúng'
                    return render(request, 'Exams/create_exam.html', {'message': message})
                answers = []
                for alpha in alphabet:
                    try:
                        status = False
                        content = request.POST['answer-' + alpha + '-' + str(i)]
                        if content.strip() == '':
                            Exams.objects.remove(exam)
                            message = 'Câu trả lời không được bỏ trống'
                            return render(request, 'Exams/create_exam.html', {'message': message})
                        if correct_answer == alpha:
                            status = True
                        label = alpha
                        answer = {
                            'content': content,
                            'status': status,
                            'label': label,
                        }
                        answer = json.loads(json.dumps(answer))
                        answers.append(answer)
                    except:
                        pass
                try:
                    link_media = request.FILES['image-' + str(i)]
                except:
                    link_media = ''
                i = i + 1
                q = Questions.objects.create(
                    level_of_different=level,
                    id_exam=exam,
                    question=question,
                    answers=answers,
                    subject=subject,
                    link_media=link_media,
                    correct_answer=correct_answer
                )
                list_id_questions.append(q.id)

            except:
                break
        exam.list_id_questions = list_id_questions
        exam.amount_questions = len(list_id_questions)
        exam.save()

        return redirect('exam:show-list-exam')


class Search(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        str_search = request.GET['search']
        print(str_search)
        exams = Exams.objects.filter(name__icontains=str_search)
        paginator = Paginator(exams, 5)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'Exams/listExam.html', {'exams': page_obj})


class ListExams(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        exams = Exams.objects.all().order_by('-innitiated_date')
        paginator = Paginator(exams, 5)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'Exams/listExam.html', {'exams': page_obj})


class takeTheExams(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request, nameExam):
        id_exam = str(request.GET['check']).split('-')[-1]
        exam = Exams.objects.get(id=id_exam)
        questions = exam.questions_set.all()
        exam.amount_view_user = exam.amount_view_user + 1
        exam.save()
        number = len(questions)
        return render(request, 'Exams/do_exam.html', {
            'exam': exam,
            'questions': questions,
            'number': number,
        })


class checkAnswers(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def post(self, request):
        id_exam = request.POST['id']
        exam = Exams.objects.get(id=id_exam)
        exam.amount_do = exam.amount_do + 1
        exam.save()
        questions = exam.questions_set.all()
        id_list_questions = ''
        list_user_answer = ''
        user = request.user
        time_do = request.POST['time-do']
        scores = 0
        for question in questions:
            id_list_questions = id_list_questions + " " + str(question.id)
            try:
                answer = request.POST[str(question.id)]
                question.correct = answer
                if answer == question.correct_answer:
                    scores = scores + 1
            except:
                question.correct = None
            list_user_answer = list_user_answer + " " + str(question.correct)

        h = History.objects.create(
            id_exam=exam,
            time_do=time_do,
            id_user=user,
            list_user_answers=list_user_answer,
            id_list_questions=id_list_questions,
            correct=scores
        )
        if user.list_id_history != None:
            user.list_id_history = user.list_id_history + " " + str(h.id)
        else:
            user.list_id_history = h.id
        user.save()
        number = len(questions)
        return render(request, 'Exams/test_results.html', {
            'exam': exam,
            'questions': questions,
            'number': number,
            'score': scores
        })


class Manage(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        user = request.user
        all_exams_do = History.objects.filter(id_user=user)
        exams_do = []
        for e in all_exams_do:
            if e.id_exam not in exams_do:
                exams_do.append(e)

        exams_create = Exams.objects.filter(id_author=user)
        return render(request, 'Exams/manage.html', {
            'exams_do': exams_do,
            'exams_create': exams_create,

        })


class Random(LoginRequiredMixin, View):
    login_url = '/user/login/'
    list_subject = ['Toán', 'Lý', 'Hoá', 'Sinh', 'Sử', 'Địa', 'Công dân', 'Tiếng anh']
    levels = ['Rất dễ', 'Dễ', 'Trung bình', 'Khó', 'Rất khó']

    def get(self, request):
        return render(request, 'Exams/form_random.html', {'list_subject': self.list_subject, 'levels': self.levels})

    def post(self, request):
        subject = request.POST['subject']
        level1 = request.POST['r-1']
        level2 = request.POST['r-2']
        level3 = request.POST['r-3']
        level4 = request.POST['r-4']
        level5 = request.POST['r-5']
        time = request.POST['time']
        questions = Questions.objects.all()
        questions_level1 = []
        questions_level2 = []
        questions_level3 = []
        questions_level4 = []
        questions_level5 = []
        for q in questions:
            if q.subject == subject:
                if q.level_of_different == 1:
                    questions_level1.append(q)
                elif q.level_of_different == 2:
                    questions_level2.append(q)
                elif q.level_of_different == 3:
                    questions_level3.append(q)
                elif q.level_of_different == 4:
                    questions_level4.append(q)
                elif q.level_of_different == 5:
                    questions_level5.append(q)
            else:
                pass

        random.shuffle(questions_level1)
        random.shuffle(questions_level2)
        random.shuffle(questions_level3)
        random.shuffle(questions_level4)
        random.shuffle(questions_level5)

        if len(questions_level1) < int(level1) or len(questions_level2) < int(level2) or len(
                questions_level3) < int(level3) or len(questions_level4) < int(level4) or len(questions_level5) < int(level5):
            return render(request, 'Exams/form_random.html',
                          {'list_subject': self.list_subject, 'levels': self.levels,
                           'message': 'Không đủ câu hỏi theo yêu cầu!'})
        questions = questions_level1[:int(level1)] + questions_level2[:int(level2)] + questions_level3[:int(
            level3)] + questions_level4[:int(level4)] + questions_level5[:int(level5)]
        return render(request, 'Exams/show_random.html', {
            'questions': questions,
            'time': int(time),
            'sum': len(questions)
        })


class checkRandom(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def post(self, request):
        sum = int(request.POST['sum'])
        questions = []
        scores = 0
        list_user_answer = ''
        id_list_questions = ''
        for i in range(1, sum+1):
            q = request.POST['h-'+str(i)]
            q = Questions.objects.get(id=q)
            id_list_questions = id_list_questions + " " + str(q.id)
            try:
                answer = request.POST[str(i)]
                q.correct = answer
                if answer == q.correct_answer:
                    scores = scores + 1
            except:
                q.correct = None
            list_user_answer = list_user_answer + " "+ str(q.correct)
            questions.append(q)
        number = len(questions)
        time_do = request.POST['time-do']
        user = request.user
        History.objects.create(
            time_do=time_do,
            id_user=user,
            list_user_answers=list_user_answer,
            id_list_questions=id_list_questions,
            correct=scores
        )
        return render(request, 'Exams/score_random.html', {
            'questions': questions,
            'number': number,
            'score': scores
        })