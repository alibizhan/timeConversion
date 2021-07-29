from timeString import timeFormat

class timeConversion:
    def __init__(self, timeFormat):
        self.timeFormat = timeFormat
        
    def convert(self):
        timeSplitted = timeFormat.split(":")
        hour = int(timeSplitted[0])
        minute = int(timeSplitted[1])
        second = int(timeSplitted[2][:-2])


            

        if( (hour>12 or hour<1) or (minute>59 or minute<0) or (second>59 or second<0) ):
            print("Entered time format is wrong")
        else:
            timeSplitted[1] = timeSplitted[1].lstrip("0")
            timeSplitted[2] = timeSplitted[2].lstrip("0")
            if(minute == 0):
                timeSplitted[1] = "00"+timeSplitted[1]
            if(second == 0):
                timeSplitted[2] = "00"+timeSplitted[2]
            if(minute<10 and minute != 0):
                timeSplitted[1] = "0"+timeSplitted[1]
            if(second<10 and second !=0):
                timeSplitted[2] = "0"+timeSplitted[2]

            if(timeFormat[-2:]=="PM"):
                if(timeSplitted[0]!= "12"):
                    timeSplitted[0] = str(int(timeSplitted[0])+12)
            else:
                if(timeSplitted[0] == "12"):
                    timeSplitted[0] = "00"
            
            time = ":".join(timeSplitted)
            time=str(time[:-2])
            print(time)

tc = timeConversion(timeFormat)
tc.convert()