'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 14:50:17
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 14:20:35  
 @Title : Harmonic number problem
'''
def print_harmonics():
    try:
        num=int(input("enter the number: "))
        nth_harmonic=0
        for i in range(1,num+1):
            nth_harmonic+=1/i
        print(nth_harmonic)
    except Exception as error:
        print("{0} error occured".format(error))
        print_harmonics()
print_harmonics()