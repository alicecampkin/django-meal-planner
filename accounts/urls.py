from django.urls import include, path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('profile/<int:pk>',views.UpdateUser.as_view(), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]