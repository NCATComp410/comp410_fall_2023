import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamNull(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_au_medicare(self):
        """Test to make sure AU_MEDICARE works"""
        # https://stackoverflow.com/questions/3589345/how-do-i-validate-an-australian-medicare-number
        results = analyze_text('2123 45670 1')
        print(results)
        self.assertIn('AU_MEDICARE', str(results))
