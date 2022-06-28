from unicodedata import category
from django.shortcuts import render
from .models import Category, Brand, Product
from django.db.models import Count

# Create your views here.

def index(request):
    pass



def products(request):
    products = Product.objects.all()
    count = Product.objects.count()
    categories = Category.objects.all().annotate(product_count=Count('product'))
    brands = Brand.objects.all().annotate(product_count=Count('product'))
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.objects.filter(category = categoryID)
    brandID = request.GET.get('brand')
    if brandID:
        products = Product.objects.filter(brand = brandID)   
    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
        'count' : count,

    }
    return render(request, 'products.html', context)


