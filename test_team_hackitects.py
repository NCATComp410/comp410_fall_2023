import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_marital_status_detect(self):
        """Testing for Marital Status"""
        
        # Positive Test Cases - 1
        results = analyze_text('Marital Status - Married')
        print(results)
        self.assertIn('MARITAL_STATUS', str(results))
        
        # Positive Test Cases - 2
        results = analyze_text('Marital Status - Divorced')
        print(results)
        self.assertIn('MARITAL_STATUS', str(results))

        # Negative Test Case
        results = analyze_text('Marital Status - M@rried!')
        print(results)
        self.assertNotIn('MARITAL_STATUS', str(results))
