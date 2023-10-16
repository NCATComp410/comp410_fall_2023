import unittest
from pii_scan import analyze_text, show_aggie_pride

class TestTeamSci(unittest.TestCase):

    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_itin_detect(self):
        """Test to make sure ITIN (US_ITIN) is detected"""

        # Positive Testcase with a valid ITIN
        results = analyze_text('My ITIN is 900701234')
        print(results)
        self.assertIn('US_ITIN', str(results))

        # Positive Testcase with another valid ITIN
        results = analyze_text('My ITIN is 9XX-71-5678')
        print(results)
        self.assertNotIn('US_ITIN', str(results))

        # Negative Testcase with a string that does not contain an ITIN
        results = analyze_text('My ITIN is 789-01-2345')
        print(results)
        self.assertNotIn('US_ITIN', str(results))

        # Negative Testcase with a string that does not contain an ITIN
        results = analyze_text('My ITIN is 124143536')
        print(results)
        self.assertNotIn('US_ITIN', str(results))
=======
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

