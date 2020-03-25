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

    # def test_list_products(self):
    #     test_name = Product(
    #         name='A product', description='test', price='10', quantity='10')
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
