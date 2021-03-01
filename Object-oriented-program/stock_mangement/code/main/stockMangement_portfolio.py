import os
import sys
import json
import logging
import re
import json_operation
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

class Stock_Portfolio:
    def __init__(self):
        self.data=json_operation.load_data()
    def calute_stock(self):
        total=[]
        stock_detail=[]
        index=0
        for detail in self.data:
            stock_detail.append([detail,self.data[detail][0]["stock_name"],self.data[detail][0]["number_of_shares"],self.data[detail][0]["share_price"]])
            total.append(float(self.data[detail][0]["number_of_shares"])*float(self.data[detail][0]["share_price"]))
        print("================================================= REPORT IS HERE ===================================================")
        print("stock          |stock_name                    |no_of_share          |stock_price          |{total_share_price          ")
        print("======================================================================================================================")  
        for cal in stock_detail:
            print("{0:<15}|{1:<30}|{2:<21}|{3:<21}|{4:<15}".format(stock_detail[index][0],stock_detail[index][1],stock_detail[index][2],stock_detail[index][3],total[index]))
            index+=1
        print("=========================================================================================================================\ntotal : {0}".format(sum(total)))
        loggerfile.Logger("debug","report genrated")
        return sum(total)

