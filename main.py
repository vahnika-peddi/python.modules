import random

num = random.randint(1,100)
print("Generated number:", num)

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if num < 50:
    print("Small number")
else:
    print("Big number")