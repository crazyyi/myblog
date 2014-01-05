from django.db import models

# Create your models here.
class Account(models.Model):
	"""docstring for Account"""
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=30)

	def __unicode__(self):
		return self.username

class Blog(models.Model):
	"""docstring for Blog"""
	account = models.ForeignKey(Account)
	title = models.CharField(max_length=200)
	body = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title

		
		