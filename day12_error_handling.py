balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount > balance:
        print("Insufficient balance")

    else:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)

finally:
    print("Transaction completed")