'''
 @Author: Ritika Patidar
 @Date: 2021-02-18 10:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 10:15:38  
 @Title : Test Address Book problem
'''
import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('code'))
from Addressbook_Operation import Address_Book


class AddressbookTestCase(unittest.TestCase):
    def test_contact_exist(self):
        """
        Description:
            This method define for test case all of modify_define function of AddressBook.py code
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(Address_Book().contact_exist("ritika", "patel","vijay nagar","indore","m.p.","454665","9802346541"),(False,{"first_name": "ritika","last_name": "patel","address": "vijay nagar","city": "indore","state": "m.p.","zip": "454665","phone_number": "9802346541"}))
        self.assertEqual(Address_Book().contact_exist("ritu", "patel","vijay nagar","indore","m.p.","454665","9802346541"), (False,{"first_name": "ritu","last_name": "patel","address": "vijay nagar","city": "indore","state": "m.p.","zip": "454665","phone_number": "9802346541"}))
        self.assertIsNotNone(Address_Book().contact_exist("ritika", "patel","vijay nagar","indore","m.p.","454665","9802346541"))
        self.assertRaises(TypeError,Address_Book().contact_exist)

    def test_add_detail(self):
        """
        Description:
            This method define for test case all of add_detail function of AddressBook.py code
        Parameter:
            None
        Return:
            None
        """
        result=Address_Book().add_detail("ritu","patel","sanghvi nagar","vidisha","m.p.","450044","9002306541")
        self.assertIsNotNone(result)
        self.assertEqual(result,False)
        self.assertNotEqual(result,True)
        self.assertRaises(TypeError,Address_Book().add_detail)

    def test_search_detail(self):
        """
        Description:
            This method define for test case all of search_detail function of AddressBook.py code
        Parameter:
            None
        Return:
            None
        """
        self.assertIsNotNone(Address_Book().search_detail(0,"ritika"))
        self.assertEqual(Address_Book().search_detail(0,"ritika"),True)
        self.assertNotEqual(Address_Book().search_detail(0,"ritika"),False)
        self.assertEqual(Address_Book().search_detail(0,"damini"),False)
        self.assertRaises(TypeError,Address_Book().search_detail)

    def test_delete_person(self):
        """
        Description:
            This method define for test case all of delete function of AddressBook.py code
        Parameter:
            None
        Return:
            None
        """
        result=Address_Book().delete_person("ashvini", "patel","vijay nagar","indore","m.p.","454665","9802346541")
        self.assertIsNotNone(result)
        self.assertNotEqual(result,True)
        self.assertEqual(result,False)
        self.assertRaises(TypeError,Address_Book().delete_person)
    def test_update_detail(self):
        """
        Description:
            This method define for test case all of update_detail function of AddressBook.py code
        Parameter:
            None
        Return:
            None
       """
        result=Address_Book().update_detail("ritika", "patel","vijay nagar","indore","m.p.","454665","9802346541",0)
        self.assertIsNotNone(result)
        self.assertEqual(result,False)
        self.assertNotEqual(result,True)
        self.assertRaises(TypeError,Address_Book().update_detail)

if __name__ == '__main__':
    unittest.main()