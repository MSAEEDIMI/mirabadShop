from django.contrib.auth import logout ,authenticate,login
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .forms import Regestrform,LoginForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
User=get_user_model()

class RegisterFormView(FormView):
    template_name = "users_app/register.html"
    form_class=Regestrform
    success_url=reverse_lazy("home_app:home")
    
    def form_valid(self, form):
        username=form.cleaned_data.get("username")
        first_name=form.cleaned_data.get("first_name")
        last_name=form.cleaned_data.get("last_name")
        email=form.cleaned_data.get("email")
        phone_number=form.cleaned_data.get("phone_number")
        password2=form.cleaned_data.get("password2")
        user=User.objects.create_user(phone=phone_number,first_name=first_name,last_name=last_name,password=password2,email=email) # type: ignore
        login(self.request,user)    
        return super().form_valid(form)
    
class LoginFormView(FormView):
    template_name = "users_app/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home_app:home")

    def form_valid(self, form):
        phone = form.cleaned_data.get('phone')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, phone=phone, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
            return self.form_invalid(form)
    


def logoutFromSite(requst):
    logout(requst)
    return redirect('home_app:home')