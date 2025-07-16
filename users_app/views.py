from django.contrib.auth import logout ,authenticate,login
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .forms import Regestrform,LoginForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# def register(request):
#     if request.user.is_authenticated:
#         return redirect('home_app:home')
    
#     if request.method == "POST":
#         form = Regestrform(request.POST)
#         context={"errors":[],
#                  "form":form,
#                  }
#         if form.is_valid():
#             username=form.cleaned_data.get("username")
#             first_name=form.cleaned_data.get("first_name")
#             last_name=form.cleaned_data.get("last_name")
#             email=form.cleaned_data.get("email")
#             phone_number=form.cleaned_data.get("phone_number")
#             password1=form.cleaned_data.get("password1")
#             password2=form.cleaned_data.get("password2")
#             if password1 !=password2:
#                 context["errors"].append("پسورد ها مشابه نیستند")
#                 return render(request,"users_app/register.html",context)
#             if User.objects.filter(username=username).exists():
#                 context["errors"].append("کاربر با این نام کاربری موجود است!!! ")
#                 return render(request,"users_app/register.html",context)
#             user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password2,email=email) # type: ignore
#             login(request,user)    
#             return redirect("home_app:home")
#         else:
#             context["errors"].append("اطلاعات وارد شده معتبر نیست.")
#             return render(request, "users_app/register.html", context)
#     else:
#         form = Regestrform()
#     return render(request,"users_app/register.html",{"form":form})

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
        password1=form.cleaned_data.get("password1")
        password2=form.cleaned_data.get("password2")
        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password2,email=email) # type: ignore
        login(self.request,user)    
        return super().form_valid(form)
    
    
    


class LoginFormView(FormView):
    template_name = "users_app/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home_app:home")

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
            return self.form_invalid(form)
    


def logoutFromSite(requst):
    logout(requst)
    return redirect('home_app:home')