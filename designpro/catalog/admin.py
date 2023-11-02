from django.contrib import admin
from .models import MainConfig, AdvUser, Request

# Register your models here.
admin.site.register(MainConfig)
admin.site.register(AdvUser)
admin.site.register(Request)