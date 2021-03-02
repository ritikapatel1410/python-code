import json
import os
import sys
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
from Addressbook_Operation import Address_Book,input_detail

def main():
    """
    Description:
        This main method defined for call function from Adressbook_Operation as per mode selected from user
    Parameter:
        None
    Return:
        None
    """
    try:
        AddressBookObj=Address_Book()
        AddressBookMode=int(input("enter mode of Address Book\n==============================================================\n0:search contact\n1:add contact\n2:del contact\n3:update contact\n4:Quit: "))
        if(AddressBookMode==0):
            mode,search=input_detail("search_detail")
            AddressBookObj.search_detail(mode,search)
        elif(AddressBookMode==1):
            first_name,last_name, address, city, state, zip_code, phone_number=input_detail("add_detail")
            AddressBookObj.add_detail(first_name,last_name, address, city, state, zip_code, phone_number)
        elif(AddressBookMode==2):
            first_name,last_name, address, city, state, zip_code, phone_number=input_detail("delete_person")
            AddressBookObj.delete_person(first_name,last_name, address, city, state, zip_code, phone_number)
        elif(AddressBookMode==3):
            first_name,last_name, address, city, state, zip_code, phone_number=input_detail("update_detail")
            AddressBookObj.update_detail(first_name,last_name, address, city, state, zip_code, phone_number)
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()