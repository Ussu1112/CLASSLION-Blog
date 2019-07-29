from django.contrib import admin
from .models import Blog, SellItem ,BuyItem
admin.site.register(Blog)
admin.site.register(BuyItem)
admin.site.register(SellItem)
