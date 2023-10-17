import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_health_insurance_policy_number_detect(self):
        """Test to ensure policy number is detected"""
        #positive testcase
        """Insurance Policy number should begin with 3 letters followed by 9 numbers"""
        results = analyze_text('My insurance policy number is XYZ123456789')
        print(results)
        self.assertIn('MEDICAL_LICENSE', str(results))

        #negative testcase
        results = analyze_text('My insurance policy number is AB1234567890')
        """This policy ID is incorrect because it has 2 Letters and 10 Numbers"""
        print(results)
        self.assertNotIn('MEDICAL_LICENSE', str(results))

        #negative testcase
        results = analyze_text('My insurance policy number is ABCD12345678')
        """This policy ID is incorrect because it contains 4 Letters and 8 Numbers"""
        print(results)
        self.assertNotIn('MEDICAL_LICENSE', str(results))