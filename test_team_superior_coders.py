import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_student_id_detect(self):
        """Test to show if a student ID is detected"""

        #positive test case
        result = analyze_text('my student ID is: 123456789')
        print(result)
        self.assertIn('STUDENT_ID', str(result))

        #negative test case
        result = analyze_text('my student ID is: 92649')
        print(result)
        self.assertNotIn('STUDENT_ID', str(result))

    def test_american_phone_number_detect(self):
        """Test to ensure an American Phone Number is detected"""

        #positive test case
        result = analyze_text('My phone number is 1-(199)-555-9461')
        print(result)
        self.assertIn('AMERICAN_PHONE_NUMBER', str(result))
        
        #positive test case
        result = analyze_text('My phone number is 1-(121)-555-2962')
        print(result)
        self.assertIn('AMERICAN_PHONE_NUMBER', str(result))

        #positive test case
        result = analyze_text('My phone number is 1.121.555.2962')
        print(result)
        self.assertIn('AMERICAN_PHONE_NUMBER', str(result))

        #positive test case
        result = analyze_text('My phone number is 11215552962')
        print(result)
        self.assertIn('AMERICAN_PHONE_NUMBER', str(result))

        #positive test case
        result = analyze_text('My phone number is 1-121-555-2962')
        print(result)
        self.assertIn('AMERICAN_PHONE_NUMBER', str(result))

        #negetive test case
        result = analyze_text('My phone number is -9461')
        print(result)
        self.assertNotIn('AMERICAN_PHONE_NUMBER', str(result))

        #negetive test case
        result = analyze_text('My phone number is -120-555-9461')
        print(result)
        self.assertNotIn('AMERICAN_PHONE_NUMBER', str(result))

        #negetive test case
        result = analyze_text('My phone number is 555-9461')
        print(result)
        self.assertNotIn('AMERICAN_PHONE_NUMBER', str(result))


