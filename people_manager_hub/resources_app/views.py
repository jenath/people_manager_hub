from django.http import HttpResponse
from django.shortcuts import render

from .models import Homepage, ResourcesPage, DesignAssets, GlobalSettings

# Create your views here.

def index(request):
    homepage = Homepage.objects.all().first()
    resource_pages = ResourcesPage.objects.all()
    design_assets = DesignAssets.objects.all().first()
    contact_info = GlobalSettings.objects.all().first()
    context = {
        'homepage': homepage,
        'resource_pages': resource_pages,
        'design_assets': design_assets,
        'contact_info' : contact_info,
        }
    return render(request, 'resources_app/index.html', context)

def section(request, section_id):
    homepage = Homepage.objects.all().first()
    resource_pages = ResourcesPage.objects.all()
    design_assets = DesignAssets.objects.all().first()
    contact_info = GlobalSettings.objects.all().first()

    try:
        resource_page = ResourcesPage.objects.get(id=section_id)
    except ResourcesPage.DoesNotExist:
        return render(request, 'resources_app/index.html', {
            'homepage': homepage,
            'resource_pages': resource_pages,
            'design_assets': design_assets,
            'contact_info' : contact_info,
        })


    design_assets = DesignAssets.objects.all().first()
    resource_pages = ResourcesPage.objects.all()
    contact_info = GlobalSettings.objects.all().first()
    context = {
        'resource_page': resource_page,
        'design_assets': design_assets,
        'resource_pages': resource_pages,
        'contact_info' : contact_info,
    }
    return render(request, 'resources_app/section.html', context)
