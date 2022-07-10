from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:pk>', views.addToCart, name='addtocart'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('cart/update_cart/<int:id>',views.update_cart,name='update_cart'),
    path('cart/delete_cart/<int:id>',views.delete_cart,name='delete_cart'),
]