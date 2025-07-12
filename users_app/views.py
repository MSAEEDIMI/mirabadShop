from django.shortcuts import render
from .forms import Regestrform
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Regestrform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pass
    else:
        form = Regestrform()
    return render(request,"users_app/register.html",{"form":form})


def login(requst):
    return render(requst,"users_app/login.html")