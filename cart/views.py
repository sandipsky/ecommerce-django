from django.shortcuts import render
from ecomapp.models import Product
from .models import Cart, CartItem
from ecomapp.models import Product
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

def cart(request):
    products = Product.objects.all()[:5]
    
    return render(request, 'cart.html', {'products': products})

def checkout(request):
    products = Product.objects.all()[:5]
    return render(request, 'checkout.html', {'products': products})

    