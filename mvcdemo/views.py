from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import *

def home(request):
    products = Product.objects.all()
    total_products = products.count()
    context = {
        'products' : products,
        'total_products' : total_products
    }
    return render(request, 'home.html', context)

def post_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    context = {'form' : form}
    return render(request, 'post_product.html', context)

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form
    }
    return render(request, 'post_product.html', context)

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/')
    context = {
            'item' : product
        }
    return render(request, 'delete.html', context)
