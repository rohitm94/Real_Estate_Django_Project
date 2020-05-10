from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'city',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ['price', 'is_published']
    list_filter = ('realtor',)
    search_fields = ('price', 'description', 'title',
                     'address', 'city', 'state', 'zipcode')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
