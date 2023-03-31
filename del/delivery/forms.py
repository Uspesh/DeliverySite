from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import GetUserInfo


class UserInfo(UserCreationForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    tel_num = forms.IntegerField(label='Номер телефона', widget=forms.NumberInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'form-input'}))

    field_order = ['name', 'tel_num', 'address']

    class Meta:
        model = GetUserInfo
        fields = {'name', 'tel_num', 'address'}