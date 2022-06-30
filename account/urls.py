from django.urls import path, include
from django.contrib.auth import views as auth_views 

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('password_reset/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name='password_reset.html',
    #          subject_template_name='registration/password_reset_subject.txt',
    #          email_template_name='registration/password_reset_email.html',
    #      ),name='password_reset'),
    # path('password_reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='password_reset_done.html'
    #      ),name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='password_reset_confirmation.html'
    #      ),name='password_reset_confirm'),
    # path('password_reset_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='password_reset_complete.html'
    #      ),name='password_reset_complete'),

    path('', include('django.contrib.auth.urls')),
    path('edit/', views.userEdit, name='edit'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
