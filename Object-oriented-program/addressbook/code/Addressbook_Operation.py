'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 12:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 12:15:38  
 @Title : Address Book problem
'''
import ast
import json
import os
import sys
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
import json_operation

class Address_Book:
    """
    Description:
        this class define for Address Book implementation
    """
    def __init__(self):
        self.data=json_operation.read_jsonfile()

    def modify_detail(self,mode):
        """
        Description:
            This method define for modify key which user want to update
        Parameter:
            None
        Return:
            search_mode[change] (string) : detail which user want to change
        """
        search_mode={0:"first_name",1:"last_name", 2:"address", 3:"city", 4:"state", 5:"zip_code", 6:"phone_number"}
        return search_mode[mode]

    def contact_exist(self,first_name,last_name, address, city, state, zip_code, phone_number):
        """
            Description:
                This method define for check contact detail exist or not
            Parameter:
                first_name : first name of user
                last_name : last name of user
                address : address of user
                city : city of user
                state : state of user
                zip_code : zip code of user
                phone_number : phone number of user
                mode : mode of user
            Return:
                True (boolean): If contact exist
                person_detail (dictionary) : entered detail of person
                False (boolean): If contact doesn't exist
        """
        person_detail = {'first_name':first_name.lower(),
        'last_name':last_name.lower(),
        'address' :address.lower(),
        'city':city.lower(),
        'state':state.lower(),
        'zip': zip_code.lower(),
        'phone_number':phone_number.lower()
            }
        data_lowercase=str(self.data["AddressBook"]).lower()
        person_info=ast.literal_eval(data_lowercase)
        if(person_detail in person_info):
            return True,person_detail
        else:
            return False,person_detail

    def add_detail(self,first_name,last_name, address, city, state, zip_code, phone_number):
        """
        Description:
            This method define for add details of new person
        Parameter:
            first_name : first name of user
            last_name : last name of user
            address : address of user
            city : city of user
            state : state of user
            zip_code : zip code of user
            phone_number : phone number of user
            mode : mode of user
        Return:
            True: if detail added
            False : if detail not added
        """
        Flag=False
        person_exist,contact_detail=self.contact_exist(first_name,last_name, address, city, state, zip_code, phone_number)
        if(person_exist==False):
            add_detail=self.data["AddressBook"].append(contact_detail)
            json_operation.write_jsonfile(self.data)
            print("person information added")
            loggerfile.Logger("info","person information added")
            Flag=True
        else:
            print("person already exist")
            loggerfile.Logger("info","person already exist")
            Flag=False
        return Flag

    def search_detail(self,mode,search):
        """
        Description:
            This method define for search details of person depend on user choice key and if person detail doesn't 
            exist then this will give choice to user for add detail of person
        Parameter:
            mode : search type
            search : what do you want in search in search type
        Return:
            None
        """
        Flag=False
        search_mode={0:"first_name",1:"last_name", 2:"address", 3:"city", 4:"state", 5:"zip_code", 6:"phone_number"}
        sorted_lastname=sorted(self.data["AddressBook"],key=lambda x:x["last_name"])
        for find_contact in sorted_lastname:
            if find_contact[search_mode[mode]].lower()==search.lower():
                print(tuple(find_contact.values()))
                loggerfile.Logger("info","search successfully")
                Flag=True
        return Flag
        
    def delete_person(self,first_name,last_name, address, city, state, zip_code, phone_number):
        """
        Description:
            This method define for delete person detail 
        Parameter:
            first_name : first name of user
            last_name : last name of user
            address : address of user
            city : city of user
            state : state of user
            zip_code : zip code of user
            phone_number : phone number of user
            mode : mode of user
        Return:
            True : if detail deleted
            False : if detail not deleted
        Output:
            if person detail exist then <<person detail deteted>> message will log into the logger.log file
            else <<contact detail not found>> will log into logger.log file
        """
        Flag=False
        person_exist,contact_detail=self.contact_exist(first_name,last_name, address, city, state, zip_code, phone_number)
        if(person_exist==True):
            self.data["AddressBook"].remove(contact_detail)
            print("{0} deleted".format(tuple(contact_detail.values())))
            loggerfile.Logger("info","delete successfully")
            Flag=True
        else:
            print("person information not found")
            loggerfile.Logger("info","person information not found")
            Flag=False
        json_operation.write_jsonfile(self.data)
        return Flag

    def update_detail(self,first_name,last_name, address, city, state, zip_code, phone_number,mode):
        """
        Description:
            This method define for update person detail 
        Parameter:
            first_name : first name of user
            last_name : last name of user
            address : address of user
            city : city of user
            state : state of user
            zip_code : zip code of user
            phone_number : phone number of user
            mode : mode of user
        Return:
            True: if detaol updated
            False : if detail not updated
        Output:
            if person detail exist then <<person detail updated>> else
            <<contact detail not found>> will log into the logger.log file
        """ 
        Flag=False       
        person_exist,contact_detail=self.contact_exist(first_name,last_name, address, city, state, zip_code, phone_number)
        
        if(person_exist==True):
            change=self.modify_detail(mode).lower()
            value=str(input("enter new {0} : ".format(change)))
            self.data["AddressBook"][self.data["AddressBook"].index(contact_detail)][change]=value
            print("{0} detatil updated".format(contact_detail.values()))
            loggerfile.Logger("info","contact updated")
            json_operation.write_jsonfile(self.data)
            Flag=True
        else:
            print("contact detail not found")
            loggerfile.Logger("info","contact detail not found")
            Flag=False
        return Flag

def input_detail(return_type):
        """
        Description:
            This method define for take the contact detail from the user
        Parameter:
            None
        Return:
            first_name (string): First name of the person
            last_name (string): First name of the person
            address (string): Address of the person 
            city (string): City of the the address 
            state (string): State of the city
            zip_code (string): zip_code of the area
            phone_number (string): Phone number of the person
        """
        try:
            if(return_type=="contact_exist" or return_type=="delete_person" or return_type=="add_detail"):        
                first_name=str(input("enter first name: "))
                last_name=str(input("enter last name: "))
                address=str(input("enter address: "))
                city=str(input("enter city: "))
                state=str(input("enter state: "))
                zip_code=str(input("enter zip: "))
                phone_number=str(input("enter phone number: "))
                return first_name,last_name, address, city, state, zip_code, phone_number
            elif(return_type=="search_detail"):
                mode=int(input("enter mode in int number========================================\n0:first_name\n1:last_name\n2:address\n3:city\n4:state\n5:zip_code\n6:phone_number\n7:Quit"))
                search=str(input("========================================================\nenter search detail: "))
                return mode,search
            elif(return_type=="update_detail"):
                first_name=str(input("enter first name: "))
                last_name=str(input("enter last name: "))
                address=str(input("enter address: "))
                city=str(input("enter city: "))
                state=str(input("enter state: "))
                zip_code=str(input("enter zip: "))
                phone_number=str(input("enter phone number: "))
                mode=int(input("==================================enter\n0:first_name\n1:last_name\n2:address\n3:city\n4:state\n5:zip_code\n6:phone_number:"))
                return first_name,last_name, address, city, state, zip_code, phone_number, mode  
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format())



