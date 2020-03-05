from django.db import models

class Ingredients(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField(null=True, blank=True)
	ingredients = models.ManyToManyField(Ingredients, blank=True)
	image = models.ImageField(upload_to='image', null=True)
	details = models.TextField(null=True)

	def __str__(self):
		return self.name
		
class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	title = models.CharField(max_length=255)
	details =  models.TextField()

	def __str__(self):
		return self.name