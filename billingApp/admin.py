from django.contrib import admin
from .models import Hotel

admin.site.site_header = "Hotel Description"
admin.site.site_title = "Nepalese"

# Register your models here.

admin.site.register(Hotel)
