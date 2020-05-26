from django.contrib import admin
from .models import *
from django.db import models

# Register your models here.
admin.site.register(VendorTable)
admin.site.register(CustomerTable)
admin.site.register(AuthTable)
admin.site.register(MenuTable)
admin.site.register(OrderTable)
admin.site.register(OrderStatus)
admin.site.register(NotificationsTable)
admin.site.register(MessageStatus)
