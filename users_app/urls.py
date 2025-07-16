
from django.urls import path 
from . import views

app_name='users_app'

urlpatterns = [
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('logout/',views.logoutFromSite,name='logout'),
    path('register/',views.RegisterFormView.as_view(),name='register'),
]
