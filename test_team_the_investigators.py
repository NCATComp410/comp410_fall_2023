import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTheInvestigators(unittest.TestCase):
    
    def test_credit_card_detect(self):
        """Test to see if Amex credit card is detected"""

        # Positive Testcase
        results = analyze_text('My Amex credit card number is 3400 000000 00009')
        print(results)
        self.assertIn('CREDIT_CARD', str(results))

        # Positive Testcase
        results = analyze_text('My Amex credit card number is 4400 000000 00009')
        print(results)
        self.assertNotIn('CREDIT_CARD', str(results))
