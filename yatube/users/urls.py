# users/urls.py
from . import views
# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
      'logout/',
      LogoutView.as_view(
      template_name='users/logged_out.html'),
      name='logout'
    ),
    path(
      'login/',
      LoginView.as_view(
      template_name='users/login.html'),
      name='login'
    ),
    path(
      'auth/password_change/done/',
      PasswordChangeDoneView.as_view(
      template_name='users/password_change_done.html'),
      name='password_change'
    ),
    path(
      'auth/reset/done',
      PasswordResetCompleteView.as_view(
      template_name='users/password_reset_complite.html'),
      name='password_reset_complite'
    ),
    path(
      'auth/reset/<uidb64>/<token>/',
      PasswordResetConfirmView.as_view(
      template_name='users/password_reset_confirm.html'),
      name='password_reset_confirm'
    ),
    path(
      'auth/password_reset/done/',
      PasswordResetDoneView.as_view(
      template_name='users/password_reset_done.html'),
      name='password_reset_done'
    ),
    path(
      'auth/password_change/',
      PasswordChangeView.as_view(
      template_name='users/password_change_form.html'),
      name='password_change'
    ),
    path(
      'auth/password_reset/',
      PasswordResetView.as_view(
      template_name='users/password_reset_form.html'),
      name='password_reset_form'
    ),
] 