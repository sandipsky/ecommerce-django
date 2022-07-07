from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<str:pk>', views.productSpecs, name='specs'),
    path('contact/', views.contact, name='contact'),
    path('contact/success', views.success, name='success'),

]
