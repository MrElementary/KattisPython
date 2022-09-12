start, end, stops = map(int,input().split())
foot_travel_times = list(map(int,input().split()))
bus_travel_times = list(map(int,input().split()))
bus_arrival_times = list(map(int,input().split()))

travel_time = start
        

for i in range(stops):
    foot_travel = foot_travel_times[i]
    travel_time += foot_travel

    late_time = travel_time % bus_arrival_times[i]
    waitingtime = 0 if late_time == 0 else bus_arrival_times[i] - late_time
    travel_time += waitingtime

    bustravel = bus_travel_times[i]
    travel_time += bustravel

travel_time += foot_travel_times[-1]

if travel_time <= end:
    print("yes")
else:
    print("no")
