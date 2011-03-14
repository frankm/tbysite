from upload.models import CantorSet, Cantor
from django.contrib import admin

class CantorInline(admin.TabularInline):
	model = Cantor
	extra = 3

class CantorSetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cantor Set',               {'fields': ['name']}),
    ]
    inlines = [CantorInline]
    list_display = ('name',)



admin.site.register(CantorSet, CantorSetAdmin)