from django.contrib import admin

# Register your models here.

from kurs.models import Blog

# Register your models here.

@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_of_creation')
    readonly_fields = ('date_of_creation', 'view_counter')