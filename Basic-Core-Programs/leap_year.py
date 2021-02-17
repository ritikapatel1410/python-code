'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 16:40:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 13:30:39 
 @Title : Leap year problem
'''
while True:
    try:
        year=int(input("enter the year in yyyy format: "))
        if(len(str(year))==4):
            if(((year%4 == 0) and (year%100 !=0)) or (year%400 == 0)):
                print(year, "is leap year")
                break
            else:
                print(year, "is not a leap year")
                break
        else:
            print("invalid year")
    except ValueError:

        print("invalid format of year try again!!")
