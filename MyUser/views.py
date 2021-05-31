from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib import auth
from django.http import JsonResponse
from .checkDataForm import check
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import GetAllUser


class Login(View):

    def get(self, request):
        f = LoginForm()
        return render(request, 'MyUser/formLogin.html', {'f': f})

    def post(self, request):
        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'Home/home.html')
        else:
            return render(request, 'MyUser/formLogin.html', {'err': 'Email hoặc mật khẩu sai !'})
        

class Signup(View):
    def get(self, request):
        f = LoginForm()
        if request.is_ajax():
            print(request.GET['btn_text'])
            return JsonResponse({'data': 'get'}, status=200)
        return render(request, 'MyUser/formSignup.html', {'f': f})

    def post(self, request):
        f = LoginForm(request.POST, request.FILES)
        if f.is_valid():
            message = check(f)
            if message == "validate":
                f.save()
                return redirect('Home:home')
            else:
                return HttpResponse(message)
        return HttpResponse(f.errors)


class Ajax(APIView):
    def get(self, request):
        list_user = User.objects.all()
        mydata = GetAllUser(list_user, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)





