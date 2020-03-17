from django.contrib import admin
from vinyldestination.models import Artist, Album, UserProfile


# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album)
admin.site.register(UserProfile)
	
	

