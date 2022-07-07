from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:pk>', views.addToCart, name='addtocart'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]