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
from unittest.mock import patch
from Object-oriented-program.code.Addressbook import Address_Book


class AddressbookTestCase(unittest.TestCase):
    @patch('builtins.input', return_value=0)
    def test_modify_detail(self,input):
        """
        Description:
            This method define for test case all of modify_define function of AddressBook.py code
        Parameter:
            input (int) = for userinput of modify_define
        Return:
            None
        """
        result = Address_Book().modify_detail()
        self.assertEqual(result, "first_name")
        self.assertNotEqual(result, "first")
        self.assertIsNotNone(result)

    @patch('builtins.input')
    def test_input_detail(self,mocked_input):
        """
        Description:
            This method define for test case all of input_detail function of AddressBook.py code
        Parameter:
            mocked_input (list) = for userinput of input_detail
        Return:
            None
        """
        mock_args = ["ritika","patel","vijay nagar","indore","m.p.","454665","9802346541"]
        mocked_input.side_effect = mock_args
        result=Address_Book().input_detail()
        self.assertEqual(result,("ritika","patel","vijay nagar","indore","m.p.","454665","9802346541"))
        self.assertNotEqual(result,("ritika","patel","vijay nagar","indore","m.p.","454665","9802346576"))
        self.assertIsNotNone(result)
    
    @patch('builtins.input')
    #@patch('Addressbook.Address_Book.contact_exist', return_value='1')    
    def test_contact_exist(self,mocked_input):
        """
        Description:
            This method define for test case all of contact_exist function of AddressBook.py code
        Parameter:
            mocked_input (list) = for userinput of contact_exist function
        Return:
            None
        """
        mock_args = ["ritika","patel","vijay nagar","indore","m.p.","454665","9802346541"]
        mocked_input.side_effect = mock_args
        result=Address_Book().contact_exist()
        self.assertEqual(result,(True, {"first_name": "ritika","last_name": "patel","address": "vijay nagar","city": "indore","state": "m.p.","zip": "454665","phone_number": "9802346541"
        }))
    
    @patch('builtins.input')
    def test_add_detail(self,mocked_input):
        """
        Description:
            This method define for test case all of add_detail function of AddressBook.py code
        Parameter:
            mocked_input (list) = for userinput of add_detail function
        Return:
            None
        """
        mock_args = ["ritika","patel","vijay nagar","indore","m.p.","454644","9802306541"]
        mocked_input.side_effect = mock_args
        result=Address_Book().add_detail()
        self.assertIsNone(result)
        self.assertNotEqual(result,1)
        self.assertEqual(result,None)
    
    @patch('builtins.input')
    def test_search_detail(self,mocked_input):
        """
        Description:
            This method define for test case all of search_detail function of AddressBook.py code
        Parameter:
            mocked_input (list) = for userinput of search_detail
        Return:
            None
        """
        mock_args = [1,"patidar"]
        mocked_input.side_effect = mock_args
        result=Address_Book().search_detail()
        self.assertIsNone(result)
        self.assertNotEqual(result,1)
        self.assertEqual(result,None)

    @patch('builtins.input')
    def test_delete_person(self,mocked_input):
        """
        Description:
            This method define for test case all of delete function of AddressBook.py code
        Parameter:
            mocked_input (list) = for userinput of delete_person function
        Return:
            None
        """
        mock_args = ["ritika","patel","vijay nagar","indore","m.p.","454644","9802306541"]
        mocked_input.side_effect = mock_args
        result=Address_Book().delete_person()
        self.assertIsNone(result)
        self.assertNotEqual(result,1)
        self.assertEqual(result,None)

    @patch('builtins.input')
    def test_update_detail(self,mocked_input):
        """
        Description:
            This method define for test case all of update_detail function of AddressBook.py code
        Parameter:
            mocked_input (list) = for userinput of update_detail
        Return:
            None
        """
        mock_args = ["ritika","patel","vijay nagar","indore","m.p.","454644","9802306541",0,"ritu"]
        mocked_input.side_effect = mock_args
        result=Address_Book().update_detail()
        self.assertIsNone(result)
        self.assertNotEqual(result,1)
        self.assertEqual(result,None)




if __name__ == '__main__':
    unittest.main()