from multiprocessing import context
from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404

from .models import*





def home(request):
    products = Product.objects.all()
    warehouses = Warehouse.objects.all()
    context = {
        "products": products,
        "warehouses": warehouses
    }
    return render(request, 'app/home.html', context) 

def warehouse(request):
    warehouse = Warehouse.objects.all()
    context = {
        "warehouses": warehouse
    }
    return render(request, 'app/warehouses.html', context) 


def create(request):
    obj = Product()
    warehouses = Warehouse.objects.all()
    context = { 
        'warehouses' : warehouses
    }

    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.price = request.POST.get('price')
        obj.quantity = request.POST.get('quantity')
        obj.warehouse = Warehouse.objects.get(name=request.POST.get('warehouse'))
        #obj.warehouse = request.POST.get('warehouse')
        
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


def deleteWarehouse(request, id):
    obj = Warehouse.objects.get(id=id)
    obj.delete()
    context = {
        "warehouses": Warehouse.objects.all(),
    }
    return redirect('/warehouses')


def createWarehouse(request):
    obj = Warehouse()
    obj2 = Warehouse()
    context = { }
    if request.method == 'POST':
        try:
            obj2 = Warehouse.objects.get(name=request.POST.get('name'))
            print("[the warehouse with that name already exists]")
        except Warehouse.DoesNotExist:
            obj.name = request.POST.get('name')
            obj.address = request.POST.get('address')
            obj.city = request.POST.get('city')
            obj.save()
            
        return redirect('/warehouses') 
    return redirect('/warehouses') 

def updateWarehouse(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        obj = Warehouse.objects.get(id=id)
        obj.name = request.POST.get('name')
        obj.address = request.POST.get('address')
        obj.city = request.POST.get('city')
        
        obj.save()
        return redirect('/warehouses')
    return redirect('/warehouses')

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        obj = Product.objects.get(id=id)
        obj.name = request.POST.get('name')
        obj.price = request.POST.get('price')
        obj.quantity = request.POST.get('quantity')
        
        obj.save()
        return render('/')
    return redirect('/')


    context = {}
    return render(request, 'app/update.html', context)

def detail(request, id):
    context = {}
    return render(request, 'app/detail.html', context)