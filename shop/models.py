# username for this app yashapp1

from django.db import models


class ShopItem(models.Model):
    name      = models.CharField(max_length = 150)
    price     = models.FloatField() 
    stock     = models.IntegerField()
    image_url = models.CharField(max_length = 2083)   # a standard for maximum urls.

    '''    # this method is not that useful in terms of this project, so have a look in admin.py file
    def __str__(self):
        return self.name[:50], self.price
    
    output:  Apple, 1.99
    '''

class Offer(models.Model):
    code        = models.CharField(max_length = 10)
    description = models.CharField(max_length = 200)
    discount    = models.FloatField()