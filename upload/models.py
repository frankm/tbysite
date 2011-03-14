from django.db import models
import os.path
from cms.models import CMSPlugin

class CantorPlugin(CMSPlugin):
	cantorset = models.ForeignKey('upload.CantorSet', related_name='plugins')
	
	def __unicode__(self):
		return self.cantorset.name
		
class CantorSet(models.Model):
	name = models.CharField(max_length=100  )
	
	def __unicode__(self):
		return self.name
		
class Cantor(models.Model):
	cantor = models.ForeignKey(CantorSet)
	document = models.FileField(upload_to='cantor')
	audio = models.FileField(upload_to='cantor')
	notes = models.TextField(max_length=255  )
	
	def document_name(self):
		return os.path.basename(self.document.name)
	
	def audio_name(self):
		return os.path.basename(self.audio.name)

	
	def __unicode__(self):
		return os.path.basename(self.document.name)
		
	class Meta:
		verbose_name_plural = "cantor"