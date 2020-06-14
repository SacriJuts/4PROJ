from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import LoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect

def index(request):

    context = {
        'loginform' : LoginForm(),
        'user' : request.user
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/front/about")
        else :
            context['error'] = "Wrong login"

    return render(request, 'front/index.html', context)


def contact(request):
    context = {
    }
    return render(request, 'front/contact.html', context)
	
def achat(request):
    context = {
    }
    return render(request, 'front/achat.html', context)
	
def about(request):
    context = {
    }
    return render(request, 'front/about.html', context)
	
def base(request):
    context = {
    }
    return render(request, 'front/base.html', context)

def logout(request):
    context = {}
    auth.logout(request)
    return HttpResponseRedirect("/front")