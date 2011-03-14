from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from imagecycle.models import ImageCyclePlugin as ImageCyclePluginModel
from django.conf import settings

class ImageCyclePlugin(CMSPluginBase):
    model = ImageCyclePluginModel
    name = _("ImageCycle Plugin")
    render_template = "imagecycle/plugin.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context 
    
    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.CMS_MEDIA_URL + u"images/plugins/image.png"
 
plugin_pool.register_plugin(ImageCyclePlugin)
