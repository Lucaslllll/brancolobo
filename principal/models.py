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



class Initial(models.Model):
	title = models.TextField()
	subtitle = models.TextField()

	def __str__(self):
		return self.title

class How_Use(models.Model):
	title = models.CharField(max_length=500, null=True)
	details = models.TextField()
	image = models.ImageField(upload_to='image/how_use')

	def __str__(self):
		return self.title

class How_Use_Text(models.Model):
	title = models.CharField(max_length=500)
	subtitle = models.CharField(max_length=500)
	details = models.TextField()

class Video_Description(models.Model):
	title = models.CharField(max_length=500, null=True)
	details = models.TextField()
	video = models.FileField(upload_to='video')

