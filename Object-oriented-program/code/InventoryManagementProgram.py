'''
 @Author: Ritika Patidar
 @Date: 2021-02-19 14:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-19 12:15:38  
 @Title : Inventory Management problem
'''

import os
import sys
import json
import logging
import re
#configure logger file
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s%(filename)s%(asctime)s %(name)-s%(message)s')
handler.setFormatter(formatter)
#logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class InventoryManagement:

    """
    Description:
        this class define Inventory Management implementation
    Parameter:
        None
    Return:
        None
    """

    def __init__(self):
        self.data=load_data()

    def StockExist(self):
        """
        Description:
            this method define for check stock detail exist or not
        Parameter:
            None
        Return:
            boolean  : True or False
            search (dict) : stock all detail
            mode[userchoice] (string) : main key of json 
        """
        while True:
            try:
                userchoice=int(input("enter mode \n 0 : Rice \n 1 : Wheat \n 2: Pulse "))
                mode={0:"Rice",1:"Wheat",2:"Pulse"}
                search={
                "name":str(input("enter the brand name: ")).lower(),
                "price":str(input("enter the price: ")).lower(),
                "weight":str(input("enter the weight: ")).lower()
                }      
                if(re.match(r'^[1-9]\d*(\.\d{0,2})?$', search["price"]) and re.match(r'^[1-9]\d*(\.\d{0,2})?$', search["weight"]) and re.match("^[A-Za-z A-Za-z]*$",search["name"])):
                    break
            except ValueError as error:
                logger.error("ValueError occured")
            except KeyError as error:
                logger.error("KeyError occured")

        if search in self.data[mode[userchoice]]:
            return True,search,mode[userchoice]
        else:
            return False,search,mode[userchoice]

    def Add_stock(self):
        """
        Description:
            this method define for add stock detail if not exist
        Parameter:
            None
        Return:
            None
        """
        exist,search,key_data=self.StockExist()
        if(exist==False):
            self.data[key_data].append(search)
            with open(os.path.join(os.path.split(os.path.abspath(__file__) )[0], '../json_file/InventoryManagement.json'),'w') as jsonfile:
                json.dump(self.data,jsonfile,indent=3)
                jsonfile.close
            print("{0} detail added".format(search.values()))
            logger.debug("detail added successfully")
        else:
            print("details are already exist")

    def Update_stock(self):
        """
        Description:
            this method define for Update stock if exist or add stock on user choice
        Parameter:
            None
        Return:
            None
        """
        brand_exist=False
        while True:
            try:
                userchoice=int(input("enter mode \n 0 : Rice \n 1 : Wheat \n 2: Pulse: "))
                mode={0:"Rice",1:"Wheat",2:"Pulse"}
                brand_name=str(input("enter brand name: "))
                update_choice=int(input("what do you want update \n 1 : price \n 2: weight: "))
                update_mode={1:"price",2:"weight"}
                update_value=str(input("enter: ")).lower()
            except ValueError as error:
                logger.error("ValueError occured")
                userchoice=int(input("enter mode \n 0 : Rice \n 1 : Wheat \n 2: Pulse: "))
                mode={0:"Rice",1:"Wheat",2:"Pulse"}
                brand_name=str(input("enter brand name: "))
            except KeyError as error:
                logger.error("KeyError occured")
            if(re.match(r'^[1-9]\d*(\.\d{0,6})?$', update_value)):
                break
        index=0
        for brand in self.data[mode[userchoice]]:
            if(brand["name"]==brand_name):
                brand_exist=True
                self.data[mode[userchoice]][index][update_mode[update_choice]]=update_value
                with open(os.path.join(os.path.split(os.path.abspath(__file__) )[0], '../json_file/InventoryManagement.json'),'w') as jsonfile:
                    json.dump(self.data,jsonfile,indent=3)
                    jsonfile.close
                print("detail updated")
                logger.debug("detail updated successfully")
            index+=1
        if(brand_exist==False):
            if(str(input("this brand is not exist \n Do you want to add this brand? y or n: "))=="y"):
                self.Add_stock()

    def search_stock(self):
        """
        Description:
            this method define for search stock detail if exist or add stock detail on user choice
        Parameter:
            None
        Return:
            None
        """
        search_name=False
        while True:
            try:
                userchoice=int(input("enter mode \n 0 : Rice \n 1 : Wheat \n 2: Pulse: "))
                mode={0:"Rice",1:"Wheat",2:"Pulse"}
                brand_name=str(input("enter brand name: "))
                if(re.match("^[A-Za-z A-Za-z]*$",brand_name)):
                    break
            except ValueError as error:
                logger.error("ValueError occured")
            except KeyError as error:
                logger.error("KeyError occured")
        for brand in self.data[mode[userchoice]]:
            if(brand["name"]==brand_name):
                search_name=True
                print("{0} find".format(tuple(brand.items())))
                logger.debug("data search successfully")
        if(search_name==False):
            if(str(input("this brand is not exist \n Do you want to add this brand? y or n: "))=="y"):
                self.Add_stock()

    def add_remove_item(self):
        """
        Description:
            this method define for add and remove stock if exist or add stock on user choice
        Parameter:
            None
        Return:
            boolean  : True or False
            search (dict) : stock all detail
            mode[userchoice] (string) : main key of json 
        """
        search_name=False
        while True:
            try:
                userchoice=int(input("enter mode \n 0 : Rice \n 1 : Wheat \n 2: Pulse: "))
                mode={0:"Rice",1:"Wheat",2:"Pulse"}
                brand_name=str(input("enter brand name: "))
                add_item=str(input("enter weight of item: "))
                add_remove=int(input("enter mode \n 0 : add item \n 1 : remove item : "))
                if(re.match("^[A-Za-z A-Za-z]*$",brand_name) and re.match(r'^[1-9]\d*(\.\d{0,6})?$',add_item)):
                    break
            except ValueError as error:
                logger.error("ValueError occured")
            except KeyError as error:
                logger.error("KeyError occured")
        index=0
        for brand in self.data[mode[userchoice]]:
            if(brand["name"]==brand_name):
                search_name=True
                print("values before item added {0}".format(tuple(self.data[mode[userchoice]][index].items())))
                if(add_remove==0):
                    self.data[mode[userchoice]][index]["weight"]=float(self.data[mode[userchoice]][index]["weight"])+float(add_item)
                    print("values after item added {0}".format(tuple(self.data[mode[userchoice]][index].items())))
                    logger.debug("item added successfully")
                else:
                    if(float(self.data[mode[userchoice]][index]["weight"])-float(add_item)>=0):
                        self.data[mode[userchoice]][index]["weight"]=float(self.data[mode[userchoice]][index]["weight"])-float(add_item)
                        print("values after item removed {0}".format(tuple(self.data[mode[userchoice]][index].items())))
                        logger.debug("item removed successfully")
                    else:
                        print("couldn't full fill your requirement we have only {0} {1} kg".format(self.data[mode[userchoice]][index]["name"],self.data[mode[userchoice]][index]["weight"]))                    
                with open(os.path.join(os.path.split(os.path.abspath(__file__) )[0], '../json_file/InventoryManagement.json'),'w') as jsonfile:
                    json.dump(self.data,jsonfile,indent=3)
                    jsonfile.close()
                logger.debug("added item success fully")
            index+=1
        if(search_name==False):
                if(str(input("this brand is not exist \n Do you want to add this brand? y or n: "))=="y"):
                    self.Add_stock()

def load_data():
        """
        Description:
            this method define for load data from json file
        Parameter:
            None
        Return:
            data (dict) : load data of json file
        """
    with open(os.path.join(os.path.split(os.path.abspath(__file__) )[0], '../json_file/InventoryManagement.json'),'r') as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
    return data


# main code
if __name__=="__main__":
    ObjInventoryManagement=InventoryManagement()
    try:
        InventoryManagementMode=int(input("enter mode of Inventory Management Mode \n 0:add stock \n 1:update stock \n 2:search stock \n 3:add remove item: "))
        if(InventoryManagementMode==0):
            ObjInventoryManagement.Add_stock()
        elif(InventoryManagementMode==1):
            ObjInventoryManagement.Update_stock()
        elif(InventoryManagementMode==2):
            ObjInventoryManagement.search_stock()
        elif(InventoryManagementMode==3):
            ObjInventoryManagement.add_remove_item()
        else:
            logging.debug("invalid mode of Inventory Management")
    except ValueError as error:
        logging.error("ValueError error occured")
