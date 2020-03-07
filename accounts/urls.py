from django.conf.urls import url, include
from accounts import urls_reset
from accounts.views import index, register, logout, login, quote, email


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^quote/$', quote, name='quote'),
    url(r'^email/$', email, name='email'),
    url(r'^password-reset/', include(urls_reset)),
]
