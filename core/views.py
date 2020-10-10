from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member
from django.contrib.auth.decorators import login_required
from .forms import InitaliseHouseholdForm


def index(request):

    return render(request, 'core/index.html')


@login_required
def list_members(request):
    members = Member.objects.filter(user=request.user)

    context = {
        'members': members
    }

    return render(request, 'core/list_members.html', context)


@login_required
def initialise_members(request):

    if request.method == "POST":
        form = InitaliseHouseholdForm(request.POST, request.FILES)

        if form.is_valid():

            member_instance = Member(
                photo=request.FILES['photo'],
                name=request.POST['name'],
                user=request.user,
                is_primary=True
            )

            member_instance.save()

            return redirect('list_members')

    else:
        form = InitaliseHouseholdForm()

    context = {
        'form': form,
    }

    return render(request, 'core/create_first_member.html', context)


class AddMember(LoginRequiredMixin, CreateView):
    model = Member
    fields = ['name', 'photo']
    template_name = 'core/add_member.html'
    success_url = reverse_lazy('list_members')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateMember(LoginRequiredMixin, UpdateView):
    model = Member
    fields = ['name', 'photo']
    template_name = 'core/update_member.html'
    success_url = reverse_lazy('list_members')


class DeleteMember(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'core/delete_member.html'
    success_url = reverse_lazy('list_members')
