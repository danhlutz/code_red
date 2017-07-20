def find_minimum_payment(balance, min_monthly_rate):
    return balance * min_monthly_rate


def find_interest_paid(balance, annual_rate):
    return balance * (annual_rate / 12.0)


def find_principal_paid(balance, payment, annual_rate):
    return payment - find_interest_paid(balance, annual_rate)


def find_balance_in_twelve(
    balance, annual_rate, minimum_monthly_rate, verbose=False
):
    for month in range(12):
        if verbose: print ("Month: " + str(month))
        minimum_payment = find_minimum_payment(balance, minimum_monthly_rate)
        if verbose: print ("Minimum monthly payment: ", str(minimum_payment))
        principal_paid = find_principal_paid(
            balance, minimum_payment, annual_rate
        )
        if verbose: print ("Principal paid: $" + str(principal_paid))
        balance -= principal_paid
        if verbose: print ("Remaining balance: $" + str(balance))
    return balance


if __name__ == '__main__':
    balance = float(input('What is your current balance? '))
    rate = float(input("What is your interest rate? "))
    min_payment_rate = float(input("And what is your minimum payment rate? "))
    find_balance_in_twelve(balance, rate, min_payment_rate, verbose=True)
