'''
 @Author: Ritika Patidar
 @Date: 2021-02-20 10:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-20 10:15:38  
 @Title : Test Inventory Management Problem
 '''
import os
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, os.path.abspath('./test/../code'))
from InventoryManagementProgram import InventoryManagement

class InventoryManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.item="Rice"
        self.name="kohinoor"
        self.weight="20"
        self.price="140"
 
    def test_StockExist(self):
        """
        Description:
            This method define for test case all of StockExist method of InventoryManagementProgram.py code
        Parameter:
            None
        Return:
            None
        """
        result = InventoryManagement().StockExist(self.item,self.name)
        self.assertEqual(result, True)
        self.assertNotEqual(result,False)
        self.assertIsNotNone(result)
        self.assertRaises(KeyError,InventoryManagement().StockExist,"rice","kohinoor")

    def test_Add_stock(self):
        """
        Description:
            This method define for cheack all test case of Add_stock method of InventoryManagementProgram.py code
        Parameter:
            None
        Return:
            None
        """
        result = InventoryManagement().Add_stock(self.item,self.name,self.weight,self.price)
        self.assertEqual(result, "item added")
        self.assertNotEqual(result, "item add")
        self.assertIsNotNone(result)

    def test_Update_stock(self):
        """
        Description:
            This method define for cheack all test case of Update_stock method of InventoryManagementProgram.py code
        Parameter:
            None
        Return:
            None
        """
        update_type="weight"
        update_quantity=00
        result = InventoryManagement().Update_stock(self.item,self.name,update_type,update_quantity)
        self.assertNotEqual(result, 117.0)
        self.assertIsNotNone(result)

    def test_search_stock(self):
        """
        Description:
            This method define for cheack all test case of search_stock method of InventoryManagementProgram.py code
        Parameter:
            None
        Return:
            None
        """
        result = InventoryManagement().search_data(self.item,self.name)
        self.assertEqual(result, {'name': 'kohinoor', 'price': '120', 'weight': '197.0'})
        self.assertNotEqual(result, {'name': 'kohinoor', 'price': '120', 'weight': '117.0'})
        self.assertIsNotNone(result)
        self.assertRaises(KeyError,InventoryManagement().search_data,"rice","kohinoor")
        self.assertRaises(KeyError,InventoryManagement().search_data,1,"kohinoor")

if __name__ == '__main__':
    unittest.main()
