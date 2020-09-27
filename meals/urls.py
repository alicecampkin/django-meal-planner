from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_meals, name='meal_list'),
    path('add', views.AddMeal.as_view(), name='add_meal')

]
