import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_marital_status_detect(self):
        """Testing for Marital Status"""
        # Positive Test Cases - 1
        results = analyze_text('Married')
        print(results)
        self.assertIn('MARITAL_STATUS', str(results))
        self.assertIn('Married', str(results))
        self.assertIn('married', str(results))
        
        # Positive Test Cases - 2
        results = analyze_text('Divorced')
        print(results)
        self.assertIn('MARITAL_STATUS', str(results))
        self.assertIn('Divorced', str(results))
        self.assertIn('divorced', str(results))

        # Negative Test Case
        results = analyze_text('M@rried!')
        print(results)
        self.assertNotIn('MARITAL_STATUS', str(results))
