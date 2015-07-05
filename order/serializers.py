from rest_framework import serializers
from .models import *
from customer.models import Customer

class OrderSerializer(serializers.ModelSerializer):
	customer = serializers.CharField(read_only=True)
	state = serializers.CharField(read_only=True)
	class Meta:
		model = Order
		fields = ('id', 'customer', 'date', 'date_due', 'amount', 'weight', 'state' )

class ItemsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Items