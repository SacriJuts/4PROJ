from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
	path('achat', views.achat, name='achat'),
	path('about', views.about, name='about'),
    path('logout', views.logout, name='logout'),
	path('base', views.base, name='base'),
	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)