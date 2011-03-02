from upload.models import Cantor
from django.contrib import admin


class CantorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Files',               {'fields': ['document', 'audio']}),
        ('Comments or Instructions', {'fields': ['notes'], 'classes': ['collapse']}),
    ]
    list_display = ('document_name', 'audio_name', 'notes')
    list_filter = ['document']
    search_fields = ['audio', 'document', 'notes']


admin.site.register(Cantor, CantorAdmin)