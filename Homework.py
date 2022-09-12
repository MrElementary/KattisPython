count = 0
for i in input().split(";"):
    if "-" in i:
        first, last = i.split("-")
        count += int(last) - int(first) + 1
    else:
        count += 1

print(count)
