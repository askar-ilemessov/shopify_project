from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404

from .models import*





def home(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'app/home.html', context) 

def create(request):
    obj = Product()
    context = { }

    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.price = request.POST.get('price')
        obj.quantity = request.POST.get('quantity')
        
        obj.save()
        return redirect('/')
    return render(request, '', context)

def delete(request, id):
    obj = Product.objects.get(id=id)
    obj.delete()
    context = {
        "product": Product.objects.all(),
    }
    return redirect('/')




def update(request):

    if request.method == 'POST':
        id = request.POST.get('id')
        obj = Product.objects.get(id=id)
        obj.name = request.POST.get('name')
        obj.price = request.POST.get('price')
        obj.quantity = request.POST.get('quantity')
        
        obj.save()
        return redirect('/')
    return redirect('/')


    context = {}
    return render(request, 'app/update.html', context)

def detail(request, id):
    context = {}
    return render(request, 'app/detail.html', context)