'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 17:50:30
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 15:20:40 
 @Title : count triplet sum zero problem
'''
while True:
    try:
        n=int(input("enter the number of element: "))
        array=[int(input("enter the value: ")) for i in range(n)]
        print("input array is: ", array)
        count=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if(array[i]+array[j]+array[k]==0):
                        print(array[i],array[j],array[k])
                        count+=1
        print("triplet sums are: ", count)
        break
    except:
        print("enter only number try again !!")


