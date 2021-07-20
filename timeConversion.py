from timeString import timeFormat

class timeConversion:
    def __init__(self, timeFormat):
        self.timeFormat = timeFormat
        
    def convert(self):
        s_splitted = timeFormat.split(":")
        if(int(s_splitted[0])>12 or int(s_splitted[1])>59 or int(s_splitted[2][:-2])>59):
            print("Entered time format is wrong")
        else:
                
            if(timeFormat[-2:]=="PM"):
                if(s_splitted[0]!="12"):
                    s_splitted[0]=str(int(s_splitted[0])+12)
            else:
                if(s_splitted[0]=="12"):
                    s_splitted[0]="00"
            time = ":".join(s_splitted)
            time=str(time[:-2])
            print(time)

tc = timeConversion(timeFormat)
tc.convert()