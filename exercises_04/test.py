import unittest

from problem01 import (
    find_minimum_payment, find_interest_paid, find_principal_paid,
    find_balance_in_twelve,
)

class InterestTest(unittest.TestCase):

    def test_monthly_minimum(self):
        min_payment = find_minimum_payment(5000.00, 0.02)
        self.assertEqual(min_payment, 100.00)


    def test_interest_paid(self):
        interest_paid = find_interest_paid(5000.00, 0.18)
        self.assertEqual(75.00, interest_paid)

    def test_principal_paid(self):
        principal_paid = find_principal_paid(5000.00, 100.00, 0.18)
        self.assertEqual(25.00, principal_paid)


    def test_after_twelve(self):
        balance_after_twelve = find_balance_in_twelve(4800.00, 0.20, 0.02)
        self.assertTrue(
            abs(4611.46 - balance_after_twelve) < 0.05
        )


if __name__ == '__main__':
    unittest.main()