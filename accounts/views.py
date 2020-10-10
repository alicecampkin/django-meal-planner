from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .admin import UserCreationForm


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('create_profile')

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        email, password = form.cleaned_data.get(
            'email'), form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return view


class SignIn(LoginView):
    template_name = 'accounts/login.html'


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile.html'
    fields = []
    success_url = reverse_lazy('index')
