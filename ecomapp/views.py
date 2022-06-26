from unicodedata import category
from django.shortcuts import render
from .models import Category, Brand, Product
from django.db.models import Count

# Create your views here.

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all().annotate(product_count=Count('product'))
    brands = Brand.objects.all().annotate(product_count=Count('product'))
    context = {
        'products': products,
        'brands': brands,
        'categories': categories

    }
    return render(request, 'products.html', context)