from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 50)
	password = models.CharField(max_length = 64)
	mail = models.CharField(max_length = 150)
	qrcode = models.CharField(max_length = 200)
	admin = models.BooleanField()

class Cart(models.Model) :
	client = models.ForeignKey(User, on_delete = models.CASCADE)
	finalised = models.BooleanField()

class Shelf(models.Model):
	position_x = models.FloatField()
	position_y = models.FloatField()


class Product(models.Model):
	cart = models.ForeignKey(Cart, on_delete = models.DO_NOTHING)
	shelf = models.ForeignKey(Shelf, on_delete = models.DO_NOTHING)
	price = models.IntegerField()
	name = models.CharField(max_length = 500)
	qrcode = models.CharField(max_length = 200)
	serial_number = models.CharField(max_length = 100)
