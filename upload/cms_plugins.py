from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from upload.models import CantorPlugin as CantorPluginModel


class CantorPlugin(CMSPluginBase):
	model = CantorPluginModel # Model where data about this plugin is saved
	name = _("Cantor Plugin") # Name of the plugin
	render_template = "upload/plugin.html" # template to render the plugin with
	text_enabled = True

	def render(self, context, instance, placeholder):
		context.update({'instance':instance})
		return context

plugin_pool.register_plugin(CantorPlugin) # register the plugin