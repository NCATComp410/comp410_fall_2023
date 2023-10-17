import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_udid(self):
        '''Testing if UDID is detected'''

        # positive test case
        results = analyze_text('A7C9B2A4-F6E82B43C580E24F')
        print(results)
        self.assertIn('UDID', str(results))

        # negative test case
        results = analyze_text('K7Y9J2A4-R6T8X1')
        print(results)
        self.assertNotIn('UDID', str(results))
