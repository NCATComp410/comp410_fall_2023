import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamNull(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_ssn_detection(self):
        """Test to make sure SSN is detected"""
        results = analyze_text('My SSN is 123-45-6789')
        print(results)
        self.assertIn('US_SSN', str(results))

        results = analyze_text('My SSN is 123-00-1234')
        print(results)
        self.assertIn('US_SSN', str(results))

        # negative testcase - should not detect a SSN
        results = analyze_text('My SSN is 123-45-678')
        print(results)
        self.assertNotIn('US_SSN', str(results))
