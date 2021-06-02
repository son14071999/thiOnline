from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from .models import History
from Questions.models import Questions
# Create your views here.


class HistoryView(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def get(self, request):
        user = request.user
        try:
            id_historys = user.list_id_history.strip().split(" ")
        except :
            return render(request, 'History/show_history.html', {
                'message': 'dữ liệu trống'
            })
        historys = []
        for history in id_historys:
            try:
                h = History.objects.get(id=int(history))
                historys.append(h)
            except :
                pass
        for history in historys:
            history.amount = len(history.id_list_questions.strip().split(' '))

        return render(request, 'History/show_history.html', {
            'historys': historys
        })


class View_exam(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def get(self, request, id_history):
        history = History.objects.get(id=id_history)
        id_questions = history.id_list_questions.strip().split()
        list_user_answers = history.list_user_answers.strip().split()
        questions = []
        for i in range(len(id_questions)):
            try:
                q = Questions.objects.get(id=int(id_questions[i]))
                q.correct = list_user_answers[i]
                questions.append(q)
            except :
                pass
        history.amount = len(questions)
        return render(request, 'History/show_exam_history.html', {
            'questions':questions,
            'exam': history.id_exam,
            'history': history
        })