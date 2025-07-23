from django.contrib.auth import logout ,authenticate,login
from django.shortcuts import render ,redirect
from django.views import View
from .forms import Regestrform,LoginForm,Phone_validate_form,Phone_validate_code_form
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from kavenegar import *
from .models import Otp
from random import randint
import uuid
User=get_user_model()

class RegisterFormView(FormView):
    template_name = "users_app/register.html"
    form_class=Regestrform
    success_url=reverse_lazy("home_app:home")
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect("home_app:home")
        username=form.cleaned_data.get("username")
        first_name=form.cleaned_data.get("first_name")
        last_name=form.cleaned_data.get("last_name")
        email=form.cleaned_data.get("email")
        phone_number=form.cleaned_data.get("phone_number")
        password2=form.cleaned_data.get("password2")
        user=User.objects.create_user(phone=phone_number,first_name=first_name,last_name=last_name,password=password2,email=email) # type: ignore
        login(self.request,user)    
        return super().form_valid(form)
    
class LoginFormView(View):
    def get(self,reqeust):
        if reqeust.user.is_authenticated:
            return redirect('home_app:home') 
        form=LoginForm()
        return render(reqeust,'users_app/login.html',context={'form':form})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home_app:home') 
        form=LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user = authenticate(phone=phone, password=password)
            if user is not None:
                login(self.request, user)
                return redirect('/')
            else:
                form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
        else:
            form.add_error(None,"اطلاعات وارد شده صحیح نیست . ")
             
        return render(request,'users_app/login.html',context={'form':form})


class RgisterPhoneView(View):
    def get(self,reqeust):
        if reqeust.user.is_authenticated:
            return redirect('home_app:home') 
        form=Phone_validate_form()
        return render(reqeust,'users_app/register_phone.html',context={'form':form})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home_app:home') 
        form=Phone_validate_form(request.POST)
        if form.is_valid():
            code=randint(1000,10000)
            token=uuid.uuid4()
            phone = form.cleaned_data.get('phone')
            Otp.objects.create(token=token,phone=phone,code=code)
            print(token)
            print(code) 
            return redirect(reverse("users_app:validate_code")+f"?token={token}")     
        else:
            form.add_error(None,"اطلاعات وارد شده صحیح نیست . ")
             
        return render(request,'users_app/register_phone.html',context={'form':form})


class ValidateCodeView(View):
    def get(self,reqeust):
        if reqeust.user.is_authenticated:
            return redirect('home_app:home') 
        form=Phone_validate_code_form()
        return render(reqeust,'users_app/validate_phone.html',context={'form':form})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home_app:home') 
        form=Phone_validate_code_form(request.POST)
        if form.is_valid():
            token=request.GET.get("token")
            code = form.cleaned_data.get('code')
            if Otp.objects.filter(code=code,token=token).exists():
                newUser=Otp.objects.get(token=token)
                if User.objects.filter(phone=newUser.phone).exists():
                    user=User.objects.get(phone=newUser.phone)
                    login(request,user)
                    newUser.delete()
                    return redirect("home_app:home")
                user,is_created=User.objects.get_or_create(phone=newUser.phone)
                login(request,user)
                newUser.delete()
                return redirect("home_app:home")
        else:
            form.add_error(None,"اطلاعات وارد شده صحیح نیست . ")
             
        return render(request,'users_app/validate_phone.html',context={'form':form})




def logoutFromSite(requst):
    logout(requst)
    return redirect('home_app:home')