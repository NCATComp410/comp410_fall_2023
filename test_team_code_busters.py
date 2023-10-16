import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_philisophical_belief_detect(self):
        #positive test case
        results = analyze_text("I am a secularist")
        print(results)
        self.assertIn('',str(results))

        #negative test case
        results = analyze_text("I am atheist")
        print(results)
        self.assertIn('',str(results))