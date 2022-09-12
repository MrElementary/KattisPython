x = input()
data = list(map(int,input().split()))

total_bases = 0
valid_hits = 0

for i in data:
    if i != -1:
        valid_hits += 1
        total_bases += i

print(float(total_bases/valid_hits))        
