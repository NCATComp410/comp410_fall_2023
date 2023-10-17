import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_ipv4_address(self):
        """Test to make sure ipv4 address id detected"""

        # positive test case
        results = analyze_text('My IP address is 123.123.123.123')
        print(results)
        self.assertIn('IP_ADDRESS', str(results))

        # negative test case
        results = analyze_text('My IP address is 123.123.23')
        print(results)
        self.assertNotIn('IP_ADDRESS', str(results))

    def test_student_id_detect(self):
        """Test to show if a student ID is detected"""

        #positive test case
        result = analyze_text('my student ID is: 926491673')
        print(result)
        self.assertIn('STUDENT_ID', str(result))

        #positive test case
        result = analyze_text('my student ID is: 123456789')
        print(result)
        self.assertIn('STUDENT_ID', str(result))

        #negative test case
        result = analyze_text('my student ID is: 92649')
        print(result)
        self.assertNotIn('STUDENT_ID', str(result))

    def test_passport_number_detect(self):
        """Test to show if a passport number is detected"""

        #positive test case
        result = analyze_text('my passport number is: 123456789')
        print(result)
        self.assertIn('US_PASSPORT', str(result))

        #positive test case
        result = analyze_text('my passport number is: 345627440')
        print(result)
        self.assertIn('US_PASSPORT', str(result))

        #negative test case
        result = analyze_text('my passport number is: 12345678')
        print(result)
        self.assertNotIn('US_PASSPORT', str(result))

        #negative test case
        result = analyze_text('my passport number is: 12345678AG1')
        print(result)
        self.assertNotIn('US_PASSPORT', str(result))

