from django.contrib import admin
from vinyldestination.models import Artist, Record, Shop, Stock, Review, Page, UserProfile


# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', 'insta')


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'views', 'likes', 'slug', 'a_id', 'genre')


class ShopAdmin(admin.ModelAdmin):
    list_display = ('s_id', 'name', 'description', 'views', 'likes', 'slug')


class StockAdmin(admin.ModelAdmin):
    list_display = ('shop', 'stock_item')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('record', 'author', 'title', 'review', 'rating')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website', 'picture')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
