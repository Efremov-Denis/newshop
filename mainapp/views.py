from django.shortcuts import render
from .models import ProductCategory, Product

def main(request):
    title = 'главная'
    
    products = Product.objects.all()[:4]
        
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)    

def products(request):
    return render(request, 'mainapp/products.html')
    

def contacts(request):
    return render(request, 'mainapp/contacts.html')