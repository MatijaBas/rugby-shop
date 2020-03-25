from django.shortcuts import render
from .models import Product

# Create your views here.

"""
This view return all products in the database
and will be viewed on the products.html page.
"""


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
