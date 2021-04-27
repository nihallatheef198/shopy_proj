from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Products)
admin.site.register(models.review)
admin.site.register(models.Order)
admin.site.register(models.order_item)
admin.site.register(models.shipping_address)
