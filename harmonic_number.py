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
        string=""
        for i in range(1,num+1):
            if(i<num):
                string+="1/"+str(i)+" + "
            else:
                string+="1/"+str(i)
        print(string)
    except:
        print("enter number only")
        print_harmonics()
print_harmonics()

    

    
