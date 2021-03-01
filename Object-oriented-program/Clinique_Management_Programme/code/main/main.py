'''
 @Author: Ritika Patidar
 @Date: 2021-02-22 21:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-22 21:15:38  
 @Title : main program for clinique Management Problem
'''
import os
import sys
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
import json_operation
import doctor
import patient

def main():
    try:
        search_mode=int(input("enter \n 0 : doctor \n 1 : patient \n 2 : quit() : "))
        if(search_mode==0):
            try:
                mode_doctor=int(input("enter \n 0 : doctor search \n 1 : doctor appointment \n 2 : popular doctor \n 3: popular specialization \n 4 : see doctor appointment: \n 5 : Quit():  "))
                if(mode_doctor==0):
                    search_type,search_detail=doctor.user_input("doctor_search")
                    doctor.doctor_management().doctor_search(search_type,search_detail)
                elif(mode_doctor==1):
                    name=doctor.user_input("take_appointment")
                    doctor.doctor_management().take_appointment(name)
                elif(mode_doctor==2):
                    doctor.doctor_management().popular_doctor()
                elif(mode_doctor==3):
                    doctor.doctor_management().popular_specialization()
                elif(mode_doctor==4):
                    doctor.doctor_management().show_appointment()
                elif(mode_doctor==5):
                    sys.exit()
                else:
                    print("invalid mode")
            except ValueError as error:
                loggerfile.Logger("error","invalid type of doctor mode")
        elif(search_mode==1):
            search_type,search_detail=patient.user_search()
            patient.patient_management().patient_search(search_type,search_detail)
        elif(search_mode==2):
            sys.exit()
        else:
            print("invalid mode")
    except ValueError as error:
        loggerfile.Logger("error","invalid type of mode")

main()