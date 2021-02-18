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

    def read_jsonfile(self):
        with open("/home/patidar/Desktop/GitHub_code/Object-oriented-program/python-code/Object-oriented-program/json_file/AddressBook.json",'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
        return data

    def write_jsonfile(self,data):    
        with open("/home/patidar/Desktop/GitHub_code/Object-oriented-program/python-code/Object-oriented-program/json_file/AddressBook.json",'w') as jsonfile:
                json.dump(data,jsonfile,indent=7)
                jsonfile.close

    def modify_index(self):
        change=int(input("enter 0:first_name,1:last_name, 2:address, 3:city, 4:state, 5:zip_code, 6:phone_number: "))
        search_mode={0:"first_name",1:"last_name", 2:"address", 3:"city", 4:"state", 5:"zip_code", 6:"phone_number"}
        return search_mode[change]

    def AddressBook_mode(self):
        mode=int(input("enter mode of Address Book 0:search contact  1:add contact 2:del contact 3:update contact: "))
        search_mode={0:self.search_detail() ,1:self.add_detail(),2:self.del_person(),3:self.update_detail()}
        return search_mode[mode]

    def input_detail(self):
        first_name=str(input("enter first name: "))
        last_name=str(input("enter last name: "))
        address=str(input("enter address: "))
        city=str(input("enter city: "))
        state=str(input("enter state: "))
        zip_code=str(input("enter zip: "))
        phone_number=str(input("enter phone number: "))
        return first_name,last_name, address, city, state, zip_code, phone_number

    def contact_exist(self):
        index=0
        first_name,last_name, address, city, state, zip_code, phone_number=self.input_detail()
        person_detail = {'first_name':first_name,
        'last_name':last_name,
        'address' :address,
            'city':city,
            'state':state,
            'zip': zip_code,
            'phone_number':phone_number
            }
        for find in data["AddressBook"]:
            if(find["first_name"].lower()==first_name.lower() and find["last_name"].lower()==last_name.lower() and find["address"].lower()==address.lower() and find["city"].lower()==city.lower() and find["state"].lower()==state.lower() and find["zip"].lower()==zip_code.lower() and find["phone_number"].lower()==phone_number.lower()):
                return (index,find)
            index+=1
        return (False,person_detail)

    def add_detail(self):
        data=self.read_jsonfile()
        find=self.contact_exist()
        if(find[0]==False):
            add_detail=data["AddressBook"].append(find[1])
            self.write_jsonfile(data)
            print("contact added")
        else:
            print("contact already exist")

    def search_detail(self):
        mode=int(input("enter mode in int number 0:first_name,1:last_name, 2:address, 3:city, 4:state, 5:zip_code, 6:phone_number: "))
        search=str(input("enter search detail"))
        data=self.read_jsonfile()
        search_mode={0:"first_name",1:"last_name", 2:"address", 3:"city", 4:"state", 5:"zip_code", 6:"phone_number"}
        sorted_lastname=sorted(data["AddressBook"],key=lambda x:x["last_name"])
        find=self.contact_exist()
        if(find[0]!=False):
            for find_contact in sorted_lastname:
                if find_contact[search_mode[mode]].lower()==search.lower():
                    print(tuple(find.values()))
        else:
            userchoice=str(input("do you want to add this contact: "))
            if(userchoice=="y"):
                self.add_detail() 

    def del_person(self):
        data=self.read_jsonfile()
        find=self.contact_exist(data)
        if(find[0]!=False):
            data["AddressBook"].remove(find[1])
            print("{0} deleted".format(tuple(find[1].values())))
        else:
            print("not find")
        self.write_jsonfile(data)

    def update_detail(self):
        data=self.read_jsonfile()
        find=self.contact_exist(data)
        if(find[0]!=False):
            change=self.modify_index()
            value=str(input("enter new {0} : ".format(change)))
            data["AddressBook"][find[0]][change]=value
            print("{0} detatil updated".format(find[1].values()))
            self.write_jsonfile(data)
        else:
            print("contact detail not found")
            
AddressBookObj=Address_Book()
AddressBookObj.AddressBook_mode()