'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 20:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 20:30:38  
 @Title : Test case of Monthly payment problem
'''
import unittest
import sys
sys.path.insert(0, '/home/patidar/Desktop/GitHub_code/Pyunit_Program/python-code/Pyunit_Program/main')
import Monthlypayment
class Test_Monthlypayment(unittest.TestCase):
    def test_cal(self):
        self.assertEqual(Monthlypayment.Monthlypayment_calulation(1000,10,2),9.201)
        self.assertEqual(Monthlypayment.Monthlypayment_calulation(1500,10,3),14.484)


if __name__ == '__main__':
    unittest.main()