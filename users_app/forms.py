from typing import Any
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User=get_user_model()

class Regestrform(forms.Form):
    first_name=forms.CharField(label='نام *:', widget=forms.TextInput( attrs={"class":"form-control" }))
    last_name=forms.CharField(label='نام خانوادگی *:', widget=forms.TextInput( attrs={"class":"form-control" }))
    phone_number=forms.CharField(label='شماره تلفن :',widget=forms.TextInput(attrs={"class":"form-control"}))
    password1=forms.CharField(label='رمز عبور *:‌',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label='تکرار رمز عبور *:',widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        phone=cleaned_data.get("phone_number")
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("پسورد ها یکی نیستن ")
        
        if User.objects.filter(phone=phone).exists() :
            raise ValidationError("کاربر با این شماره تلفن در سامانه موجود است ")
        
        return cleaned_data




class LoginForm(forms.Form):
    phone=forms.CharField(label="شماره تلفن :", widget=forms.TextInput( attrs={"class":"form-control" }))
    password=forms.CharField(label='رمز ورود :', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    
    def clean_password(self):
        user1 = authenticate(phone=self.cleaned_data["phone"],password=self.cleaned_data["password"])
        if user1 is not None:
            return self.cleaned_data.get("password")
        raise ValidationError("این کاربر در سایت عضو نمیباشد :)",code='user_is_not_on_Db')