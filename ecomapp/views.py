from unicodedata import category
from django.shortcuts import render
from .models import Category, Brand, Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {
        'products': products,
        'brands': brands,
        'categories': categories

    }
    return render(request, 'index.html', context)