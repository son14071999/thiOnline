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
        list_id_questions = []
        i = 1
        while (True):
            try:
                question = request.POST['question-' + str(i)]
                if question == '':
                    break
                id_exam = exam
                correct_answer = request.POST['correct-answer-' + str(i)]
                answers = []
                for alpha in alphabet:
                    try:
                        status = False
                        content = request.POST['answer-' + alpha + '-' + str(i)]
                        if content.strip() == '':
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
                    id_exam=exam,
                    question=question,
                    answers=answers,
                    subject=subject,
                    link_media=link_media,
                )
                list_id_questions.append(q.id)

            except:
                break
        exam.list_id_questions = list_id_questions
        exam.save()
        return redirect('/')


class ListExams(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        questions = Exams.objects.all().order_by('innitiated_date')
        return render(request, 'Exams/listExam.html', {'questions': questions})


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
        id_list_correct_questions = ''
        id_user = request.user
        time_do = request.POST['time-do']
        scores = 0
        for question in questions:
            id_list_questions = id_list_questions + " " + str(question.id)
            try:
                answer = request.POST[str(question.id)]
                question.correct = answer
                if answer == question.correct_question:
                    scores = scores+1
                    id_list_correct_questions = id_list_correct_questions + " " + str(question.id)
            except:
                question.correct = None
                pass

        History.objects.create(
            id_exam=exam,
            time_do=time_do,
            id_user=id_user,
            id_list_correct_questions=id_list_correct_questions,
            id_list_questions=id_list_questions
        )
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
