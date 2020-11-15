from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_meals, name='meal_list'),
    path('meals/', views.meal_manager, name='meal_manager'),
    path('meal/<int:pk>/update', views.UpdateMeal.as_view(), name='update_meal'),
    path('meal/<int:pk>/delete', views.delete_meal, name='delete_meal'),
    path('meal/<str:date>', views.meal_detail, name='meal_detail')
]
