'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 12:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 12:15:38  
 @Title : Address Book problem
'''
#add module
import ast
import json
import logging
import os

#define a class
class Address_Book:
    """
    Description:
        this class define for Address Book implementation
    Parameter:
        None
    Return:
        None
    """
    def __init__(self):
        pass

    def read_jsonfile(self):
        """
        Description:
            this method define for read AddressBook.json file and load data from json file
        Parameter:
            None
        Return:
            data (List): Load data from read file
        """
        fileDir = os.path.abspath(__file__) 
        with open(os.path.join(os.path.split(fileDir)[0], '../json_file/AddressBook.json'),'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
        return data

    def write_jsonfile(self,data):
        """
        Description:
            This method define for write data into AddressBook.json file
        Parameter:
            data (List): Modified load data 
        Return:
            None
        """
        fileDir = os.path.abspath(__file__) 
        with open(os.path.join(os.path.split(fileDir)[0], '../json_file/AddressBook.json'),'w') as jsonfile:
                json.dump(data,jsonfile,indent=7)
                jsonfile.close

    def modify_detail(self):
        """
        Description:
            This method define for modify key which user want to update
        Parameter:
            None
        Return:
            search_mode[change] (string) : detail which user want to change
        """
        change=int(input("enter 0:first_name,1:last_name, 2:address, 3:city, 4:state, 5:zip_code, 6:phone_number: "))
        search_mode={0:"first_name",1:"last_name", 2:"address", 3:"city", 4:"state", 5:"zip_code", 6:"phone_number"}
        return search_mode[change]

    def input_detail(self):
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
        first_name=str(input("enter first name: "))
        last_name=str(input("enter last name: "))
        address=str(input("enter address: "))
        city=str(input("enter city: "))
        state=str(input("enter state: "))
        zip_code=str(input("enter zip: "))
        phone_number=str(input("enter phone number: "))
        return first_name,last_name, address, city, state, zip_code, phone_number

    def contact_exist(self):
        """
            Description:
                This method define for check contact detail exist or not
            Parameter:
                None
            Return:
                True (boolean): If contact exist
                person_detail (dictionary) : entered detail of person
                False (boolean): If contact doesn't exist
        """
        first_name,last_name, address, city, state, zip_code, phone_number=self.input_detail()
        person_detail = {'first_name':first_name.lower(),
        'last_name':last_name.lower(),
        'address' :address.lower(),
        'city':city.lower(),
        'state':state.lower(),
        'zip': zip_code.lower(),
        'phone_number':phone_number.lower()
            }
        data=self.read_jsonfile()
        data_lowercase=str(data["AddressBook"]).lower()
        person_info=ast.literal_eval(data_lowercase)
        if(person_detail in person_info):
            return True,person_detail
        else:
            return False,person_detail

    def add_detail(self):
        """
        Description:
            This method define for add details of new person
        Parameter:
            None
        Return:
            None
        """
        person_exist,contact_detail=self.contact_exist()
        if(person_exist==False):
            data=self.read_jsonfile()
            add_detail=data["AddressBook"].append(contact_detail)
            self.write_jsonfile(data)
            logging.debug("person information added")
        else:
            logging.debug("person already exist")

    def search_detail(self):
        """
        Description:
            This method define for search details of person depend on user choice key and if person detail doesn't 
            exist then this will give choice to user for add detail of person
        Parameter:
            None
        Return:
            None
        """
        contact_count=0
        mode=int(input("enter mode in int number 0:first_name,1:last_name, 2:address, 3:city, 4:state, 5:zip_code, 6:phone_number: "))
        search=str(input("enter search detail: "))
        data=self.read_jsonfile()
        search_mode={0:"first_name",1:"last_name", 2:"address", 3:"city", 4:"state", 5:"zip_code", 6:"phone_number"}
        sorted_lastname=sorted(data["AddressBook"],key=lambda x:x["last_name"])
        for find_contact in sorted_lastname:
            if find_contact[search_mode[mode]].lower()==search.lower():
                logging.debug(tuple(find_contact.values()))
                contact_count+=1
        if contact_count==0:
            userchoice=str(input("do you want to add this contact press? y or n: "))
            if(userchoice=="y"):
                self.add_detail() 

    def delete_person(self):
        """
        Description:
            This method define for delete person detail 
        Parameter:
            None
        Return:
            None
        Output:
            if person detail exist then <<person detail deteted>> message will log into the logger.log file
            else <<contact detail not found>> will log into logger.log file
        """
        person_exist,contact_detail=self.contact_exist()
        data=self.read_jsonfile()
        if(person_exist==True):
            data["AddressBook"].remove(contact_detail)
            logging.debug("{0} deleted".format(tuple(contact_detail.values())))
        else:
            logging.debug("person information not found")
        self.write_jsonfile(data)

    def update_detail(self):
        """
        Description:
            This method define for update person detail 
        Parameter:
            None
        Return:
            None
        Output:
            if person detail exist then <<person detail updated>> else
            <<contact detail not found>> will log into the logger.log file
        """        
        person_exist,contact_detail=self.contact_exist()
        data=self.read_jsonfile()
        if(person_exist==True):
            change=self.modify_detail().lower()
            value=str(input("enter new {0} : ".format(change)))
            data["AddressBook"][data["AddressBook"].index(contact_detail)][change]=value
            logging.debug("{0} detatil updated".format(contact_detail.values()))
            self.write_jsonfile(data)
        else:
            logging.debug("contact detail not found")

if __name__ == "__main__":
    #Create and configure logger 
    logging.basicConfig(filename="/home/patidar/logger.log",level=logging.DEBUG,format='%(levelname)s:%(filename)s:%(funcName)s:%(asctime)s:%(name)s:%(message)s') 
    #Creating an object 
    logger=logging.getLogger('__name__')
    AddressBookObj=Address_Book()
    try:
        AddressBookMode=int(input("enter mode of Address Book 0:search contact  1:add contact 2:del contact 3:update contact: "))
        if(AddressBookMode==0):
            AddressBookObj.search_detail()
        elif(AddressBookMode==1):
            AddressBookObj.add_detail()
        elif(AddressBookMode==2):
            AddressBookObj.delete_person()
        elif(AddressBookMode==3):
            AddressBookObj.update_detail()
        else:
            logging.debug("invalid mode of Address Book")
    except ValueError as error:
        logging.error("ValueError error occured")