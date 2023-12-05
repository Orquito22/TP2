from django.contrib import admin

# Register your models here.

from .models import Resenia

@admin.register(Resenia)
class ReseniaAdmin(admin.ModelAdmin):
    ...