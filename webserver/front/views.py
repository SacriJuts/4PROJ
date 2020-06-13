from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    context = {
    }
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