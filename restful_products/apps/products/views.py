from django.shortcuts import render, HttpResponse, redirect
from models import Product
  # Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()[::-1]
    }

    return render(request, "products/index.html", context)

def show(request, id):
    context = {
        'product': Product.objects.get(id=id)
    }

    return render(request, "products/show.html", context)

def new(request):

    return render(request, "products/new.html")

def edit(request, id):
    context = {
        'product': Product.objects.get(id=id)
    }

    return render(request, "products/edit.html", context)

def create(request):
    Product.objects.create_new_product(request)

    return redirect("products:index")

def update(request, id):
    Product.objects.update_product(request, id)

    return redirect("products:index")

def destroy(request):
    pass
