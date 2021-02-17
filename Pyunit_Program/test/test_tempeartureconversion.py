'''
 @Author: Ritika Patidar
 @Date: 2021-02-15 19:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-15 19:30:38  
 @Title : Test case of Temperature conversion problem
'''
import unittest
import sys
sys.path.insert(0, '/home/patidar/Desktop/pyunit-programs/main')
import temperatureconversion
class Test_temperatureconversion(unittest.TestCase):
    def test_celcius(self):
        self.assertEqual(temperatureconversion.Temp_conv(50).celsius(),10.000)
        self.assertEqual(temperatureconversion.Temp_conv(-10).celsius(),-23.333)
    def test_fer(self):
        self.assertEqual(temperatureconversion.Temp_conv(32).fahrenheit(),89.6)
        self.assertEqual(temperatureconversion.Temp_conv(100).fahrenheit(),212.0)
if __name__ == '__main__':
    unittest.main()