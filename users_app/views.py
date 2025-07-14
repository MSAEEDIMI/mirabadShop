from django.contrib.auth import logout ,authenticate,login
from django.shortcuts import render ,redirect
from .forms import Regestrform,LoginForm
from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    
    if request.method == "POST":
        form = Regestrform(request.POST)
        context={"errors":[],
                 "form":form,
                 }
        if form.is_valid():
            username=form.cleaned_data.get("username")
            first_name=form.cleaned_data.get("first_name")
            last_name=form.cleaned_data.get("last_name")
            email=form.cleaned_data.get("email")
            phone_number=form.cleaned_data.get("phone_number")
            password1=form.cleaned_data.get("password1")
            password2=form.cleaned_data.get("password2")
            if password1 !=password2:
                context["errors"].append("پسورد ها مشابه نیستند")
                return render(request,"users_app/register.html",context)
            if User.objects.filter(username=username).exists():
                context["errors"].append("کاربر با این نام کاربری موجود است!!! ")
                return render(request,"users_app/register.html",context)
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password2,email=email) # type: ignore
            login(request,user)    
            return redirect("home_app:home")
        else:
            context["errors"].append("اطلاعات وارد شده معتبر نیست.")
            return render(request, "users_app/register.html", context)
    else:
        form = Regestrform()
    return render(request,"users_app/register.html",{"form":form})


def loginToSite(requst):
    if requst.method=="POST":
        form=LoginForm(requst.POST)
        if form.is_valid:
            username=form.cleaned_data.get('username')
            user=User.objects.get(username=username)
            login(requst,user)
            return redirect("home_app:home")
    else:
        form=LoginForm()
    
    return render(requst,"users_app/login.html",context={"form":form})



def logoutFromSite(requst):
    logout(requst)
    return redirect('home_app:home')