from django.contrib import admin
from shortener.models import URL

@admin.register(URL)
class UserAdminClass(admin.ModelAdmin):
    pass
