from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, UploadFileForm, SMSSendForm
from django.shortcuts import render
import csv
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from twilio.rest import Client
from .models import Contact, UploadedFile
from django.http import HttpResponse
from accounts.utils import send_sms


@login_required
def send_sms_view(request):
    if request.method == 'POST':
        form = SMSSendForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            if send_sms(phone_number, message):
                return HttpResponse('SMS sent successfully!')
            else:
                return HttpResponse('Failed to send SMS. Please try again later.')
    else:
        form = SMSSendForm()

    return render(request, 'send_sms.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

@login_required
def upload_file(request):
    # Check if the user has already uploaded a file
    already_uploaded = UploadedFile.objects.filter(user=request.user).exists()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Check again if the user has already uploaded (in case of concurrent requests)
            if not already_uploaded:
                uploaded_file = form.save(commit=False)
                uploaded_file.user = request.user
                uploaded_file.save()
                messages.success(request, 'File uploaded successfully.')
                return redirect('upload_success')  # Replace with your desired redirect
            else:
                messages.error(request, 'You have already uploaded a file.')
        else:
            messages.error(request, 'Error uploading file. Please try again.')
    else:
        form = UploadFileForm()

    return render(request, 'upload_files.html', {'form': form, 'already_uploaded': already_uploaded})


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def profile_update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile_update.html', {'form': form})
