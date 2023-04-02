from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class AddAppealForm(forms.ModelForm):
    class Meta:
        model = appeal
        fields = ['name', 'city', 'appeal_text', 'e_mail', 'phone_number', 'photo']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) == 0:
            raise ValidationError('Поле должно быть заполнено!')
        return name

    def clean_city(self):
        city = self.cleaned_data['city']
        if len(city) == 0:
            raise ValidationError('Поле должно быть заполнено!')
        return city

    def clean_appeal_text(self):
        appeal_text = self.cleaned_data['appeal_text']
        if len(appeal_text) == 0:
            raise ValidationError('Поле должно быть заполнено!')
        return appeal_text

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))