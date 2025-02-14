from django.contrib import admin
from django.contrib.auth.models import User
from .models import OfficerProfile, Driver

# Register your models here.
admin.site.register(OfficerProfile)
admin.site.register(Driver)
