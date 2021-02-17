'''
 @Author: Ritika Patidar
 @Date: 2021-02-10 14:40:20
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-11 13:20:38  
 @Title : Replace string problem
'''
import re
def print_name():
    user_name=input("enter the name: ")
    given_string="Hello <<UserName>>, How are you?"
    if(len(user_name)>=3 and (re.match("^[A-Za-z A-Za-z]*$", user_name)!=None)):
        new_string = re.sub("<<UserName>>", user_name, given_string)
        print(new_string) 
    else:
        print("invalid name try again")
        print_name()
print_name()
