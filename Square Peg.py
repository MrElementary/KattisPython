import math

x = input().split()

answer = int(x[1]) * (math.sqrt(2))

if answer > int(x[0]):
    print('fits')
else:
    print('nope')
print(answer)
