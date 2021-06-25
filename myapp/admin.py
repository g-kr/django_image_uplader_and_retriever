from django.contrib import admin
from .models import Uimage

# Register your models here.
@admin.register(Uimage)
class Imageadmin(admin.ModelAdmin):
    list_display= ['id','image','date']
