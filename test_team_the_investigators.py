import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTheInvestigators(unittest.TestCase):
   # def test_aggie_pride(self):
     #   """Test to make sure the Aggie Pride function works"""
      #  self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_amex_card_detect(self):
        """Test to make sure the Amex Card is detected"""

        #Postitive Case
        results = analyze_text('My Amex card number is 3711 465932 57302')
        print(results)
        self.assertIn('AMEX_CARD', str(results))

        #Negative Case
        results = analyze_text('My Amex card number is 6011 473832 85948')
        print(results)
        self.assertIn('AMEX_CARD', str(results))

        #Postitive Case
        results = analyze_text('My Amex card number is 3403 129054 39204')
        print(results)
        self.assertIn('AMEX_CARD', str(results))

        #Negative Case
        results = analyze_text('My Amex card number is 3011 4738 3277 8594')
        print(results)
        self.assertIn('AMEX_CARD', str(results))