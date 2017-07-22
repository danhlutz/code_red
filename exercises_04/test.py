import unittest

from problem01 import (
    find_minimum_payment, find_interest_paid, find_principal_paid,
    find_balance_in_twelve,
)
from problem02 import find_payoff, find_payoff_bisection


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


    def test_after_twelve_higher_minimum(self):
        balance_after_twelve = find_balance_in_twelve(4800.00, 0.20, 0.04)
        self.assertTrue(
            abs(3615.74 - balance_after_twelve) < 0.25
        )


class PayoffTest(unittest.TestCase):

    def test_find_payoff(self):
        payoff_amount, months = find_payoff(1200.00, 0.18)
        self.assertEqual(months, 11)
        self.assertEqual(120.00, payoff_amount)


    def test_find_payoff2(self):
        payoff_amount, months = find_payoff(32000.00, 0.2)
        self.assertEqual(months, 12)
        self.assertEqual(payoff_amount, 2970.00)


    def test_find_payoff_with_bisection(self):
        payoff_amount = find_payoff_bisection(320000.00, 0.2)
        self.assertTrue(
            abs(29643.05 - payoff_amount) < 1.00
        )


if __name__ == '__main__':
    unittest.main()
