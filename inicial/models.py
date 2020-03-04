from django.db import models

class Information_Page(models.Model):
	ask = models.CharField(max_length=255)
	response = models.TextField()
	name_client = models.CharField(max_length=255)
	details_client = models.TextField()