from src.Payment import process_payment_paid, process_payment_unpaid, Payment, Guest
import unittest


class TestPayment(unittest.TestCase):

    def test_process_payment_unpaid(self):
        actual_output = process_payment_unpaid("John Smith", 100)
        expected_output = "Guest: John Smith, Amount: $100, Status: Unpaid"
        self.assertEqual(actual_output, expected_output)

    def test_process_payment_paid(self):
        actual_output = process_payment_paid("Dan Niles", 350)
        expected_output = "Guest: Dan Niles, Amount: $350, Status: Paid"
        self.assertEqual(actual_output, expected_output)

    def test_set_paid(self):
        guest = Guest("Dan Niles")
        payment = Payment(guest, 350)
        payment.make_payment()
        self.assertTrue(payment.is_paid)

    def test_set_unpaid(self):
        guest = Guest("Dan Niles")
        payment = Payment(guest, 350)
        payment.is_paid = False
        self.assertFalse(payment.is_paid)

if __name__ == '__main__':
    unittest.main()