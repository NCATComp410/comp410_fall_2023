import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_birthdate_detect(self):
        #Positive test case
        results = analyze_text(" My birthdate: 11/01/2002")
        print(results)
        self.assertIn('birthdate', str(results))

        #Negative test case
        results = analyze_text(" My birthdate: ABC/de/frog.")
        print(results)
        self.assertNotIn('birthdate', str(results))

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

