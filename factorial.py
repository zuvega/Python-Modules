from math import factorial

num = int(input("Enter a number to calculate its factorial: "))

fact = 1
for i in range(1, num + 1):
    fact *= i

    
print(f"Factorial of {num} using loop: {fact}")

math_fact = factorial(num)

print(f"Factorial of {num} using math module: {math_fact}")
