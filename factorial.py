'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 16:40:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 14:07:38  
 @Title : Factorial number problem
'''
while True:
    try:
        num=int(input("enter the number: "))
        mult=1
        while(num>0):
            mult*=num
            num-=1
        print(mult)
        break
    except:
        print("enter number only try again")

