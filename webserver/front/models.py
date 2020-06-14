from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	qrcode = models.CharField(max_length = 200)

	def __str__(self):
		return self.username

class Cart(models.Model) :
	client = models.ForeignKey(User, on_delete = models.CASCADE)
	date = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		pre = " - In progress"
		if self.date != None:
			pre = " - " + self.date.ctime()
		return self.client.username + pre

class Shelf(models.Model):
	name = models.CharField(max_length=50)
	position_x = models.FloatField()
	position_y = models.FloatField()

	def __str__(self):
		return self.name + " (" + str(self.position_x) + ", " + str(self.position_y) + ")"

class Product(models.Model):
	cart = models.ForeignKey(Cart,null=True, blank=True, on_delete = models.DO_NOTHING)
	shelf = models.ForeignKey(Shelf, on_delete = models.DO_NOTHING)
	price = models.IntegerField()
	name = models.CharField(max_length = 500)
	qrcode = models.CharField(unique=True, max_length = 200)
	serial_number = models.CharField(max_length = 100)

	def __str__(self):
		pre = " - Available"
		if self.cart != None:
			pre = " - Bought"
		return self.name + pre
