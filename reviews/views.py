from django.shortcuts import render
from django.contrib import messages, auth
from products.models import Product
from services.models import Service
from django.contrib.auth.decorators import login_required
from .models import Reviews


"""This view gets all the customer reviews and uses the reviews model which is then shown on the reviews.html page."""


def show_all_reviews(request):
    reviews = Reviews.objects.all()
    products = Product.objects.all()
    services = Service.objects.all()
    return render(request, "reviews.html", {"reviews": reviews, "products": products, "services": services})
