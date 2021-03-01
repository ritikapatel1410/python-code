'''
 @Author: Ritika Patidar
 @Date: 2021-02-21 14:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-21 19:15:38  
 @Title : Stock account Management problem
'''

import os
import sys
import json
import re
import json_operation
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

class create_stock:
    def __init__(self):
        self.data=json_operation.load_data()

    def stock_exist(self,stock):
        """
        Description:
            this method define for check stock detail exist or not
        Parameter:
            stock (string): stock
        Return:
            True (boolean) : if stock exist
            False (boolean) : if stock doesnot exist

        """
        if stock in  self.data.keys():
            return True
        else:
            return False

    def add_stock(self,stock,company_name,no_of_share,price_of_share):
        """
        Description:
            this method define for add stock detail if not exist
        Parameter:
            stock (string): stock

        Return:
            True (boolean) : if stock exist
            False (boolean) : if stock doesnot exist

        """
        if(self.stock_exist(stock)==True):
            loggerfile.Logger("debug","stock already exist")
            return "stock already exist"
        else:
            stock_detail=[{"stock_name":company_name,
			"number_of_shares": no_of_share,
			"share_price": price_of_share
            }]
        self.data[stock]=stock_detail
        json_operation.upload_data(self.data)
        loggerfile.Logger("debug","stock added")
        return "stock added"

    def update_share_price(self,stock,price_of_share):
        if(self.stock_exist(stock)==True):
            self.data[stock][0]["share_price"]=price_of_share
            json_operation.upload_data(self.data)
            loggerfile.Logger("debug","updated successfully")
            return True
        else:
            return False

    def sell_stock_share(self,stock,no_of_share):
        if(self.stock_exist(stock)==True):
            if(int(no_of_share)<=int(self.data[stock][0]["number_of_shares"])):
                self.data[stock][0]["number_of_shares"]=str(int(self.data[stock][0]["number_of_shares"])-int(no_of_share))
                json_operation.upload_data(self.data)
                loggerfile.Logger(logging.DEBUG,"sell stock successfully")
                return "share selled suffessfully"
            else:
                return "unsufficient share"

        else:
            return "stock not available"

    def purchase_stock_share(self,stock,no_of_share):
        if(self.stock_exist(stock)==True):
            self.data[stock][0]["number_of_shares"]=str(int(self.data[stock][0]["number_of_shares"])+int(no_of_share))
            json_operation.upload_data(self.data)
            loggerfile.Logger("debug","sell stock successfully")
            return "share purchased suffessfully"
        else:
            return "stock not available"


def input_fuction(return_value):
    if(return_value=="add_stock"):
        stock=str(input("enter stock: ")).lower()
        company_name=str(input("enter stock name: ")).lower()
        no_of_share=str(input("no of shares: ")).lower()		
        price_of_share=str(input("price of share: ")).lower()
        return stock,company_name,no_of_share,price_of_share
    elif(return_value=="update_share"):
        stock=str(input("enter stock: ")).lower()
        price_of_share=str(input(" update price of share: ")).lower()
        return stock,price_of_share
    elif(return_value=="sell_share"):
        stock=str(input("enter stock: ")).lower()
        no_of_share=str(input("no of shares: ")).lower()		
        return stock,no_of_share
    else:
        stock=str(input("enter stock: ")).lower()
        no_of_share=str(input("no of shares: ")).lower()		
        return stock,no_of_share




