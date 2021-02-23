'''
 @Author: Ritika Patidar
 @Date: 2021-02-21 21:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-21 21:15:38  
 @Title : Stock account Management problem
'''
import os
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, os.path.abspath('./test/../code'))
import StockManagement

class InventoryManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.stock="ibm"
        self.company_name="ibm private ltd"
        self.no_of_share="5"
        self.price_of_share="350"

    def test_stock_exist(self):
        result=StockManagement.create_stock().stock_exist(self.stock)
        self.assertEqual(result, True)
        self.assertNotEqual(result,False)
        stock="philips"
        result=StockManagement.create_stock().stock_exist(stock)
        self.assertEqual(result, False)
        self.assertIsNotNone(result)

    def test_add_stock(self):
        result=StockManagement.create_stock().add_stock(self.stock,self.company_name,self.no_of_share,self.price_of_share)
        self.assertEqual(result, "stock already exist")
        self.assertNotEqual(result,"stock added")
        self.assertIsNotNone(result)

    def test_add_stock(self):
        result=StockManagement.Stock_Portfolio().calute_stock()
        self.assertEqual(result, 55338.0)
        self.assertNotEqual(result,123)
        self.assertIsNotNone(result)
    

if __name__ == '__main__':
    unittest.main()