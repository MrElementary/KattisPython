x = int(input())

for i in range(x):
    raw_data = input().split()
    numberofbeats = int(raw_data[0])
    numberofseconds = float(raw_data[1])
    time_difference = 60/numberofseconds
    BPM = 60*numberofbeats/numberofseconds
    abpm_lower = BPM - time_difference
    abpm_higher = BPM + time_difference
    print("{} {} {}".format(round(abpm_lower,4),round(BPM,4),round(abpm_higher,4)))
