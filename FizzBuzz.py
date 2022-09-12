x, y, z = map(int, input().split())

for i in range(1,z+1):
    if i%x == 0 and i%y == 0:
        print("FizzBuzz")
    elif i%x == 0 and i%y != 0:
        print("Fizz")
    elif i%x != 0 and i%y == 0:
        print("Buzz")
    elif i%x != 0 and i%y != 0:
        print(i)
