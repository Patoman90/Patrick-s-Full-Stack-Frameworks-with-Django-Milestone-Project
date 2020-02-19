from django.shortcuts import render
from .models import Product

# Create your views here.
"""This view gets all the products and uses the Product model which is then shown on the products.html page."""


def show_all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
