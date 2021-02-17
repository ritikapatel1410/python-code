'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 17:40:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-13 10:37:40 
 @Title : Create 2D array Problem
'''
while True:    
    try:
        row=int(input("enter the number of row: "))
        column=int(input("enter the number of coloumns: "))
        array=[ [input("enter the value: ") for c in range(column)] for r in range(row)]
        print("2D array:", array)
        break
    except ValueError:
        print("enter int number only try again!!")

