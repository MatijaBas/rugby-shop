from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    """
    Model to store order information, customer, shipping address, date
    and return a summary of the users order with the id, date and name.
    """

    user = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=54, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=42, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=42, blank=False)
    street_address1 = models.CharField(max_length=42, blank=False)
    street_address2 = models.CharField(max_length=42, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderItem(models.Model):
    """
    Model to store the order items, which product is being purchased and the quantity
    that was entered by the user.
    It returns the quantity of bought products, the name and price of the product.
    """

    order = models.ForeignKey(
        Order, null=False, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)
