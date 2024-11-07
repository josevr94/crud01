from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm



# Create your views here.

def order_created(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request,'orders/order_form.html',{'form':form})

def order_list(request):
    orders = Order.objects.all()
    return render(request,'orders/order_list.html',{'orders':orders})


def report_view(request):
    orders = Order.objects.select_related('product').all()
    return render(request,'orders/reports.html',{'orders': orders})