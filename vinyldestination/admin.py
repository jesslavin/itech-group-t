from django.contrib import admin
from vinyldestination.models import Artist, Page, UserProfile, Record


# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Record)
	

