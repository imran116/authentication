from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('password/reset', views.PasswordReset.as_view(), name='password-reset'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'password-forgot.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password-forgot-message.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password-forgot-confirm-message.html'), name='password_reset_complete'),


]