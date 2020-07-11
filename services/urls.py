from django.conf.urls import url, include
from .views import show_all_services
from accounts.urls import quote, email


urlpatterns = [
    url(r'^$', show_all_services, name='services'),
    url(r'^quote/$', quote, name='quote'),
    url(r'^email/$', email, name='email')
]
