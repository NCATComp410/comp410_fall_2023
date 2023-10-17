import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamSci(unittest.TestCase):
    # def test_aggie_pride(self):
    #     """Test to make sure the Aggie Pride function works"""
    #     self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_credit_card_detect(self):
        """Test to make sure the credit card number is detected"""

        # Positive Testcase
        results = analyze_text('My credit card number is 6011 8064 2259 3800')
        print(results)
        self.assertIn('CREDIT_CARD', str(results))

        # Positive Testcase
        results = analyze_text('My credit card number is 6011-4432-9423-6878')
        print(results)
        self.assertIn('CREDIT_CARD', str(results))

        # Positive Testcase
        results = analyze_text('My credit card number is 4024007142881399')
        print(results)
        self.assertIn('CREDIT_CARD', str(results))

        # Positive Testcase
        results = analyze_text('My credit card number is 5327682836838904')
        print(results)
        self.assertIn('CREDIT_CARD', str(results))

        # Negative Testcase
        results = analyze_text('My credit card number is 1234-5678-9012-3456')
        print(results)
        self.assertNotIn('CREDIT_CARD', str(results))

        # Negative Testcase
        results = analyze_text('My credit card number is 0000-0000-0000-0000')
        print(results)
        self.assertNotIn('CREDIT_CARD', str(results))

        # Negative Testcase
        results = analyze_text('My credit card number is 1111111111111111')
        print(results)
        self.assertNotIn('CREDIT_CARD', str(results))
