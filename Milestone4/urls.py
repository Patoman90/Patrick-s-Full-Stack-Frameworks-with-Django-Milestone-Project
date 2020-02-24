"""Milestone4 URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from accounts import urls as urls_accounts
from products import urls as urls_products
from services import urls as urls_services
from reviews import urls as urls_reviews
from cart import urls as urls_cart
from products.views import all_products
from services.views import all_services
from reviews.views import all_reviews
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', all_products, name='index1'),
    url(r'^$', all_services, name='index2'),
    url(r'^$', all_reviews, name='index3'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^services/', include(urls_services)),
    url(r'^reviews/', include(urls_reviews)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
