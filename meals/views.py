import json
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal
from core.models import Member
from .forms import CreateMealForm
from django.contrib.auth.decorators import login_required


@login_required
def list_meals(request):
    meals_queryset = []
    default_mealtime = 'Dinner'

    if request.method == 'POST':
        form = CreateMealForm(request.POST, request=request)

        if form.is_valid():
            meal = Meal(
                name=request.POST['name'],
                date=request.POST['date'],
                mealtime=request.POST['mealtime'],
                user=request.user
            )
            meal.save()

            member_ids = form.cleaned_data['members'].values_list(
                'id', flat=True)

            for id in member_ids:
                meal.members.add(id)

            default_mealtime = meal.mealtime

    else:
        form = CreateMealForm(request=request)

    meals_queryset = Meal.objects.filter(
        user=request.user).order_by('date').values()

    meals = list(meals_queryset)
    for meal in meals:
        meal['date'] = meal['date'].isoformat()

    context = {}
    context['meals'] = json.dumps(meals)
    context['form'] = form
    context['default_mealtime'] = default_mealtime

    return render(request, 'meals/list_meals.html', context)


class AddMeal(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = CreateMealForm
    template_name = 'meals/add_meal.html'
    success_url = reverse_lazy('meal_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(AddMeal, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UpdateMeal(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = CreateMealForm
    template_name = 'meals/update_meal.html'
    success_url = reverse_lazy('meal_list')

    def get_form_kwargs(self):
        kwargs = super(UpdateMeal, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DeleteMeal(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'meals/delete_meal.html'
    success_url = reverse_lazy('meal_list')
