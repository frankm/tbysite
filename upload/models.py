from django.db import models
import os.path

class Cantor(models.Model):
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