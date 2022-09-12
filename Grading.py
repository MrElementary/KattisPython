a,b,c,d,e = map(int,input().split())

test = int(input())

if test >= a:
    print("A")
if test < a and test >= b:
    print("B")
if test < b and test >= c:
    print("C")
if test < c and test >= d:
    print("D")
if test < d and test >= e:
    print("E")
if test < e:
    print("F")
