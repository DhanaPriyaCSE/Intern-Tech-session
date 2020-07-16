class time_conversion:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def convert_to_minute(self):
        self.hours=self.hours*60
        self.minutes=self.minutes+self.hours
        return self.minutes

    def add(self,time1,time2):
        return (self.time1+self.time2)
    def sub(self,time1,time2):
        return abs(self.time1-self.time2)
    
    def Convert_time(self,time):
        self.hours = self.time // 60
        self.time %= 60
        self.minutes = self.time 
        print("%d Hours and %d miniutes" % (self.hours, self.minutes))



time1=input("Enter the time").split()
time2=input("Enter the time").split()

time1_min=time_conversion(int(time1[0]),int(time1[3]))
time2_min=time_conversion(int(time2[0]),int(time2[3]))

add=time1_min.add(time2_min)
time1_min.Convert_time(add)


sub=time1_min.sub(time2_min)
time1_min.Convert_time(sub)

print('The Total time in miutes:',time1_min.add)
