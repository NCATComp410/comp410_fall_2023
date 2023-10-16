import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_Interests(self):
        """Test to make sure the Aggie Pride function works"""
        
        results = analyze_text('I like Ice Cream')
        self.assertIn('INTEREST', str(results))

        results = analyze_text('I love Bitches')
        self.assertIn('INTEREST', str(results))

        results = analyze_text('My name is Caleb')
        self.assertNotIn('INTEREST', str(results))