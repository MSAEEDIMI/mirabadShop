from django.urls import path
from . import views

app_name="cart_app"

urlpatterns = [
    path('cart_detale',views.CartDetaleView.as_view(),name="cart_detale"),
    path('cart_add/<int:id>',views.CartAddView.as_view(),name="cart_add"),
    path("cart_clear",views.cart_clear,name='cart_clear'),
    path('cart_remove/<str:id>',views.cart_remove,name='cart_remove'),
    path('order/add',views.OrderCreation.as_view(),name='order_creation'),
    path('order/<int:pk>',views.OrderDetale.as_view(),name='order_detale')
]