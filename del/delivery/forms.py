from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import GetUserInfo


class UserInfo(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password1']
        del self.fields['password2']

    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    tel_num = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))
    comment = forms.CharField(label='Ваш комментарий', widget=forms.TextInput(attrs={'class': 'from-input'}))
    address = forms.CharField(label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'form-input'}))

    field_order = ['name', 'tel_num', 'comment', 'address']

    class Meta:
        model = GetUserInfo
        fields = {'name', 'tel_num', 'comment', 'address'}