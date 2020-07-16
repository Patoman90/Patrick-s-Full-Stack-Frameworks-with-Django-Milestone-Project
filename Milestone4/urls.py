"""Milestone4 URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin
from home import urls as urls_home
from accounts import urls as urls_accounts
from products import urls as urls_products
from reviews import urls as urls_reviews
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from home.views import index
from products.views import show_all_products
from reviews.views import show_all_reviews
from cart.views import view_cart
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^$', show_all_products, name='index1'),
    url(r'^$', show_all_reviews, name='index3'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^reviews/', include(urls_reviews)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
