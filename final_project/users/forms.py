from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
        )
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserInfoForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Your first name',
        max_length=100
    )
    last_name = forms.CharField(
        label='Your last name',
        max_length=50
    )
    email = forms.EmailField(
        label='Your email'
    )
    model = forms.ChoiceField(
        label='Your prefer model',
        choices=CHOISE_MODEL
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
