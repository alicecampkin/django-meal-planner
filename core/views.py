from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member


def index(request):

    members = Member.objects.all()

    context = {
        'members': members
    }

    return render(request, 'core/index.html', context)


class AddMember(LoginRequiredMixin, CreateView):
    model = Member
    fields = ['name', 'photo']
    template_name = 'core/add_member.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateMember(LoginRequiredMixin, UpdateView):
    model = Member
    fields = ['name', 'photo']
    template_name = 'core/update_member.html'
    success_url = reverse_lazy('index')


class DeleteMember(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'core/delete_member.html'
    success_url = reverse_lazy('index')
