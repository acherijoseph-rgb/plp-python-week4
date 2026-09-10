# ATM Menu
# A simple ATM program using nested decisions.

balance = 1000
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

if pin != correct_pin:
    print("Incorrect PIN")
else:
    amount = float(input("Enter amount to withdraw: "))

    # This decision is nested inside the correct PIN decision.
    if amount <= balance:
        balance = balance - amount
        print(f"Withdrawal successful. New balance: {balance:.2f}")
    else:
        print("Insufficient funds")
