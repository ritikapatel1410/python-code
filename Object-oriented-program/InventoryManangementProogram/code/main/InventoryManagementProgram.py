'''
 @Author: Ritika Patidar
 @Date: 2021-02-19 14:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-19 19:15:38  
 @Title : Inventory Management problem
'''

import os
import sys
import json
import logging
import re
sys.path.insert(0, os.path.abspath('./code/../LogFile'))
import loggerfile 


class InventoryManagement:
    """
    Description:
        this class define Inventory Management implementation
    """

    def __init__(self):
        self.data=load_data()
    def StockExist(self,item,name):
        """
        Description:
            this method define for check stock detail exist or not
        Parameter:
            item (string) : type of item (rice,wheat,pulse)
            name (string) : brand name of item
        Return:
            True (boolean) : if stock exist
            False (boolean) : if stock doesnot exist

        """
        if name in [check["name"] for check in self.data[item]]:
            return True
        else:
            return False

    def Add_stock(self,item,name,weight,price):
        """
        Description:
            this method define for add stock detail if not exist
        Parameter:
            item (string)  : type of item (rice,wheat,pulse)
            name (string)  : brand name of item
            weight (string) : weight of item
            price (string) : price of item
        Return:
            A string : "item added"
        """
        item_detail={"name":name,
                        "price":price,
                        "weight":weight
        }
        self.data[item].append(item_detail)
        upload_data(self.data)
        loggerfile.Logger(logging.DEBUG,"detail added successfully")
        return "item added"

    def Update_stock(self,item,name,update_type,update_quantity):
        """
        Description:
            this method define for Update stock if exist 
        Parameter:
            item (string)  : type of item (rice,wheat,pulse)
            name (string)  : brand name of item
            weight (string) : weight of item
            price (string) : price of item
            update_type (string) : update type (price or weight)
            update_quantity (string) : value of price or weight

        Return:
           updated value of weight or price (depends on user choice)
        """
        if(update_type=="weight"):
            for add_kg in self.data[item]:
                if(add_kg["name"]==name):
                    add_kg["weight"]=str(float(add_kg["weight"])+float(update_quantity))
                    upload_data(self.data)
                    loggerfile.Logger(logging.DEBUG,"weight updated")
                    return float(add_kg["weight"])+float(update_quantity)

        else:
            for price_update in self.data[item]:
                if(price_update["name"]==name):
                    price_update["price"]=update_quantity
                    upload_data(self.data)
                    loggerfile.Logger(logging.DEBUG,"price updated")
                    return update_quantity
    
    def search_data(self,item,name):
        """
        Description:
            this method define for search stock if exist 
        Parameter:
            item (string)  : type of item (rice,wheat,pulse)
            name (string)  : brand name of item
        Return:
            search (string) : detail of serached item
        """
        for search in self.data[item]:
            if(search["name"]==name):
                return search
    
    def calcutate_inventory(self,item,name,weight):
        """
        Description:
            this method define for calculate_inventory 
        Parameter:
            item (string)  : type of item (rice,wheat,pulse)
            name (string)  : brand name of item
            weight (string) : weight of item
         Return:
            return will vary depends on condition 
        """
        for calculate in self.data[item]:
            if(calculate["name"]==name):
                if(float(calculate["weight"])>=float(weight)):
                    calculate["weight"]=str(float(calculate["weight"])-float(weight))
                    upload_data(self.data)
                    return [True,[name,weight,calculate["price"]],float(weight)*float(calculate["price"])]
                else:
                    return [False, name]



def input_fuction(return_input):
    """
    Description:
        this method define for user input 
    Parameter:
        return_input (string) : condition for different function input
        Return:
        return different type of inputs on function requirement
    """

    while True:
        if(return_input=="stock_exist"):
            item=str(input("enter item: ")).capitalize() 
            name=str(input("enter brand name: ")).lower()
            if(re.match("^[A-Za-z A-Za-z]*$",name) and re.match("^[A-Za-z A-Za-z]*$",item)):
                return item, name
        elif(return_input=="add_stock"):
            weight=str(input("enter weight: ")).lower()
            price=str(input("enter price: ")).lower()
            if(re.match(r'^[1-9]\d*(\.\d{0,6})?$',weight) and re.match(r'^[1-9]\d*(\.\d{0,6})?$',price)):
                return weight, price
        elif(return_input=="update_stock"):
            try:
                choice=int(input("what do you want \n add weight enter 0 \n update price of item 1: "))
            except ValueError as error:
                print("enter 0 or 1 only")
            if(choice==0):
                weight=str(input("enter weight: ")).lower()
                if(re.match(r'^[1-9]\d*(\.\d{0,6})?$',weight)):
                    return "weight",weight
            else:
                price=str(input("enter price: ")).lower()
                if(re.match(r'^[1-9]\d*(\.\d{0,6})?$',price)):
                    return "price",price
        else:
            weight=str(input("enter weight: ")).lower()
            if(re.match(r'^[1-9]\d*(\.\d{0,6})?$',weight)):
                    return weight





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

def upload_data(data):
    """
        Description:
            this method define for upload data into json file
        Parameter:
           data (dict) : loaded data from json file
        Return:
            None
    """
    with open(os.path.join(os.path.split(os.path.abspath(__file__) )[0], '../json_file/InventoryManagement.json'),'w') as jsonfile:
        json.dump(data,jsonfile,indent=3)
        jsonfile.close()

def main():
    """
    Description:
        this is main function it will manage mode of invententory system
    Parameter:
        None
    Return:
        None
    """
    ObjInventoryManagement=InventoryManagement()
    try:
        InventoryManagementMode=int(input("enter mode of Inventory Management Mode \n 0:add stock \n 1:update stock \n 2:search stock \n 3:calcutate_inventory"))
        if(InventoryManagementMode==0):
            item,name=input_fuction("stock_exist")
            if(ObjInventoryManagement.StockExist(item,name)==False):
                weight,price=input_fuction("add_stock")
                ObjInventoryManagement.Add_stock(item,name,weight,price)
            else:
                print("stock already exist")
        elif(InventoryManagementMode==1):
            item,name=input_fuction("stock_exist")
            if(ObjInventoryManagement.StockExist(item,name)==True):
                update_type,update_quantity=input_fuction("update_stock")
                ObjInventoryManagement.Update_stock(item,name,update_type,update_quantity)
            else:
                print("stock not exist")
        elif(InventoryManagementMode==2):
            item,name=input_fuction("stock_exist")
            if(ObjInventoryManagement.StockExist(item,name)==True):
                print(ObjInventoryManagement.search_data(item,name))
        elif(InventoryManagementMode==3):
            list_item_not_available=[]
            list_item_not_sufficient=[]
            list_item_available=[]
            total=[]
            while True:
                item,name=input_fuction("stock_exist")
                if(ObjInventoryManagement.StockExist(item,name)==True):
                    weight=input_fuction("calulate")
                    result=ObjInventoryManagement.calcutate_inventory(item,name,weight)
                    print(result)
                    if(result[0]==True):
                        list_item_available.append(result[1])
                        total.append(result[2])
                    else:
                        list_item_not_sufficient.append(result[1])

                else:
                    list_item_not_available.append(name)
                if(str(input("do you want add something ? y or n: "))=="n"):
                    print("##### invoice is here #####")
                    if(len(list_item_available)>0):
                        for list_item in list_item_available:
                            print("{0}   {1}X{2}".format(list_item[0],list_item[1],list_item[2]))
                    if(len(list_item_not_sufficient)>0):
                        print("##### not sufficient quantity item #####")
                        for list_item in list_item_not_sufficient:
                            print("{0}   not sufficient".format(list_item[0]))
                    if(len(list_item_not_available)>0):
                        print("##### not available item #####")
                        for list_item in list_item_not_available:
                            print("{0}   not available".format(list_item))
                    print("##### total #####")
                    print("total:{0}".format(sum(total)))
                    break
        else:
            loggerfile.Logger(logging.DEBUG,"invalid mode of Inventory Management")
    except ValueError as error:
        loggerfile.Logger(logging.ERROR,"ValueError error occured")
    



if __name__=="__main__":
    ObjInventoryManagement=InventoryManagement()
    main()