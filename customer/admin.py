from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('user_customer', 'ci','fone', 'fone2', 'address')

admin.site.register(Customer, CustomerAdmin)	
