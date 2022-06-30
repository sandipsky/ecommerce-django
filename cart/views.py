from django.shortcuts import render
from ecomapp.models import Product
from .models import Cart, CartItem
# Create your views here.


def addToCart(request, pk):
    product = Product.objects.get(id=pk)

    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
        
    return render(request, 'addtocart.html')