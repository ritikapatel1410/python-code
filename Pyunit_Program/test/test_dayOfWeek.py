'''
 @Author: Ritika Patidar
 @Date: 2021-02-16 14:45:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-16 9:05:10  
 @Title : Test case of Day of Week problem
'''
import unittest
import sys
sys.path.insert(0, '/home/patidar/Desktop/GitHub_code/Pyunit_Program/python-code/Pyunit_Program/main')
import day_Of_Week

class Test_DayOfWeek(unittest.TestCase):

    def test_month_day_year(self):
        self.assertEqual(day_Of_Week.dayOfWeek(2,1,2021),1)
        self.assertEqual(day_Of_Week.dayOfWeek(2,16,2021),2)
        self.assertEqual(day_Of_Week.dayOfWeek(2,23,2021),2)
        self.assertEqual(day_Of_Week.dayOfWeek(12,5,2020),6)
        self.assertEqual(day_Of_Week.dayOfWeek(8,29,2021),1)

if __name__ == "__main__":
    unittest.main()