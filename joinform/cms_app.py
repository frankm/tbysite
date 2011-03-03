from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class JoinApphook(CMSApp):
    name = _("Join Form")
    urls = ["joinform.urls"]

apphook_pool.register(JoinApphook)
