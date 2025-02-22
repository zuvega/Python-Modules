import math

def calculate_pi_approximation(terms):
    pi_approximation = 0
    for i in range(terms):
        pi_approximation += ((-1) ** i) / (2 * i + 1)
    pi_approximation *= 4
    return pi_approximation

pi_approximation = calculate_pi_approximation(1000000)
print("Approximation of Pi:", pi_approximation)

print("Value of math.pi:", math.pi)
