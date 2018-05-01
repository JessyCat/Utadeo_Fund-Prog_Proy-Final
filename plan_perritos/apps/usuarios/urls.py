from django.urls import re_path
from .views import homepage

urlpatterns = [
    re_path(r'^', homepage, name='home'),
]



