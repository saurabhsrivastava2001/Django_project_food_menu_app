from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

#creating the new form (instead of the USercreationForm ) bcz we need more functionalities

class RegisterForm (UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model= User
        fields =['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields=['image','location']


