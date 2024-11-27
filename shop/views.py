from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):
    products = Product.objects.filter(status=0, trending=1)
    return render(request,"shop/home.html", {"trending":products})

def register(request):
    return render(request,"shop/register.html")

def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, "shop/collections.html", {"category":category})

def collectionsview(request, name):
    if (Category.objects.filter(name=name, status=0)):
        product = Product.objects.filter(category__name=name, status=0)
        return render(request, "shop/products/index.html", {"product_name":product,"category":name})
    else:
        messages.error(request,"No Such Category Found!")
        return redirect('collections')
    
def productdetails(request, cname, pname):
    if (Category.objects.filter(name=cname, status=0)):
        if (Product.objects.filter(name=pname, status=0)):
            products = Product.objects.filter(name=pname, status=0).first()
            return render(request, "shop/products/productdetails.html", {"products":products,"category_name":cname})
        else:
            messages.error(request, "No Such Product Found!")
    else:
        messages.error(request, "No Such Category Found!")
        return redirect("collections")