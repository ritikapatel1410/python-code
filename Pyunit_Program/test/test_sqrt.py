'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 22:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 22:30:38  
 @Title : Test case for Computes the square root of a nonnegative number using Newton's method
'''
import unittest
import sys
sys.path.insert(0, '/home/patidar/Desktop/GitHub_code/Pyunit_Program/python-code/Pyunit_Program/main')
import sqrt

class Test_sqrt(unittest.TestCase):
    def test_toBinary(self):
        self.assertEqual(sqrt.sqrt(15),3.873)
        self.assertEqual(sqrt.sqrt(3),1.732)
        self.assertRaises(ZeroDivisionError,sqrt.sqrt,-1)
        self.assertRaises(TypeError,sqrt.sqrt,"a")
if __name__ == '__main__':
    unittest.main()