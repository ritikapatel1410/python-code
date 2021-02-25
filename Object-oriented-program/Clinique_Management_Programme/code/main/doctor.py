'''
 @Author: Ritika Patidar
 @Date: 2021-02-22 21:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-22 21:15:38  
 @Title : doctor program for clinique Management Program
'''
import os
import sys
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
import json_operation
import re

class doctor_management:
    def __init__(self):
        self.data_doctor=json_operation.load_data_doctor()
        self.data_appointent=json_operation.load_data_appoitment()
    def doctor_search(self,search_type,search_detail):
        check=False
        list_name=[]
        for search in self.data_doctor:
             if(search[search_type]==search_detail or (search_detail in search[search_type])):
                check=True
                list_name.append(tuple(search.values())[0])
                print("#### DOCTOR DETAIL #### \n name : {0} \n id : {1} \n specialziation : {2} \n availablity : {3}".format(tuple(search.values())[0],tuple(search.values())[1],tuple(search.values())[2],tuple(search.values())[3]))
                loggerfile.Logger("debug","searched successfully")
                if(search_type=="name"or search_type=="id"):
                    if(tuple(search.values())[0] in self.data_appointent["search_name"][0].keys()):
                        self.data_appointent["search_name"][0][tuple(search.values())[0]]=str(int(self.data_appointent["search_name"][0][tuple(search.values())[0]])+1)
                        json_operation.upload_data_appoitment(self.data_appointent)
                    else:
                       self.data_appointent["search_name"][0][tuple(search.values())[0]]="1"
                       json_operation.upload_data_appoitment(self.data_appointent)
                if(search_type=="specialization"):
                    if(tuple(search.values())[2] in self.data_appointent["specialization"][0].keys()):
                        self.data_appointent["specialization"][0][tuple(search.values())[2]]=str(int(self.data_appointent["specialization"][0][tuple(search.values())[2]])+1)
                        json_operation.upload_data_appoitment(self.data_appointent)
                    else:
                        self.data_appointent["specialization"][0][tuple(search.values())[2]]="1"
                        json_operation.upload_data_appoitment(self.data_appointent)

        if(check==True):
            return (True,list_name)
        else:
            print("detail not found")
            return (False,0) 
    
    def take_appointment(self,name):
        if(name in [name_list["name"] for name_list in self.data_doctor]):
            if(name in self.data_appointent["appointment"][0].keys()):
                if(int(self.data_appointent["appointment"][0][name])<5):
                    self.data_appointent["appointment"][0][name]=str(int(self.data_appointent["appointment"][0][name])+1)
                    json_operation.upload_data_appoitment(self.data_appointent)
                    self.data_appointent["search_name"][0][name]=str(int(self.data_appointent["search_name"][0][name])+1)
                    json_operation.upload_data_appoitment(self.data_appointent)
                    print("appointment fixed")
                    loggerfile.Logger("debug","take appointment successfully")
                else:
                    self.data_appointent["search_name"][0][name]=str(int(self.data_appointent["search_name"][0][name])+1)
                    json_operation.upload_data_appoitment(self.data_appointent)
                    print("today not possible try for next day")
            else:
                self.data_appointent["appointment"][0][name]=str(1)  
                json_operation.upload_data_appoitment(self.data_appointent)
                print("appointment fixed")
                self.data_appointent["search_name"][0][name]=str(1)
                json_operation.upload_data_appoitment(self.data_appointent)
                loggerfile.Logger("debug","take appointment successfully")
        else:
            print("this doctor not available")

    def popular_doctor(self):
        sorted_doctor={key: value for key, value in sorted(self.data_appointent["search_name"][0].items(), key=lambda item:int(item[1]))}
        for key,value in sorted_doctor.items():
            if(value==tuple(sorted_doctor.values())[len(sorted_doctor)-1]):
                print("####################     {0} most popular doctor       ####################".format(key))
                loggerfile.Logger("debug","most popular doctor find")
        return True

    def popular_specialization(self):
        sorted_specialization={key: value for key, value in sorted(self.data_appointent["specialization"][0].items(), key=lambda item: int(item[1]))}
        for key,value in sorted_specialization.items():
            if(value==tuple(sorted_specialization.values())[len(sorted_specialization)-1]):
                print("#####  {0} most popular specialization   ##### ".format(key))
                loggerfile.Logger("debug","most specialization doctor find")
        return True

    def show_appointment(self):
        print("========================= Doctor Appointment Detail Here =============================")
        for doctor,appointment in self.data_appointent["appointment"][0].items():
            print("doctor {0} have {1} appointment".format(doctor,appointment))

def user_input(return_input):
    while True:
        if(return_input=="doctor_search"):
            try:
                search_mode=int(input("enter \n 0 : doctor name \n 1 : doctor id \n 2 : doctor availability : \n 3 : specialziation \n 4 : Quit() : "))
                if(search_mode==0 ):
                    name=str(input("enter doctor name: ")).lower()
                    if(re.match("^[A-Za-z A-Za-z]*$",name)):
                        return "name",name
                    else:
                        print("invalid name")
                elif(search_mode==1):
                    id=str(input("enter doctor id: ")).lower()
                    if(re.match(r'^[0-9]{4}$',id)):
                        return "id",id
                    else:
                            print("invalid id")
                elif(search_mode==2):
                    availability=str(input("enter doctor availability: ")).lower()
                    if(re.match(r'^am$',availability) or re.match(r'^pm$',availability) or re.match(r'^am & pm$',availability)):
                        return "availability",availability
                    else:
                        print("invalid availability")
                elif(search_mode==3):
                    specialization=str(input("enter doctor specialization: ")).lower()
                    if(re.match("^[A-Za-z A-Za-z]*$",specialization)):
                        return "specialization",specialization
                    else:
                        print("invalid availability")
                elif(search_mode==4):
                    sys.exit()
            except ValueError as error:
                loggerfile.Logger("error","invalid mode entered")

        elif(return_input=="take_appointment"):
            name=str(input("enter doctor name: ")).lower()
            if(re.match("^[A-Za-z A-Za-z]*$",name)):
                    return name
            else: 
                print("invalid_name")
