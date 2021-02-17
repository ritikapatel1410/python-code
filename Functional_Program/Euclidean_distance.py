'''
 @Author: Ritika Patidar
 @Date: 2021-02-11 18:00:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 18:00:30 
 @Title : Euclidean distance problem
'''
import sys
import math
def Euclidean_distance():
    try:
        if(len(sys.argv)>1):
            print("Euclidean_distance" ,math.sqrt(int(sys.argv[1])**2+int(sys.argv[2])**2))
        else:
            print("you did not pass any value")
    except:
        print("enter command line argument as number only")
Euclidean_distance()