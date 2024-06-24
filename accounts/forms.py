from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from .models import UploadedFile

class UploadFilesForm(forms.Form):
    file1 = forms.FileField(required=False)
    file2 = forms.FileField(required=False)
    file3 = forms.FileField(required=False)
    file4 = forms.FileField(required=False)
    file5 = forms.FileField(required=False)
    
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('name', 'email', 'phone_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('name', 'email', 'phone_number')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'password')

class SMSSendForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=20, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']