from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=("id", "title", "is_published", "price", "list_date", "realtor")
    list_display_links= ("id", "title")
    list_filter = ("realtor",)
    list_editable = ("is_published",)
    search_fields = ('title', 'zipcode', 'description', 'city', 'address', 'state')
    list_per_page = 25
# Register your models here.
admin.site.register(Listing, ListingAdmin)