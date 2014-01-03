from django.db import models

# Create your models here.
class Account(models.Model):
	"""docstring for Account"""
	username = models.CharField(max_length=100)
	password = 
		