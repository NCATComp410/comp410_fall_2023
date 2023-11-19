import unittest
import re
import os
from pii_scan import show_aggie_pride, analyze_text


class TestPIIScan(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_show_supported(self):
        """Test to make sure the default supported entities are returned"""
        results = analyze_text('', show_supported=True)
        self.assertIn('PERSON', str(results))

    def test_uuid(self):
        """Test to make sure a valid UUID is detected"""
        # Test to make sure the recognizer supports UUID
        results = analyze_text('', show_supported=True)
        self.assertIn('UUID', str(results))

        results = analyze_text('This is a UUID: 123e4567-e89b-12d3-a456-42665234000c')
        self.assertIn('UUID', str(results))

        # test some uppercase letters
        results = analyze_text('This is a UUID: 123E4567-e89B-12d3-a456-4266523400FF')
        self.assertIn('UUID', str(results))

        # test an invalid UUID for detection
        results = analyze_text('This is not a UUID: 123e4567-e89b-12d3-a456-42665234000')
        self.assertNotIn('UUID', str(results))

    def test_base_supported_entities(self):
        """Test to make sure the default supported entities are returned"""
        results = analyze_text('', show_supported=True)
        print(results)
        supported_entities = ['IP_ADDRESS',
                              'MEDICAL_LICENSE',
                              'LOCATION',
                              'EMAIL_ADDRESS',
                              'DATE_TIME',
                              'CREDIT_CARD',
                              'CRYPTO',
                              'AU_MEDICARE',
                              'AU_ABN',
                              'PHONE_NUMBER',
                              'US_PASSPORT',
                              'IBAN_CODE',
                              'AU_TFN',
                              'US_BANK_NUMBER',
                              'NRP',
                              'UK_NHS',
                              'US_SSN',
                              'SG_NRIC_FIN',
                              'PERSON',
                              'URL',
                              'US_ITIN',
                              'UUID',
                              'US_DRIVER_LICENSE',
                              'AU_ACN',
                              'STUDENT_ID',
                              'USERNAME',
                              'INMATE'
                              ]
        for entity in supported_entities:
            self.assertIn(entity, results)

    def test_starts_with_test(self):
        """Test to make sure all test methods start with test"""
        # In order to run as a test case the method name must start with test
        # This test checks to make sure all defines within test files start with test
        # This is a common mistake that can cause tests to be skipped
        for file in os.listdir('.'):
            if file.endswith('.py') and file.startswith('test_'):
                with open(file) as f:
                    for line in f:
                        # make sure everything that looks like a method name starts with test
                        m = re.search(r'\s*def (\w+)', line)
                        if m:
                            self.assertTrue(m.group(1).startswith('test'),
                                            'Method name does not start with test: def ' + m.group(1) + ' in ' + file)


if __name__ == '__main__':
    unittest.main()
