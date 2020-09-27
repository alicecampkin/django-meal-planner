from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_meals, name='meal_list'),
    path('add', views.AddMeal.as_view(), name='add_meal'),
    path('<int:pk>/update', views.UpdateMeal.as_view(), name='update_meal'),
    path('<int:pk>/delete', views.DeleteMeal.as_view(), name='delete_meal'),

]
