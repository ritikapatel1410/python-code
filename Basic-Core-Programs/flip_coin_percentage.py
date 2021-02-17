'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 16:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-13 10:22:38  
 @Title : Flip coin problem
'''
import random
def flip_coin_fun():
    try:
        number=int(input("enter the number of experiment: "))
        head=0
        tail=0
        counter=number
        if(number>0):
            while counter!=0:
                if(random.randint(0, 1)==0):
                    head+=1
                counter-=1
            head_count=(head/number)*100
            print("Head Percentage: ", head_count)
            print("Tail Percentage: ", 100-head_count)    
        else:
            print("enter positive integer number only try again")
            flip_coin_fun()
    except Exception:
        print("enter integer number only try again")
        flip_coin_fun()
flip_coin_fun()

