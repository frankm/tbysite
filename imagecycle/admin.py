from imagecycle.models import ImageCycle, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class ImageCycleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Rotating Image Set', 	{'fields': ['setname']}),
		('Background Information', {'fields': ['background_color', 'background_image', 'repeat' ], 'classes': ['collapse']}),
		]
	inlines = [ChoiceInline]
	list_display = ('setname', 'background_color', 'background_image_name', 'repeat')

admin.site.register(ImageCycle, ImageCycleAdmin)