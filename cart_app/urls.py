from django.urls import path
from . import views

app_name="cart_app"

urlpatterns = [
    path('cart_detale',views.CartDetaleView.as_view(),name="cart_detale"),
    path('cart_add/<int:id>',views.CartAddView.as_view(),name="cart_add"),
]