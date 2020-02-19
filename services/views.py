from django.shortcuts import render
from .models import Service

# Create your views here.
"""This view gets all the services and uses the Service model which is then shown on the services.html page."""


def show_all_services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})
