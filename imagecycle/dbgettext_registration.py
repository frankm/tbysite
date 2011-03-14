from dbgettext.registry import registry, Options
from models import ImageCycle

class ImageCycleOptions(Options):
    attributes = ('url')
    parent = 'page'

registry.register(ImageCycle, ImageCycleOptions)
