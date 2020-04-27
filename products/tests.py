from django.test import TestCase
from .models import Product

# Create your tests here.


class ProductTests(TestCase):

    """
    Test that I'll run against the
    Product model
    """

    # Test the name of the product.
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
