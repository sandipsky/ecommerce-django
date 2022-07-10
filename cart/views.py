from django.http import HttpResponse
from django.shortcuts import render, redirect
from ecomapp.models import Product
from .cart import Cart
# Create your views here.


def addToCart(request, pk):
    if request.method == 'POST':
        print(request.session.get("product_cart"))
        product = Product.objects.get(id=pk)
        if request.POST['quantity']:
            quantity = request.POST['quantity']
        else:
            quantity = 1
        if not quantity:
            quantity = 1
        cart  = Cart(request)
        cart.add(product,quantity)
        return redirect('cart')
    return HttpResponse("Item added")


def cart(request):
    cart = Cart(request)
	# carts = cart.list()
    context = {
		'cart':cart
	}
    
    return render(request, 'cart.html', context)

def update_cart(request,id):
   if request.method == 'POST':
      data = request.POST
      quantity = data['quantity']
      cart = Cart(request)
      cart.update(quantity,id)

      context = {
            'cart':cart
         }

      return render(request,'cart.html',context)


def delete_cart(request,id):
   cart = Cart(request)
   cart.delete(id)
   context = {
            'cart':cart
         }
   return render(request,'cart.html',context)


def checkout(request):
    cart = Cart(request)
    context = {
		'cart':cart
    }
    return render(request, 'checkout.html', context)

    