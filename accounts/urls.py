from django.conf.urls import url, include
from .views import index, register, profile, logout, login, quote
from . import urls_reset

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^quote/$', quote, name='quote'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]
