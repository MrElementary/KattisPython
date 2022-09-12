from fractions import Fraction

rings = int(input())
ring_sizes = list(map(int,input().split()))
first_ring = ring_sizes[0]

for i in ring_sizes[1:]:
    turns = Fraction(first_ring,i)
    print("{}/{}".format(turns.numerator, turns.denominator))
