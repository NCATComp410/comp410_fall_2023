import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())
    
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
