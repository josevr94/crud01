from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .form import ProductForm
# Create your views here.


def product_created(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request,'poducts/product_form.html',{'form':form})   

def product_list(request):
    products = Product.objects.all()
    return render(request,'poducts/product_list',{'products':products}) 

def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)    
    return render(request,'poducts/products_detail.html',{'product':product})

def product_update(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance = product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request,'poducts/product_form.html',{'form': form})        