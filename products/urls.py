from django.conf.urls import url, include
from .views import show_all_products


urlpatterns = [
    url(r'^$', show_all_products, name='products'),
]
