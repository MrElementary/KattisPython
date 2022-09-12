import sys

x = sys.stdin.read().splitlines()

numbers = [int(i) for i in x]

data_used = sum(numbers[2:])
data_left = ((numbers[1] * numbers[0]) - data_used) + numbers[0]

print(data_left)
