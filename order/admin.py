from django.contrib import admin
from order.models import *

class StateAdmin(admin.ModelAdmin):
	list_display = ('state',)

class OrderAdmin(admin.ModelAdmin):
	list_display = ('customer', 'date','date_due', 'date_delivered', 'amount', 'weight', 'state')

class InvoiceAdmin(admin.ModelAdmin):
	list_display = ('guia', 'date', 'date_arrive', 'amount', 'amount_tax', 'weight')

class ItemsAdmin(admin.ModelAdmin):
	list_display = ('order', 'qty', 'description', 'price', 'source', 'code', 'date', 'invoice', 'weight', 'tracking', 'note')

admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(State, StateAdmin)