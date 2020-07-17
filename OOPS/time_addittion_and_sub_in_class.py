class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def convert_hours_to_minutes(self):
        self.minutes=self.minutes+(self.hours*60)
        return self.minutes

def adding_minutes(time1,time2):
    added_time=time1+time2
    #convert_min_hours(added_time)
    return added_time

def difference_minutes(time1,time2):
    diff_time=time1-time2
    #convert_min_hours(diff_time)
    return diff_time
def convert_min_and_hours(time):
    hours = time // 60
    time %= 60
    minutes = time 
    print("%d Hours and %d miniutes" % (hours,minutes))

time_value1=input("Enter the time and miutes").split()
time_value2=input("Enter the time and miutes").split()

time1=Time(int(time_value1[0]),int(time_value1[3]))
time2=Time(int(time_value2[0]),int(time_value2[3]))

calculate_min_time1=time1.convert_hours_to_minutes()
calculate_min_time2=time2.convert_hours_to_minutes()

add=adding_minutes(calculate_min_time1,calculate_min_time2)
diff=difference_minutes(calculate_min_time1,calculate_min_time2)

convert_min_and_hours(add)
convert_min_and_hours(diff)

print("Total Minutes",add)



##output:
'''

Enter the time and miutes5 hrs and 50 minutes
Enter the time and miutes2 hrs and 15 minutes
8 Hours and 5 miniutes
3 Hours and 35 miniutes
Total Minutes 485


'''

