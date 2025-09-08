
from django.urls import path 
from . import views

app_name='users_app'

urlpatterns = [
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('logout/',views.logoutFromSite,name='logout'),
    path('final/register/',views.RegisterFormView.as_view(),name='register'),
    path('phone/register/',views.RgisterPhoneView.as_view(),name='phone_register'),
    path('validate/code/',views.ValidateCodeView.as_view(),name='validate_code'),
    path('add/address/',views.AddAddressView.as_view(),name='add_address'),
]
