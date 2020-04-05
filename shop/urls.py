from django.urls import path
from .views import userdisplay, homepage

urlpatterns = [
    path('', homepage, name = 'home'),
    path('products/', userdisplay, name = 'index'),
]
