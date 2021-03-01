import os
import sys
import json

def load_data():
    """
        Description:
            this method define for load data from json file
        Parameter:
            None
        Return:
            data (dict) : load data of json file
    """
    with open(os.path.abspath('json/StockAccountManagement.json'),'r') as jsonfile:
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
    with open(os.path.abspath( 'json/StockAccountManagement.json'),'w') as jsonfile:
        json.dump(data,jsonfile,indent=3)
        jsonfile.close()
