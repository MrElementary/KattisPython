x = input().split()

hours_data = int(x[0])
minutes_data = int(x[1])

def time_lapse(minutes, hours):
    if minutes >= 45:
        print(hours, minutes-45)
    elif minutes < 45 and hours > 0:
        print(hours-1,minutes+15)
    elif minutes < 45 and hours == 0:
        print(23, minutes+15)
        
time_lapse(minutes_data,hours_data)
