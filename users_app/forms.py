from typing import Any
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate


class Regestrform(forms.Form):
    first_name=forms.CharField(label='نام *:', widget=forms.TextInput( attrs={"class":"form-control" }))
    last_name=forms.CharField(label='نام خانوادگی *:', widget=forms.TextInput( attrs={"class":"form-control" }))
    email=forms.CharField(label='ایمیل *:',widget=forms.EmailInput(attrs={"class":"form-control"}))
    phone_number=forms.CharField(label='شماره تلفن :',widget=forms.TextInput(attrs={"class":"form-control"}))
    password1=forms.CharField(label='رمز عبور *:‌',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label='تکرار رمز عبور *:',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    username=forms.CharField(help_text="باید ترکیبی از حروف انگلیسی و اعداد و نماد ها باشد ." ,label="نام کاربری *:",widget=forms.TextInput(attrs={"class":"form-control"}))


class LoginForm(forms.Form):
    username=forms.CharField(label="نام کاربری :", widget=forms.TextInput( attrs={"class":"form-control" }))
    password=forms.CharField(label='رمز ورود :', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    
    def clean_password(self):
        user1 = authenticate(username=self.cleaned_data["username"],password=self.cleaned_data["password"])
        if user1 is not None:
            return self.cleaned_data.get("password")
        raise ValidationError("این کاربر در سایت عضو نمیباشد :)",code='user_is_not_on_Db')