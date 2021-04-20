from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Products)
admin.site.register(Productcat)
admin.site.register(Productsitems)
admin.site.register(Cart)


