from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member
from django.contrib.auth.decorators import login_required
from .forms import InitaliseHouseholdForm, MemberForm


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

            if 'photo' in request.FILES:
                member_instance = Member(
                    photo=request.FILES['photo'],
                    name=request.POST['name'],
                    user=request.user,
                    is_primary=True
                )
            else:
                member_instance = Member(
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


@login_required
def update_primary_member(request):
    primary_member = Member.objects.filter(
        user=request.user, is_primary=True).first()

    if not primary_member:
        return redirect('create_profile')
    else:

        if request.method == 'POST':

            form = InitaliseHouseholdForm(
                request.POST, instance=primary_member)

            if form.is_valid():
                member = form.save(commit=False)
                member.user = request.user
                member.is_primary = True
                member.save()

                return redirect('list_members')

        else:
            form = InitaliseHouseholdForm(instance=primary_member)

            context = {
                'form': form,
                'member': primary_member,
            }

            return render(request, 'core/update_primary_member.html', context)


def update_member(request, pk):

    member = get_object_or_404(Member, id=pk)

    if member.is_primary:
        return redirect('profile')

    if request.method == 'POST':

        form = MemberForm(
            request.POST, instance=member)

        if form.is_valid():
            member = form.save(commit=False)
            member.user = request.user
            member.is_primary = True
            member.save()

            return redirect('list_members')

    else:
        form = InitaliseHouseholdForm(instance=member)

        context = {
            'form': form,
            'member': member,
        }

        return render(request, 'core/update_member.html', context)


class AddMember(LoginRequiredMixin, CreateView):
    model = Member
    fields = ['name', 'photo']
    template_name = 'core/add_member.html'
    success_url = reverse_lazy('list_members')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteMember(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'core/delete_member.html'
    success_url = reverse_lazy('list_members')
