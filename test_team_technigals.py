import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamTechniGALS(unittest.TestCase):
    def test_gender_detect(self):
        """Test to make sure gender is detected"""

        # positive test cases
        results = analyze_text('my gender is female')
        print(results)
        self.assertIn('GENDER', str(results))

        results = analyze_text('my gender is male')
        print(results)
        self.assertIn('GENDER', str(results))

        results = analyze_text('my gender is non-binary')
        print(results)
        self.assertIn('GENDER', str(results))

        # negative test case
        results = analyze_text('my gender is november')
        print(results)
        self.assertNotIn('GENDER', str(results))

    def test_bank_account_number(self):
        """Test to find bank account number"""
        results = analyze_text('my bank account number is: 1234567890')
        print(results)
        self.assertIn('US_BANK_NUMBER', str(results))

        results = analyze_text('my bank account number is: ABC123')
        print(results)
        self.assertNotIn('US_BANK_NUMBER', str(results))

    def test_int_num_detect(self):
        results = analyze_text('123-123-1234-1234')
        print(results)
        self.assertIn('INTERNATIONAL_PN', str(results))

        results = analyze_text('123-123-1234-123')
        print(results)
        self.assertNotIn('INTERNATIONAL_PN', str(results))

        results = analyze_text('1231231234123')
        print(results)
        self.assertNotIn('INTERNATIONAL_PN', str(results))

    def test_detect_usernames(self):
        # Test a valid username
        valid_result = analyze_text('@comp410Rocks')
        self.assertIn("USERNAME", str(valid_result), "Valid username not detected")

        # Test an invalid organization
        invalid_result = analyze_text('John Smith')
        self.assertNotIn("USERNAME", str(invalid_result), "Invalid organization incorrectly detected")
