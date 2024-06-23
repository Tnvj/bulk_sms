from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, UploadFilesForm
from django.shortcuts import render
import csv
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact

@login_required
def upload_files(request):
    if request.method == 'POST':
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            files_uploaded = False
            for file_field in ['file1', 'file2', 'file3', 'file4', 'file5']:
                file = request.FILES.get(file_field)
                if file:
                    files_uploaded = True
                    if file.name.endswith('.csv'):
                        data = csv.reader(file.read().decode('utf-8').splitlines())
                        next(data)  # Skip the header row
                        for row in data:
                            Contact.objects.update_or_create(
                                user=request.user,
                                name=row[0],
                                defaults={'phone_number': row[1]}
                            )
                    elif file.name.endswith(('.xls', '.xlsx')):
                        data = pd.read_excel(file)
                        for index, row in data.iterrows():
                            Contact.objects.update_or_create(
                                user=request.user,
                                name=row['name'],
                                defaults={'phone_number': row['phone_number']}
                            )
            if files_uploaded:
                messages.success(request, "Contacts uploaded successfully.")
                return redirect('index')
            else:
                messages.error(request, "Please upload files.")
    else:
        form = UploadFilesForm()
    return render(request, 'upload_files.html', {'form': form})
    
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
