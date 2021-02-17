'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 14:30:25
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 13:40:38  
 @Title : Power of two problem
'''
def power_of_two():
    try:
        user_input=int(input("enter the number: "))
        count=0
        while(count<=user_input and count<31):
            print("2 ^ %d = %d " %(count,2**count))
            count+=1   
    except:
        print("enter number only") 
        power_of_two()
power_of_two()
