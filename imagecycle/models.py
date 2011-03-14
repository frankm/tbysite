from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from os.path import basename


storage = 'imagecycle'

class ImageCyclePlugin(CMSPlugin):
    imagecycle = models.ForeignKey('imagecycle.ImageCycle', related_name='plugins')
    
    def __unicode__(self):
    	return self.imagecycle.setname

class ImageCycle(models.Model):
    X = "repeat-x"
    Y = "repeat-y"
    NEITHER = "no-repeat"
    REPEAT_CHOICES = ((X, _("horizontally")),
                     (Y, _("vertically")),
                      (NEITHER, _("no-repeat")),
                     )
    setname = models.CharField(max_length=200)
    background_color = models.CharField(_("background-color"), max_length=20, blank=True, null=True)
#     background_image = models.ImageField(_("background-image"), upload_to=CMSPlugin.get_media_path, blank=True, null=True, )
    background_image = models.ImageField(_("background-image"), upload_to=storage, blank=True, null=True, )
    repeat = models.CharField(_("repeat"), max_length=12, blank=True, null=True, choices=REPEAT_CHOICES, help_text=_("default: (------) repeat horizontally & vertically"))
    
    def background_image_name(self):
    	return basename(self.background_image.name)
	
    background_image_name.short_description = 'Background-image'

    def __unicode__(self):
    	return self.setname
	

    
class Choice(models.Model):
    image_set = models.ForeignKey(ImageCycle)
    image = models.ImageField(_("image"), upload_to=storage)
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True, help_text=_("if present image will be clickable"))
    url = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    
    def __unicode__(self):
    	return basename(self.image.name)
	