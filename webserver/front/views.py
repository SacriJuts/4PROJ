from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, PickProduct
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import Product, Cart
from datetime import datetime

def index(request):

    context = {
        'loginform' : LoginForm(),
        'registerform' : RegisterForm(),
        'user' : request.user,
    }

    if request.method == "POST":
        if request.POST.get('formtype') == "login":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect("/front/")
            else :
                context['error'] = "Wrong login"
        elif request.POST.get('formtype') == "register":
            f = RegisterForm(request.POST)
            if f.is_valid():
                f.save()

    return render(request, 'front/index.html', context)

def contact(request):
    context = {
    }
    return render(request, 'front/contact.html', context)
	
def achat(request):
    context = {
        'user' : request.user,
    }
    return render(request, 'front/achat.html', context)

def scan(request):


    context = {
        'products' : Product.objects.filter(cart = None),
        'pickproduct' : PickProduct(),
    }
    currentCart = ""
    if (Cart.objects.filter(date=None).count() == 0):
        currentCart = Cart(client=request.user)
    else:
        currentcart = Cart.objects.get(client = request.user.id, date = None)

    context['cart'] = currentCart
    if request.method == "POST":
        if request.POST.get("formtype") == "addproduct":
            qr = request.POST.get("qrcode")
            product = Product.objects.get(qrcode = qr)
            product.cart = currentcart
            product.save()
        elif request.POST.get("formtype") == "deleteproduct":
            qr = request.POST.get("qrcode")
            product = Product.objects.get(qrcode = qr)
            product.cart = None
            product.save()
        elif request.POST.get("formtype") == "submitcart":
            currentcart.date = datetime.now()
            currentcart.save()


    return render(request, 'front/scan.html', context)

def about(request):
    context = {
    }
    return render(request, 'front/about.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/front")
