from django.db import models

class Ingredients(models.Model):
	name = models.CharField(max_length=255)

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	ingredients = models.ManyToManyField(Ingredients)

class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	title = models.CharField(max_length=255)
	details =  models.TextField()

