from django.shortcuts import render
from .models import Product
from reviews.views import Reviews


"""This view gets all the products or services and uses the Product model
which is then shown on the products.html page or services.html page respectively."""


def show_all_products(request):
    products = Product.objects.filter(is_service=False)
    return render(request, "products.html", {"products": products})


def show_all_services(request):
    products = Product.objects.filter(is_service=True)
    return render(request, "services.html", {"services": services})


def get_reviews(request):
    reviews = Reviews.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
