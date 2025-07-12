from django.urls import path
from . import views

app_name="products_app"

urlpatterns = [
    path('products',views.products,name='products'),
    path('product/<slug:slug>',views.product,name='product')
]
