from django.test import TestCase
from .models import Review

# Create your tests here.


class ReviewTests(TestCase):

    def test_str(self):
        test_title = Review(title='Good jersey')
        self.assertEqual(str(test_title), 'Good jersey')
