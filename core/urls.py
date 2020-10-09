from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lets-get-started', views.initialise_members, name='create_profile'),
    path('household/members', views.list_members, name='list_members'),
    path('household/members/add', views.AddMember.as_view(), name='add_member'),
    path('household/members/<int:pk>/update',
         views.UpdateMember.as_view(), name='update_member'),
    path('household/members/<int:pk>/delete',
         views.DeleteMember.as_view(), name='delete_member')
]
