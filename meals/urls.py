from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_meals, name='meal_list'),
    path('<int:pk>/update', views.UpdateMeal.as_view(), name='update_meal'),
    path('delete/<int:pk>', views.delete_meal, name='delete_meal'),
    path('<str:date>', views.meal_detail, name='meal_detail')

]
