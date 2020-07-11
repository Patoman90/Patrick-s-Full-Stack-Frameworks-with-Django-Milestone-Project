from django.shortcuts import render


def index(request):
    """This view uses the render method to request the template index.html"""
    return render(request, "index.html")
