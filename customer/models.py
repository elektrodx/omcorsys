from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user_customer = models.OneToOneField(User, primary_key=True)
	fone = models.CharField(max_length=10)
	fone2 = models.CharField(max_length=10, blank=True)
	address = models.CharField(max_length=100, blank=True)
	ci = models.CharField(max_length=10)
	def __unicode__(self):
		return self.user_customer.username

	

