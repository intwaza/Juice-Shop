from typing import Reversible
from django.shortcuts import redirect, render
from homePage.models import Products
from homePage.forms import RegistrationForm
from .models import Register
from django.urls import reverse



def home(request):
    products= Products.objects.all()
    return render(request,"home.html" ,{"products": products})
    # return render(request,template_name='home.html')

# def products(request):
    

def product_view(request,id):
    product= Products.objects.get(id=id)
    return render(request, "product_view.html",{"product":product})


def register(request):
    if request.method=="POST":
        form= RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect (reverse("registered"))
        else:
            print(form.errors)
    else:
        form= RegistrationForm()
    return render(request,"register.html",{"form":form})


def register_list(request):
    customers= Register.objects.all()
    return render(request, "register_list.html",{"customers": customers})

def registered(request):
    return render(request,template_name='registered.html')