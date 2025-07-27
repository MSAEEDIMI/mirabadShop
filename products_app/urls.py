from django.urls import path
from . import views
from .views import ProductsDetailView
app_name="products_app"

urlpatterns = [
    path('products',views.products,name='products'),
    path('product/<slug:slug>',ProductsDetailView.as_view(),name='product')
]
