from django.contrib import admin

# Register your models here.

from .models import *

class ResourceModuleAdmin(admin.ModelAdmin):
    model = ResourceModule
    filter_horizontal = ('resources',)

admin.site.register(Video)
admin.site.register(Document)
admin.site.register(Website)
admin.site.register(ResourcesPage)
admin.site.register(Homepage)
admin.site.register(DesignAssets)
admin.site.register(GlobalSettings)
admin.site.register(ResourceModule, ResourceModuleAdmin)
