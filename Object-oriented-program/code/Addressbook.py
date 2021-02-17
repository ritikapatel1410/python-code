'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 12:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-17 12:15:38  
 @Title : Address Book problem
'''
import json
class Address_Book:
    def __init__(self):
        pass
    def input_detail(self):
        first_name=str(input("enter first name: "))
        last_name=str(input("enter last name: "))
        address=str(input("enter address: "))
        city=str(input("enter city: "))
        state=str(input("enter state: "))
        zip_code=str(input("enter zip: "))
        phone_number=str(input("enter phone number: "))
        return first_name,last_name, address, city, state, zip_code, phone_number
    def add_detail(self,first_name,last_name, address, city, state, zip_code, phone_number):
        person_detail = {'first_name':first_name,
                'last_name':last_name,
                'address' :address,
                    'city':city,
                    'state':state,
                    'zip': zip_code,
                    'phone_number':phone_number
                    }
        with open("/home/patidar/Desktop/GitHub_code/Object-oriented-program/python-code/Object-oriented-program/json_file/AddressBook.json",'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
        with open("/home/patidar/Desktop/GitHub_code/Object-oriented-program/python-code/Object-oriented-program/json_file/AddressBook.json",'w') as jsonfile:
            add_detail=data["AddressBook"].append(person_detail)
            json.dump(data,jsonfile,indent=7)
            jsonfile.close
    def search_detail(self,mode,search):
        with open("/home/patidar/Desktop/GitHub_code/Object-oriented-program/python-code/Object-oriented-program/json_file/AddressBook.json",'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
        counter=0   
        search_mode={0:"first_name",1:"last_name", 2:"address", 3:"city", 4:"state", 5:"zip_code", 6:"phone_number"}
        sorted_lastname=sorted(data["AddressBook"],key=lambda x:x["last_name"])
        for find in sorted_lastname:
            if find[search_mode[mode]].lower()==search.lower():
                counter+=1
                print(tuple(find.values()))
        return counter 
    def del_person(self,first_name,last_name, address, city, state, zip_code, phone_number):
        counter=0
        with open("/home/patidar/Desktop/GitHub_code/Object-oriented-program/python-code/Object-oriented-program/json_file/AddressBook.json",'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
        for find in data["AddressBook"]:
            if(find["first_name"]==first_name and find["last_name"]==last_name and find["address"]==address and find["city"]==city and find["state"]==state and find["zip"]==zip_code and find["phone_number"]==phone_number):
                counter+=1
                data["AddressBook"].remove(find)
                print("{0} deleted".format(tuple(find.values())))
        with open("/home/patidar/Desktop/GitHub_code/Object-oriented-program/python-code/Object-oriented-program/json_file/AddressBook.json",'w') as jsonfile:
            json.dump(data,jsonfile,indent=7)
            jsonfile.close
        return counter 



AddressBookObj=Address_Book()
mode=int(input("enter mode in int number 0:first_name,1:last_name, 2:address, 3:city, 4:state, 5:zip_code, 6:phone_number: "))
search=str(input("enter which you want to search: "))
print(AddressBookObj.input_detail())
#AddressBookObj.del_person()
if(AddressBookObj.search_detail(mode,search)==0):
    user_permision=str(input("this detail not exist in AddressBook!! Do you want to add? press y or n: "))
    if(user_permision=="y"):
        AddressBookObj.add_detail(AddressBookObj.input_detail())


        



        

