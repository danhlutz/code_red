from problem01 import find_principal_paid

def find_payoff(starting_balance, annual_rate, verbose=False):
    payment = 10.00
    while True:
        if verbose: print ("checking payment: ", str(payment))
        monthly_balance = starting_balance
        month = 0
        while month < 12:
            monthly_balance -= find_principal_paid(
                monthly_balance, payment, annual_rate
            )
            month += 1
            if monthly_balance < 0.00:
                if verbose: print ("Got it: ", str(monthly_balance), str(month))
                return payment, month
        payment += 10.00
