import itertools

x = input()

y = "".join(i[0] for i in itertools.groupby(x))

print(y)
