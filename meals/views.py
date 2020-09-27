from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal
from .forms import CreateMealForm
from django.contrib.auth.decorators import login_required


@login_required
def list_meals(request):
    meals = Meal.objects.all()

    context = {
        'meals': meals
    }
    return render(request, 'meals/list_meals.html', context)


class AddMeal(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = CreateMealForm
    template_name = 'meals/add_meal.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(AddMeal, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UpdateMeal(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = CreateMealForm
    template_name = 'core/update_meal.html'
    success_url = reverse_lazy('index')


class DeleteMeal(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'core/delete_meal.html'
    success_url = reverse_lazy('index')
