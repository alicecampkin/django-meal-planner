from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login',views.SignIn.as_view(), name='login'),
    path('profile/<int:pk>',views.UpdateUser.as_view(), name='profile'),
    path('profile/<int:pk>/change',views.ChangePassword.as_view(), name='changepassword'),
    path('profile/done',views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]