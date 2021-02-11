'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 16:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 13:50:38  
 @Title : Flip coin problem
'''
import random
while True:
    try:
        number=int(input("enter the number: "))
        head=0
        tail=0
        counter=number
        while counter!=0:
            if(random.randint(0, 1)==0):
                head+=1
            counter-=1
        head_count=(head/number)*100
        break
    except:
        print("enter number only try again")
print("Head: ", head_count)
print("Tail: ", 100-head_count)
