from django.contrib import admin
from vinyldestination.models import Artist, Record, Shop, Review, Page, UserProfile


# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class RecordAdmin(admin.ModelAdmin):
	list_display = ('r_id', 'name', 'year', 'views', 'likes', 'slug')

class ShopAdmin(admin.ModelAdmin):
	list_display = ('s_id', 'name', 'description', 'views', 'likes', 'slug')

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('record', 'author', 'title', 'review', 'rating')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'website', 'picture')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)
	
	

