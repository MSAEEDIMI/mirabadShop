import re
from django.core import validators
from django import forms
from django.forms import ValidationError
from django.contrib.auth import get_user_model
User=get_user_model()

def validate_phone(value):
    pattern1 = r'^09\d{9}$'
    if not re.match(pattern1, value):
        raise ValidationError('شماره تلفن معتبر نیست و باید با ۰۹ شروع شود .')



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
    phone=forms.CharField(label="شماره تلفن :", validators=[validators.MaxLengthValidator(13),validate_phone],widget=forms.TextInput( attrs={"class":"form-control" ,"placeholder":"شماره تلفن به 09 شروع شود"}))
    password=forms.CharField(label='رمز ورود :', widget=forms.PasswordInput(attrs={"class":"form-control"}))



class Phone_validate_form(forms.Form):
    phone=forms.CharField(label="شماره تلفن :", validators=[validators.MaxLengthValidator(13),validate_phone],widget=forms.TextInput( attrs={"class":"form-control" ,"placeholder":"شماره تلفن به 09 شروع شود"}))


class Phone_validate_code_form(forms.Form):
    code=forms.CharField(label="کد دریافتی :", validators=[validators.MaxLengthValidator(4)],widget=forms.TextInput( attrs={"class":"form-control",'maxlength':"4" }))
