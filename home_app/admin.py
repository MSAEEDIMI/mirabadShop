from django.contrib import admin
from .models import SiteInfo ,Banner

# Register your models here.
# Register your models here.
admin.site.register(SiteInfo)

@admin.register(Banner)
class BanerAdmin(admin.ModelAdmin):
    list_display=["title",'position','order']
    list_filter=['position']
    list_editable=['position','order']