'''
 @Author: Ritika Patidar
 @Date: 2021-03-01 18:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-03-01 18:15:38  
 @Title : test all the test case of doctor.py file
'''
import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('../Clinique_Management_Programme/code/main'))
from doctor import doctor_management
import json_operation

class DoctorTestCase(unittest.TestCase):
    """
    Description:
        This class define for test all case of methods of doctor.py file
    """
    def setUp(self):
        self.data_doctor=json_operation.load_data_doctor()
        self.data_appointent=json_operation.load_data_appoitment
    def test_doctor_search(self):
        """
        Description:
            This method define for test all case of doctor_search method of doctor.py file
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(doctor_management().doctor_search("name","dipali"),(True, ['dipali'])) 
        self.assertEqual(doctor_management().doctor_search("id","1139"),(True, ['dipali']))
        self.assertIsNotNone(doctor_management().doctor_search("name","dipali"))
        self.assertRaises(KeyError,doctor_management().doctor_search,"duty","dipali")
        self.assertRaises(TypeError,doctor_management().doctor_search,"name")
        self.assertNotEqual(doctor_management().doctor_search("id","1039"),(True, ['dipali']))
        self.assertEqual(doctor_management().doctor_search("id","1039"),(False, 0))

    def test_take_appointment(self):
        """
        Description:
            This method define for test all case of take_appointment method of doctor.py file
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(doctor_management().take_appointment("dipali"),False) 
        self.assertNotEqual(doctor_management().take_appointment("aastha"),True)
        self.assertRaises(TypeError,doctor_management().take_appointment)
        self.assertIsNotNone(doctor_management().take_appointment("dipali"))

    def test_popular_doctor(self):
        """
        Description:
            This method define for test all case of popular_doctor method of doctor.py file
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(doctor_management().popular_doctor(),True) 
        self.assertNotEqual(doctor_management().popular_doctor(),False)
        self.assertIsNotNone(doctor_management().popular_doctor())

    def test_popular_specialization(self):
        """
        Description:
            This method define for test all case of popular_specialization method of doctor.py file
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(doctor_management().popular_specialization(),True) 
        self.assertNotEqual(doctor_management().popular_specialization(),False)
        self.assertIsNotNone(doctor_management().popular_specialization())

    def test_show_appointment(self):
        """
        Description:
            This method define for test all case of show_appointment method of doctor.py file
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(doctor_management().show_appointment(),True) 
        self.assertNotEqual(doctor_management().show_appointment(),False)
        self.assertIsNotNone(doctor_management().show_appointment())


if __name__ == '__main__':
    unittest.main()