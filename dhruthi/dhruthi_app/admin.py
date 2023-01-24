from django.contrib import admin
from .models import HomeSlider,Popup

# Register your models here.
class AdminBanner(admin.ModelAdmin):
    list_display=('Id','Title','Image')

class AdminPopup(admin.ModelAdmin):
    list_display=('Id','Title','Image')

admin.site.register(HomeSlider,AdminBanner)
admin.site.register(Popup,AdminPopup)  