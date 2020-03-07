from django.conf.urls import url, include
from .views import show_all_products
from reviews import urls as urls_reviews
from accounts.urls import quote, email

urlpatterns = [
    url(r'^$', show_all_products, name='products'),
    url(r'^reviews/', include(urls_reviews)),
    url(r'^quote/$', quote, name='quote'),
    url(r'^email/$', email, name='email')
]
