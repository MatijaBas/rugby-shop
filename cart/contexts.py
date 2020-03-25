from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the users content that's added to the cart
    will be available when rendering any page within the web app
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}