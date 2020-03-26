from django.shortcuts import render
from products.models import Product

# Create your views here.


def do_search(request):
    """
    Search view, Whatever is typed into the form
    will be used to filter the products
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
