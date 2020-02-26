from django.conf.urls import url, include
from .views import show_all_reviews


urlpatterns = [
    url(r'^$', show_all_reviews, name='reviews'),
]
