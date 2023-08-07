from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from . import forms
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


def index(self, request):
    return render(request, 'home.html')


class PasswordReset(View):
    def get(self,request):
        return render(request, 'password-forgot.html')

class Register(View):
    def get(self,request):
        return render(request, 'register.html')

    def post(self, request):

        form = forms.RegisterForm(data=request.POST)
        password = form.data['password']
        confirm_password = form.data['confirm_password']
        if password == confirm_password:
            if form.is_valid():
                password = form.data['password']
                user = form.save()
                user.set_password(password)
                user.save()
                messages.error(request, "Register Success.")
                return redirect('login')
            else:
                messages.error(request, "User name already Exits.")
                return render(request, 'register.html', {'form': form})
        else:
            messages.error(request, "Confirm password Dont match.")
            return render(request, 'register.html', {'form':form})


class Login(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self, request):
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    messages.success(request, "Login Success.")
                    login(request,user)
                    return redirect('home')
                else:
                    messages.error(request, "User Not Found.")
                    return render(request, 'login.html' ,{'form':form})

            except ObjectDoesNotExist:
                messages.error(request, "User Not Found.")
                return render(request, 'login.html', {'form': form})



class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')
