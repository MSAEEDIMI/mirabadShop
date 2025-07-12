from django.urls import path
from . import views
app_name="home_app"

urlpatterns = [
    path('',views.home_app,name="home"), 
    path('search/',views.serach,name="search"), 
]