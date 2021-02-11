'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 17:40:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 15:07:40 
 @Title : Create 2D array Problem
'''
while True:    
    try:
        n=int(input("enter the number of row: "))
        m=int(input("enter the number of coloumns: "))
        array=[ [input("enter the value: ") for i in range(m)] for j in range(n)]
        print("2D array:", array)
        break
    except:
        print("enter only number")

