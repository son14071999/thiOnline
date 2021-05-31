from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from .models import History
# Create your views here.


class HistoryView(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def get(self, request):
        user = request.user
        exams = History.objects.filter(id_user=user)
        for exam in exams:
            exam.correct = len(exam.id_list_correct_questions.split(' '))
            exam.amount = len(exam.id_list_questions.split(' '))

        return render(request, 'History/show_history.html', {
            'exams': exams
        })