from django.contrib.auth import logout ,authenticate,login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render ,redirect
from django.views import View
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
    
class LoginFormView(View):
    
    def get(self,reqeust):
        form=LoginForm()
        return render(reqeust,'users_app/login.html',context={'form':form})
    
    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            print(phone)
            user = authenticate(phone=phone, password=password)
            if user is not None:
                login(self.request, user)
                return redirect('/')
            else:
                form.add_error("phone", "نام کاربری یا رمز عبور اشتباه است.")
        else:
            return form.add_error("phone","اطلاعات وارد شده صحیح نیست . ")
             
        return render(request,'users_app/login.html',context={'form':form})

def logoutFromSite(requst):
    logout(requst)
    return redirect('home_app:home')