knots = int(input())

data_set_one = set(map(str,input().split()))

data_set_two = set(map(str,input().split()))

missing = (data_set_one.difference(data_set_two))

print(list(missing)[0])
