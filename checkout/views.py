from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, NewOrderForm
from .models import OrderItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """
    A view to ensure that payment information is being handled
    by stripe correctly, so that the user will be able to purchase
    items. The view renders the html page
    and pass in the forms and contents of the cart.
    """
    if request.method == "POST":
        order_form = NewOrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        # # if the order form and the payment form is valid,
        # filled out correctly, then the order form will be saved as order.

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()

            # get the information from the cart from the current session,
            #  about what is being purchased.
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_item = OrderItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_item.save()

            # a try except that will create a customer charge, using Stripe's in-built API.
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )

            # If the card is being declined.
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            # if the customer have paid, request the cart from the current session.
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))

            # if the user have not paid.
            else:
                messages.error(
                    request, "We were unable to take your payment at this time")

        # if any payment form errors occurs.
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment from this card")

    # return a payment form and an order form as blank.
    else:
        payment_form = MakePaymentForm()
        order_form = NewOrderForm()

    # return the checkout html with an order form, a payment form, and a publishable key for Stripe,
    # available on the HTML page when the user clicks on checkout.
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
