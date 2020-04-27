from django.contrib import messages
from django.shortcuts import render
from .models import Product
from products.mails import send_subscribe_mail

# Create your views here.

"""
This view return all products in the database
and will be viewed on the products.html page.
"""


def all_products(request):
    if request.method == "POST":
        send_subscribe_mail(request.POST)
        messages.success(
            request, "Thank you for subscribtion. Check your mailbox."
        )
    products = Product.objects.all()
    name = request.GET.get("q")
    if name:
        products = products.filter(name__icontains=name)

    products = products.order_by("name")
    return render(request, "products.html", {"products": products})


def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product-details.html", {"product": product})
