from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.


class Index(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        return redirect('exam:show-list-exam')
