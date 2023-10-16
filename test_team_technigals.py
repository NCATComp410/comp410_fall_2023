import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamTechniGALS(unittest.TestCase):
    def test_gender_detect(self):
        """Test to make sure gender is detected"""

        # positive test cases
        results = analyze_text('My gender is Female')
        print(results)
        self.assertIn('GENDER', str(results))

        results = analyze_text('My gender is Male')
        print(results)
        self.assertIn('GENDER', str(results))

        results = analyze_text('My gender is Non-Binary')
        print(results)
        self.assertIn('GENDER', str(results))

        # negative test case
        results = analyze_text('My gender is November')
        print(results)
        self.assertNotIn('GENDER', str(results))
