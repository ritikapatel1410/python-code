'''
 @Author: Ritika Patidar
 @Date: 2021-02-11 18:10:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 18:10:30 
 @Title : Quardratic Equation Problem
'''
import cmath
while True:
    try:
        a=float(input("enter coefficients(a) value: "))
        b=float(input("enter coefficients(b) value: "))
        c=float(input("enter coefficients(c) value: "))
        delta = (b**2) - (4*a*c)
        root1 = (-b-cmath.sqrt(delta))/(2*a)
        root2 = (-b+cmath.sqrt(delta))/(2*a)
        print('The roots are {0} and {1}'.format(root1,root2))
        break
    except:
        print("enter number only try again!!")

