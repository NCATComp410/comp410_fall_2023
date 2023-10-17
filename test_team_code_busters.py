import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_philisophical_belief_detect(self):
        #positive test case
        results = analyze_text("marxism")
        print(results)
        self.assertIn('PHILBELIEFS', str(results))

        #negative test case
        results = analyze_text("christian")
        print(results)
        self.assertNotIn('PHILBELIEFS', str(results))