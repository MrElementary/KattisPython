import sys

x = sys.stdin.read().splitlines()

y = x[1:]

total = 0
for i in y:
    power_value = int(i[-1])
    base_value = int(i[:-1])
    multi_answer = pow(base_value, power_value)
    total = total + multi_answer

print(total)
    
