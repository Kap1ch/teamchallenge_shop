from django.contrib import admin

from .models import Catalog, SubCategory

# Register your models here.

admin.site.register(Catalog)
admin.site.register(SubCategory)