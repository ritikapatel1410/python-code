'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 16:40:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 14:07:38  
 @Title : Prime factor problem
'''
while True:
    try:
        username=int(input("enter the number: "))
        for factor in range(1,username+1):
            flag=True
            if(username%factor==0):
                for prime_factor in range(2,int(factor/2)+1):
                    if(factor%prime_factor==0):
                        flag=False
                        break
                if(flag==True):
                    print(factor, end=" ")
        print("\r")
        break
    except Exception as error:
        print("{0} error occured".format(error))

