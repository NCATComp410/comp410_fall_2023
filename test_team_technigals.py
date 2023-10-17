import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamTechniGALS(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_zipcode(self):
        """Test to find zipcode of user"""
        #positive testcase
        results = analyze_text('my zipcode is: 27401')
        print(results)
        self.assertIn('ZIPCODE', str(results))

        #negative testcase
        results = analyze_text('my zipcode is: 274001')
        print(results)
        self.assertIn('ZIPCODE', str(results))
