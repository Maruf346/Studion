from django.contrib import admin
from .models import *


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
