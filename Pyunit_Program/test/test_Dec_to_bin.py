'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 23:40:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-16 22:40:10  
 @Title : Test case of Decimal to binary conversion 
'''
import unittest
import sys
sys.path.insert(0, '/home/patidar/Desktop/GitHub_code/Pyunit_Program/python-code/Pyunit_Program/main')
import Dec_to_Bin

class Test_Dec_to_Bin(unittest.TestCase):
    def test_toBinary(self):
        self.assertEqual(Dec_to_Bin.toBinary(100.0),"00000000000000000000000001100100")
        self.assertEqual(Dec_to_Bin.toBinary(0.11),"000000000000000000000000.000111000")
        self.assertRaises(ValueError,Dec_to_Bin.toBinary,100)
        self.assertRaises(ValueError,Dec_to_Bin.toBinary,-1343)
        self.assertRaises(ValueError,Dec_to_Bin.toBinary,"a")
if __name__ == '__main__':
    unittest.main()