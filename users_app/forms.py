from typing import Any
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class Regestrform(forms.Form):
    first_name=forms.CharField(label='نام *:', widget=forms.TextInput( attrs={"class":"form-control" }))
    last_name=forms.CharField(label='نام خانوادگی *:', widget=forms.TextInput( attrs={"class":"form-control" }))
    email=forms.CharField(label='ایمیل *:',widget=forms.EmailInput(attrs={"class":"form-control"}))
    phone_number=forms.CharField(label='شماره تلفن :',widget=forms.TextInput(attrs={"class":"form-control"}))
    password1=forms.CharField(label='رمز عبور *:‌',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label='تکرار رمز عبور *:',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    username=forms.CharField(help_text="باید ترکیبی از حروف انگلیسی و اعداد و نماد ها باشد ." ,label="نام کاربری *:",widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        username=cleaned_data.get("username")
        email=cleaned_data.get("email")
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("پسورد ها یکی نیستن ")
        
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            raise ValidationError("کاربر با این ایمیل و نام کاربری موجود است ")
        
        return cleaned_data




class LoginForm(forms.Form):
    username=forms.CharField(label="نام کاربری :", widget=forms.TextInput( attrs={"class":"form-control" }))
    password=forms.CharField(label='رمز ورود :', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    
    def clean_password(self):
        user1 = authenticate(username=self.cleaned_data["username"],password=self.cleaned_data["password"])
        if user1 is not None:
            return self.cleaned_data.get("password")
        raise ValidationError("این کاربر در سایت عضو نمیباشد :)",code='user_is_not_on_Db')