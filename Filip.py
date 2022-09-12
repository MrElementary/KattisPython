x, y = map(str, input().split())

def reverse(number):
    reverse_string = number[::-1]
    reverse_num = int(reverse_string)
    return reverse_num

x = reverse(x)
y = reverse(y)
if x > y:
    print(x)
else:
    print(y)
