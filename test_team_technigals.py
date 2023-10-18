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
        self.assertIn('BANKACC', str(results))

        results = analyze_text('my bank account number is: 12345678910')
        print(results)
        self.assertNotIn('BANKACC', str(results))

