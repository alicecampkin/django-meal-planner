from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),

    path('login', views.SignIn.as_view(), name='login'),

    path('logout', views.LogoutView.as_view(), name='logout'),

    path(
        'accounts/password_change',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change_form.html'),
        name='change_password'
    ),

    path(
        'accounts/password_change/done',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'),
        name='password_change_done'
    ),

    path(
        'accounts/password_reset',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset_form.html'),
        name='password_reset'
    ),

    path(
        'accounts/password_reset/done',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'),
        name='password_reset_done'
    ),

    path(
        'accounts/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),

    path(
        'accounts/reset/done',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete',
    )

]
