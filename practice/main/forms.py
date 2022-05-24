from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name_e', 'about', 'time', 'evtype')


class EventFormModer(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class UCardForm(forms.ModelForm):
    class Meta:
        model = UserCard
        fields = '__all__'

'''class EventForm(forms.Form):
    name_e = forms.CharField(label='Название мероприятия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    about = forms.CharField(label='Описание мероприятия', widget=forms.Textarea(attrs={'cols': 68, 'rows': 10}))
    time = forms.DateTimeField(label='Дата и время проведения', widget=forms.DateTimeInput)
    evtype = forms.ModelChoiceField(label='Тип мероприятия', queryset=Evtype.objects.all(), empty_label="Категория не выбрана")

    class Meta:
        model = Event
        fields = ('name', 'about', 'time', 'evtype')'''


