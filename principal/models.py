from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()

class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	title = models.CharField(max_length=255)
	details =  models.TextField()

