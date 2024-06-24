# sms/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, user_login, profile_update, index, upload_files,user_logout, send_sms_view

urlpatterns = [
     path('', index, name='index'),  # Home page
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile_update/', profile_update, name='profile_update'),
     path('send-sms/', send_sms_view, name='send_sms'), 
     path('upload/', upload_files, name='upload_files'),
]
