from django.contrib import admin
from .models import ShopItem, Offer

# below i am creating seperate fields in webpage for each item
# Note: admin.site.register takes up only two argumnets, so for extra classes you need mention
# the register code again (as shown below)
# Note: list_display is a keyword
class DisplayItems(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')   # list_display is a keyword

class DisplayOffer(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Offer, DisplayOffer)
admin.site.register(ShopItem, DisplayItems)