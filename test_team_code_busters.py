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
        self.assertIn('BIRTHDATE', str(results))

        #Negative test case
        results = analyze_text(" My birthdate: ABC/de/frog.")
        print(results)
        self.assertNotIn('BIRTHDATE', str(results))

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

    def test_udid(self):
        '''Testing if UDID is detected'''

        # positive test case
        results = analyze_text('A7C9B2A4-F6E82B43C580E24F')
        print(results)
        self.assertIn('UDID', str(results))

        # negative test case
        results = analyze_text('K7Y9J2A4-R6T8X1')
        print(results)
        self.assertNotIn('UDID', str(results))

    def test_health_insurance_policy_number_detect(self):
        """Test to ensure policy number is detected"""
        #positive testcase
        results = analyze_text('My insurance policy number is XYZ123456789')
        print(results)
        self.assertIn('US_DRIVER_LICENSE', str(results))

        #negative testcase
        results = analyze_text('My insurance policy number is ABC123456789011')
        print(results)
        self.assertNotIn('US_DRIVER_LICENSE', str(results))

        #negative testcase
        results = analyze_text('My insurance policy number is ABCDE12345678')
        print(results)
        self.assertNotIn('US_DRIVER_LICENSE', str(results))
