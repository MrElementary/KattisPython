data = list(map(int,input().split()))

dimensions = data[0]
h_cut = data[1]
v_cut = data[2]

h_remain = dimensions - h_cut
v_remain = dimensions - v_cut

biggest_h = 0
biggest_v = 0

if h_remain >= h_cut:
    biggest_h = h_remain
else:
    biggest_h = h_cut

if v_remain >= v_cut:
    biggest_v = v_remain
else:
    biggest_v = v_cut

size = biggest_h * biggest_v * 4
print(size)
