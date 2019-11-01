from django import template
register = template.Library()

from ..models import DesignAssets

@register.simple_tag
def get_resource_icon(resource):
    design_assets = DesignAssets.objects.first()
    if hasattr(resource, 'video'):
        return design_assets.video_img
    if hasattr(resource, 'website'):
        return design_assets.website_img
    # default
    return design_assets.document_img
