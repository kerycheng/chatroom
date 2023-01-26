from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class MyUserCreationForm(UserCreationForm):
    name = forms.CharField(
        label='暱稱',
    )

    username = forms.CharField(
        label='ID名稱',
        error_messages={'unique': 'ID名稱已使用'}
    )

    email = forms.EmailField(
        label='信箱'
    )

    password1 = forms.CharField(
        label='密碼',
        error_messages={"password_too_short": '密碼太短，必須至少包含 8 個字符',
                        "password_too_common": '密碼太簡單了',
                        "password_entirely_numeric": '密碼須包含至少 1 個英文字母'}
    )

    password2 = forms.CharField(
        label='請重複輸入密碼',
        error_messages={"password_too_short": '密碼太短，必須至少包含 8 個字符',
                        "password_too_common": '密碼太簡單了',
                        "password_entirely_numeric": '密碼須包含至少 1 個英文字母'}
    )

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']

        labels = {
            'avatar': '頭像',
            'name': '暱稱',
            'username': 'ID名稱',
            'email': '信箱',
            'bio': '自我介紹',
        }
