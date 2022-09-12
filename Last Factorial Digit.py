import math

test_cases = int(input())

for i in range(test_cases):
    factor = int(input())
    factor_digit = math.factorial(factor) % 10
    print(factor_digit)
