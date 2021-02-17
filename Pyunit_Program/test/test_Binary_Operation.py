'''
 @Author: Ritika Patidar
 @Date: 2021-02-16 15:50:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-16 15:50:10  
 @Title : Test cases for Binary operation problem
'''
import unittest
import sys
sys.path.insert(0, '/home/patidar/Desktop/pyunit-programs/main')
from Binary_operation import Binary_operation
class Test_Binary_operation(unittest.TestCase):
    def test_Binary_operation(self):
        self.assertEqual(Binary_operation(70),(100,False))
        self.assertEqual(Binary_operation(300),(4290,False))
        self.assertEqual(Binary_operation(8),(128,True))
        self.assertRaises(TypeError,Binary_operation,"char")
        self.assertRaises(TypeError,Binary_operation,0.123)

if __name__ == '__main__':
    unittest.main()