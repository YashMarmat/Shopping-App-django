from django.urls import path
from .views import userdisplay, homepage

urlpatterns = [
    path('', homepage),
    path('products/', userdisplay),
]