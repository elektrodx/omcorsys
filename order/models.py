from django.db import models
from customer.models import Customer

class State(models.Model):
	state = models.CharField(max_length=20)
	def __unicode__(self):
		return self.state

class Invoice(models.Model):
	guia = models.CharField(max_length=10)
	date = models.DateField()
	date_arrive = models.DateField(blank=True)
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	amount_tax = models.DecimalField(max_digits=7, decimal_places=2)
	weight = models.DecimalField(max_digits=7, decimal_places=2)
	
class Order(models.Model):
	customer = models.ForeignKey(Customer)
	date = models.DateField(auto_now_add=True)
	date_due = models.DateField(blank=True , null=True)
	date_delivered = models.DateField(blank=True, null=True)
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	weight = models.DecimalField(max_digits=7, decimal_places=2)
	state = models.ForeignKey(State)
	def __unicode__(self):
		return str(self.id)	

class Items(models.Model):
	order = models.ForeignKey(Order)
	qty = models.IntegerField()
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	source = models.URLField(max_length=200)
	code = models.CharField(max_length=50)
	date = models.DateField(blank=True, null=True)
	invoice = models.ForeignKey(Invoice, blank=True, null=True)
	weight = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
	tracking = models.URLField(max_length=500, blank=True)
	note = models.TextField(blank=True, null=True)





