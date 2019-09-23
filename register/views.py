from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.shortcuts import render
from django.views import generic
from .forms import LoginForm


class Top(generic.TemplateView):
    template_name = 'register/top.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'register/top.html'