'''
 @Author: Ritika Patidar
 @Date: 2021-02-14 17:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-14 8:40:38  
 @Title : Test case of vending machine problem
'''
import unittest
import sys
sys.path.insert(0, '/home/patidar/Desktop/pyunit-programs/main')
import vending_machine


class Test_vending_machine(unittest.TestCase):
    def test_VM(self):
        total_change=[1000,500,100,50,10,5,2,1]
        return_money=dict()
        self.assertEqual(vending_machine.vending_machine(100,total_change,return_money),{100:1})
        self.assertEqual(vending_machine.vending_machine(5300,total_change,return_money),{1000:5, 100:3})
if __name__ == '__main__':
    unittest.main()