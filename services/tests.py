from django.test import TestCase
from .models import Service
# Create your tests here.


class ServiceTesting(TestCase):
    """
    I define a test case here and check to see if it passes the desired
    output to the user in this case for services that are provided.
    """
    def test_str(self):
        test_name = Service(name='Service demo')
        self.assertEqual(str(test_name), 'Service demo')
