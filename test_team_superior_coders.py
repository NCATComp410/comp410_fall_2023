import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())
    
    def test_political_standings(self):
        """ Test to make sure political standing is detected"""
        # positive testcase
        results = analyze_text("I am a republican")
        print(results)
        self.assertIn('NPR', str(results))
        # negative testcase
        results = analyze_text("I am a neutral supporter")
        print(results)
        self.assertNotIn('NPR', str(results))

    def test_student_id_detect(self):
        """Test to show if a student ID is detected"""

        # positive test case
        result = analyze_text('my student ID is: 926491673')
        print(result)
        self.assertIn('STUDENT_ID', str(result))

        # positive test case
        result = analyze_text('my student ID is: 123456789')
        print(result)
        self.assertIn('STUDENT_ID', str(result))

        # negative test case
        result = analyze_text('my student ID is: 92649')
        print(result)
        self.assertNotIn('STUDENT_ID', str(result))

    def test_passport_number_detect(self):
        """Test to show if a passport number is detected"""

        # positive test case
        result = analyze_text('my passport number is: 123456789')
        print(result)
        self.assertIn('US_PASSPORT', str(result))

        # positive test case
        result = analyze_text('my passport number is: 345627440')
        print(result)
        self.assertIn('US_PASSPORT', str(result))

        # negative test case
        result = analyze_text('my passport number is: 12345678')
        print(result)
        self.assertNotIn('US_PASSPORT', str(result))

        # negative test case
        result = analyze_text('my passport number is: 12345678AG1')
        print(result)
        self.assertNotIn('US_PASSPORT', str(result))

    def test_ipv4_address(self):
        """Test to show if a ipv4 address is detected"""

        # positive test case
        result = analyze_text('My ip address is: 123.123.45.233')
        print(result)
        self.assertIn('IP_ADDRESS', str(result))

        # negative test case
        result = analyze_text('My ip address is: 123.123')
        print(result)
        self.assertNotIn('IP_ADDRESS', str(result))

    def test_detect_race(self):
        """Test to make sure race is detected properly"""
        # Positive Test Case
        result = analyze_text('I am African American')
        print(result)
        self.assertIn('RACE', str(result))

        # Positive Test Case
        result = analyze_text('I am Native American')
        print(result)
        self.assertIn('RACE', str(result))

        # Positive Test Case
        result = analyze_text('I am Black')
        print(result)
        self.assertIn('RACE', str(result))

        # Negative Test Case
        result = analyze_text('I am brown')
        print(result)
        self.assertNotIn('RACE', str(result))
