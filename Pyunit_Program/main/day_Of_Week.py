'''
 @Author: Ritika Patidar
 @Date: 2021-02-16 14:45:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-16 14:45:10  
 @Title : Day of Week problem
'''

def dayOfWeek(month,day,year):
    new_year = int((year - (14 - month)) / 12)
    leap_year = int(new_year + (new_year/4) - (new_year/100) + (new_year/400)) 
    new_month = month + 12 * ((14 - month) / 12) - 2
    new_day = (day + leap_year + 31*(new_month) / 12) % 7   
    return new_day    

def main():  
    month=int(input("enter the month: "))
    day=int(input("enter the day: "))
    year=int(input("enter theyear: "))
    week_day={0:"sunday", 1:"monday", 2:"tuesday", 3:"wendesday", 4:"thursday", 5:"friday", 6:"saturady"}
    return week_day[dayOfWeek(month,day,year)]
if __name__ == '__main__':
    print(main())
