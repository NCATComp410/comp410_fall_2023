import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamTechniGALS(unittest.TestCase):
    def test_gender_detect(self):
        """Test to make sure gender is detected"""

        # positive test cases
        results = analyze_text('my gender is female')
        print(results)
        self.assertIn('GENDER', str(results))

        results = analyze_text('my gender is male')
        print(results)
        self.assertIn('GENDER', str(results))

        results = analyze_text('my gender is non-binary')
        print(results)
        self.assertIn('GENDER', str(results))

        # negative test case
        results = analyze_text('my gender is november')
        print(results)
        self.assertNotIn('GENDER', str(results))

    def test_zipcode(self):
        """Test to find zipcode of user"""
        #positive testcase
        results = analyze_text('my zipcode is: 27401')
        print(results)
        self.assertIn('ZIPCODE', str(results))

        #positive testcase
        results = analyze_text('30135')
        print(results)
        self.assertIn('ZIPCODE', str(results))


        #negative testcase
        results = analyze_text('274001')
        print(results)
        self.assertNotIn('ZIPCODE', str(results))

