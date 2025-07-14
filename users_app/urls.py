
from django.urls import path 
from . import views

app_name='users_app'

urlpatterns = [
    path('login/',views.loginToSite,name='login'),
    path('logout/',views.logoutFromSite,name='logout'),
    path('register/',views.register,name='register'),
]
