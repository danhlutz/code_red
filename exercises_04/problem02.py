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


def find_end_balance(balance, payment, annual_rate):
    for month in range(12):
        balance -= find_principal_paid(
            balance, payment, annual_rate
        )
    return balance


def find_payoff_bisection(starting_balance, annual_rate, verbose=False):
    low = starting_balance / 12.0
    high = starting_balance
    i = 0
    while True:
        if verbose: print ("high " + str(high) + " low " + str(low))
        guess = (high + low) / 2.0
        if verbose: print ("guess " +  str(guess))
        end_balance = find_end_balance(starting_balance, guess, annual_rate)
        if verbose: print ("end_balance " + str(end_balance))
        if end_balance > -1.00 and end_balance <  0.00:
            return guess
        elif end_balance > 0.00:
            low = guess
        else:
            high = guess


if __name__ == '__main__':
    balance = float(input('What is your starting balance? '))
    annual_rate = float(input('And what is your rate? '))
    print ("Monthly payments to pay off in 1 year: " + str(
        find_payoff_bisection(balance, annual_rate
        )
    ))
