from unicodedata import category
from django.shortcuts import redirect, render
from .models import Category, Brand, Product
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    search=""
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(name__icontains=search)
    return render(request, 'index.html')



def products(request):
    search=""
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()
    count = Product.objects.count()
    categories = Category.objects.all().annotate(product_count=Count('product'))
    brands = Brand.objects.all().annotate(product_count=Count('product'))
    categoryID = request.GET.get('category')
    print(categoryID)
    if categoryID:
        products = Product.objects.filter(category=categoryID)
    brandID = request.GET.get('brand')
    if brandID:
        products = Product.objects.filter(brand=brandID)
    paginator = Paginator(products, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
        'count' : count,
        'search': search,
        'page_obj': page_obj,

    }
    return render(request, 'products.html', context)


