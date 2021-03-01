import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('../Clinique_Management_Programme/code/main'))
import doctor
import patient
import json_operation

class PatientTestCase(unittest.TestCase):
    def setUp(self):
        self.data_patient=json_operation.load_data_patient()
    def test_patient(self):
        result=patient.patient_management().patient_search("name","ananya")
        self.assertEqual(result,"detail searched")
        self.assertIsNotNone(result)
        self.assertRaises(KeyError,patient.patient_management().patient_search,"duty","ananya")
        result=patient.patient_management().patient_search("name","ragini")
        self.assertEqual(result,"detail not match")
if __name__ == '__main__':
    unittest.main()