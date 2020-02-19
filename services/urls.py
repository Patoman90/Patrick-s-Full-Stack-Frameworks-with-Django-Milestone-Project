from django.conf.urls import url, include
from .views import show_all_services


urlpatterns = [
    url(r'^$', show_all_services, name='services'),
]
