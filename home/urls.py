from django.conf.urls import url, include
from .views import index

'''Url for homepage'''
urlpatterns = [
    url(r'^$', index, name='home'),
]
