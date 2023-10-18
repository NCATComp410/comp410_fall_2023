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

    def  test_credit_card_score_detect(self):
        """Test to make sure credit score is detected"""
        # positive testcase
        results = analyze_text('my current credit score is: 450')
        print(results)
        self.assertIn('CREDIT_CARD', str(results))

        # negative testcase
        results = analyze_text('my current credit score is: 250')
        print(results)
        self.assertNotIn('CREDIT_CARD', str(results)) 

        # negative testcase
        results = analyze_text('my current credit score is: 851')
        print(results)
        self.assertNotIn('CREDIT_CARD', str(results)) 

    def test_eye_color_detect(self):
        """Testing if eye color is detected"""
        #positive test case
        results = analyze_text('Eye color: red')
        print(results)
        self.assertIn('EYE_COLOR', str(results))

        #negative test case
        results = analyze_text('Eye color: Ball')
        print(results)
        self.assertNotIn('EYE_COLOR', str(results))
