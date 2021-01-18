from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import userLogin,UserInfro

admin.site.register(userLogin)
admin.site.register(UserInfro)