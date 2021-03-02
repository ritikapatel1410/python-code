import json
import os
import sys
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile



def read_jsonfile():
    """
    Description:
        this method define for read AddressBook.json file and load data from json file
    Parameter:
        None
    Return:
        data (List): Load data from read file
    """
    try:
        with open(os.path.abspath('json/AddressBook.json'),'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
            loggerfile.Logger("info","successfully read data from json")
        return data
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))


def write_jsonfile(data):
    """
    Description:
        This method define for write data into AddressBook.json file
    Parameter:
        data (List): Modified load data 
    Return:
        None
    """
    try:
        with open(os.path.abspath('json/AddressBook.json'),'w') as jsonfile:
                json.dump(data,jsonfile,indent=7)
                jsonfile.close
                loggerfile.Logger("info","successfully read data from json")
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))