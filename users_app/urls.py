
from django.urls import path 
from . import views

app_name='users_app'

urlpatterns = [
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('logout/',views.logoutFromSite,name='logout'),
    path('final_register/',views.RegisterFormView.as_view(),name='register'),
    path('phone_register/',views.RgisterPhoneView.as_view(),name='phone_register'),
        path('validate_code/',views.ValidateCodeView.as_view(),name='validate_code'),

]
