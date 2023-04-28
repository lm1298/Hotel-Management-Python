import unittest

from src.Payment import Payment
from src.guest import Guest


class TestPayment(unittest.TestCase):
    """
    Unit tests for the Payment class.
    """

    def setUp(self):
        """
        Sets up a new Payment object and a corresponding Guest object for testing.
        """
        self.guest = Guest("John Doe", "john.doe@example.com", "555-555-1234")
        self.payment = Payment(self.guest, 100.0)

    def test_make_payment(self):
        """
        Tests that make_payment() sets the is_paid flag to True.
        """
        self.payment.make_payment()
        self.assertTrue(self.payment.is_paid)

    def test_get_payment_details(self):
        """
        Tests that get_payment_details() returns a string with the guest name, payment amount, and payment status.
        """
        expected = "Guest name: John Doe\nPayment amount: 100.0\nPayment status: not paid"
        self.assertEqual(self.payment.get_payment_details(), expected)


if __name__ == '__main__':
    unittest.main()
