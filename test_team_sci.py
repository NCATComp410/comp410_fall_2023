import unittest
from pii_scan import analyze_text, show_aggie_pride

class TestTeamSci(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_itin_detect(self):
        """Test to make sure ITIN (US_ITIN) is detected"""

        # Positive Testcase with a valid ITIN
        results = analyze_text('My ITIN is 123-45-6789')
        print(results)
        self.assertIn('US_ITIN', str(results))

        # Positive Testcase with another valid ITIN
        results = analyze_text('My ITIN is 456-78-9012')
        print(results)
        self.assertIn('US_ITIN', str(results))

        # Negative Testcase with a string that does not contain an ITIN
        results = analyze_text('My phone number is 789-01-2345')
        print(results)
        self.assertNotIn('US_ITIN', str(results))

        # Negative Testcase with a string that does not contain an ITIN
        results = analyze_text('My ITIN is 124143536')
        print(results)
        self.assertNotIn('US_ITIN', str(results))