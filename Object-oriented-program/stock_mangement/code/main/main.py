'''
 @Author: Ritika Patidar
 @Date: 2021-02-21 14:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-21 19:15:38  
 @Title : main code of Stock account Management problem
'''

import os
import sys
import json
import re
import StockManagement
import stockMangement_portfolio
import json_operation
sys.path.insert(0, os.path.abspath('code/LogFile'))
import loggerfile 

def main():
    try:
        mode=int(input("do you want excess\n stock create enter: 0 \n or Stock Portfolio enter 1 :"))
        if(mode==0):
            try:
                create_mode=int(input("enter \n add stock : 0 \n or update share price : 1 \n or sell share : 2 \n or purchase : 3 "))
                if(create_mode==0):
                    stock,company_name,no_of_share,price_of_share=StockManagement.input_fuction("add_stock")
                    StockManagement.create_stock().add_stock(stock,company_name,no_of_share,price_of_share)
                elif(create_mode==1):
                    stock,price_of_share=StockManagement.input_fuction("update_share")
                    StockManagement.create_stock().update_share_price(stock,price_of_share)
                elif(create_mode==2):
                    stock,no_of_share=StockManagement.input_fuction("sell_share")
                    StockManagement.create_stock().sell_stock_share(stock,no_of_share)
                else:
                    stock,no_of_share=StockManagement.input_fuction("purchase_share")
                    StockManagement.create_stock().purchase_stock_share(stock,no_of_share)

            except ValueError as error:
                loggerfile.Logger("error","value error accured")

        else:
            stockMangement_portfolio.Stock_Portfolio().calute_stock()
    except ValueError as error:
        loggerfile.Logger("error","value error accured")

if __name__=="__main__":
    main()