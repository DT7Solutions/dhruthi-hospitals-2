from django.contrib import admin
from .models import HomeSlider

# Register your models here.
class AdminBanner(admin.ModelAdmin):
    list_display=('Id','Title','Image')

admin.site.register(HomeSlider,AdminBanner)