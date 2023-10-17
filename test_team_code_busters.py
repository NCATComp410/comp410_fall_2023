import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_health_insurance_policy_number_detect(self):
        """Test to ensure policy number is detected"""
        #positive testcase
        results = analyze_text('My insurance policy number is XYZ123456789')
        print(results)
        self.assertIn('US_DRIVER_LICENSE', str(results))

        #negative testcase
        results = analyze_text('My insurance policy number is ABC123456789011')
        print(results)
        self.assertNotIn('US_DRIVER_LICENSE', str(results))

        #negative testcase
        results = analyze_text('My insurance policy number is ABCDE12345678')
        print(results)
        self.assertNotIn('US_DRIVER_LICENSE', str(results))
