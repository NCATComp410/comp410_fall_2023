import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_marital_status_detect(self):
        """Testing for Marital Status"""
        # Positive Test Cases - 1
        self.assertEqual("3","3")
        results = analyze_text('We are married!')
        print(results)
        self.assertIn('MARITALSTATS', str(results))

               # # Positive Test Cases - 2
        results = analyze_text('divorced')
        print(results)
        self.assertIn('MARITALSTATS', str(results))
        # self.assertIn('Divorced', str(results))
        # self.assertIn('divorced', str(results))

        # # Negative Test Case
        results = analyze_text('M@rried!')
        print(results)
        self.assertNotIn('MARITAL_STATUS', str(results))
        
    def test_Interests(self):
        """Test to make sure the Aggie Pride function works"""
        
        results = analyze_text('I like Bibleman, but I do not like Chris Chan')
        self.assertIn('INTEREST', str(results))

        results = analyze_text('I love Bitches.')
        self.assertIn('INTEREST', str(results))

        results = analyze_text('I don\'t like Mondays')
        self.assertNotIn('INTEREST', str(results))
        
