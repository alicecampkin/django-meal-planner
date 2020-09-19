from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .admin import UserCreationForm


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

class SignIn(LoginView):
    template_name = 'accounts/login.html'

class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile.html'
    fields = ['profile_picture','first_name','last_name']
    success_url = reverse_lazy('index')
