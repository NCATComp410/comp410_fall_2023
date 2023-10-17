import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_ncdriversLicense(self):
        #Positive Test Case 1
        res = analyze_text('111111111111')
        self.assertIn('ThorLicenseRec',str(res))


        # Negative test Case because of the dots
        res = analyze_text('1234.5678.9012')
        self.assertNotIn('ThorLicenseRec',str(res))



        #Negative Test Case because it is 13 digits
        res = analyze_text('1234567890123')
        self.assertNotIn('ThorLicenseRec',str(res))




