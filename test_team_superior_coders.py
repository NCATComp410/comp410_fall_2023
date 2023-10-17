import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())
    
    def test_political_standings(self):
        """ Test to make sure political standing is detected"""
        #positive testcase
        results = analyze_text("I am a republican")
        print(results)
        self.assertIn('NPR', str(results))
        #negative testcase
        results = analyze_text("I am a neutral supporter")
        print(results)
        self.assertNotIn('NPR', str(results))