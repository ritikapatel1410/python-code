'''
 @Author: Ritika Patidar
 @Date: 2021-02-22 21:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-22 21:15:38  
 @Title : patient program for clinique Management Program
'''
import os
import sys
sys.path.insert(0, os.path.abspath('./LogFile'))
import loggerfile
import json_operation
import re

class patient_management:
    def __init__(self):
        self.data_patient=json_operation.load_data_patient()
    def patient_search(self,search_type,search_detail):
        check=False
        for search in self.data_patient:
             if(search[search_type]==search_detail):
                check=True
                print("#### PATIENT DETAIL #### \n name : {0} \n id : {1} \n mobilenumber: {2}".format(tuple(search.values())[0],tuple(search.values())[1],tuple(search.values())[2]))
                loggerfile.Logger("debug","searched successfully")
        if(check==True):
            return "detail searched"
        else:
            print("detail not found")
            return "detail not match"


def user_search():
    while True:
        try:
            search_mode=int(input("enter \n 0 : name \n 1 : id \n 2 : mobile number:  "))
            if(search_mode==0):
                name=str(input("enter patient name: ")).lower()
                if(re.match("^[A-Za-z A-Za-z]*$",name)):
                    return "name",name
                else:
                    print("invalid name")
            elif(search_mode==1):
                id=str(input("enter patient id: ")).lower()
                if(re.match(r'^[0-9]{4}$',id)):
                    return "id",id
                else:
                        print("invalid id")
            elif(search_mode==2):
                mobile_number=str(input("enter patient mobile number: ")).lower()
                if(re.match(r'^[7-9]{1}[0-9]{9}$',mobile_number)):
                    return "phone_number",mobile_number

        except ValueError as error:
            loggerfile.Logger("error","invalid mode entered")
