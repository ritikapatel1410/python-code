year=int(input("enter the year: "))
if(len(str(year))==4):
    if(((year%4 == 0) and (year%100 !=0)) or (year%400 == 0)):
        print(year, "is leap year")
    else:
        print(year, "is not a leap year")
else:
    print("invalid year")