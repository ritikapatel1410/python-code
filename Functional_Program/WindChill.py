'''
 @Author: Ritika Patidar
 @Date: 2021-02-11 18:10:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-13 11:10:30 
 @Title : Wind chill Problem
'''
def wind_chill():
    try:
        t=float(input("enter temperature less 50 in Fahrenheit: "))
        v=float(input("enter speed greater then equal to 3 and less then or equal to 120 in miles per hour: "))
        if(t<=50.0 and (v<=120.0 and v>=3)):
            w=35.74+0.6215*t+pow((0.4275*t-35.75)*v,0.16)
            print("wind chill: ", w)
        else:
            wind_chill()
    except ValueError:
        print("enter number only try again!!")
        wind_chill()
wind_chill()

