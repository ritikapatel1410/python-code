'''
 @Author: Ritika Patidar
 @Date: 2021-02-12 10:51:40
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-12 10:051:40 
 @Title : Gambler problem
'''
import random
while True:
    try:
        win=0
        loss=0
        experiment=0
        stake=int(input("enter the stake value: "))
        goal=int(input("enter the goal: "))
        number_of_times=int(input("enter the value of number_of_times run experiment: "))
        while(stake>0 and stake<goal and number_of_times>experiment):
            bet=random.randint(0,1)
            if(bet==1):
                win+=1
                stake+=1
            else:
                stake-=1
            experiment+=1
        win_percentage=(win/experiment)*100
        print("number of wins: ", win)
        print("number of win percentage: ", win_percentage)
        print("number of loss percentage: ", 100-win_percentage)
        break
    except:
        print("enter number only")


