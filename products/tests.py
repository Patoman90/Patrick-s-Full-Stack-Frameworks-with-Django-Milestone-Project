from django.test import TestCase
from .models import Product
# Create your tests here.


class TestingProduct(TestCase):
    """
    I define a test case here and check to see if it passes the desired
    output to the user
    """
    def test_str(self):
        test_name = Product(name='Product demo')
        self.assertEqual(str(test_name), 'Product demo')
