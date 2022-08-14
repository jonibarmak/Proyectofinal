from django.contrib import admin
from info.models import about_us 

@admin.register(about_us)
class Nosotros_admin(admin.ModelAdmin):
    list_display=["name","description"]
