import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTheInvestigators(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_credit_card_detect(self):
        """Test to see if Amex credit card is detected"""

        # Positive Testcase
        results = analyze_text('My Amex credit card number is 3400 000000 00009')
        print(results)
        self.assertIn('CREDIT_CARD', str(results))

        # Negative Testcase
        results = analyze_text('My Amex credit card number is 4400 000000 00009')
        print(results)
        self.assertNotIn('CREDIT_CARD', str(results))

    def test_email_address_detect(self):
        """Test to make sure email address is detected"""
        # positive testcase
        results = analyze_text('my email address is: yadayada@hotmail.com')
        print(results)
        self.assertIn('EMAIL_ADDRESS', str(results))

        # negative testcase
        results = analyze_text('my email address is: yadayadahotmailcom')
        print(results)
        self.assertNotIn('EMAIL_ADDRESS', str(results))

        # test longest possible email address

    def test_place_of_birth_detect(self):
        """Test to make sure the place of birth is detected"""
        # positive test
        test_str = 'I was born in College Station, Texas.'
        results = analyze_text(test_str)
        self.assertIn('LOCATION', str(results))
        # expect POB to be detected
        self.assertIn('POB', str(results))

        # negative test
        test_str = 'I live in College Station, Texas.'
        results = analyze_text(test_str)
        self.assertIn('LOCATION', str(results))
        # expect POB to be detected
        self.assertNotIn('POB', str(results))

    def test_full_names_detect(self):
        """Test to make sure full names are detected"""
        # Positive test case
        results = analyze_text('John William Smith')
        print(results)
        self.assertIn('PERSON', str(results))

        # Negative test case
        results = analyze_text('John@123')
        print(results)
        self.assertNotIn('PERSON', str(results))

    def test_inmate_numbers_detect(self):
        """Test to make sure that the federal inmate numbers are detected"""
        # Positive test case
        results =  analyze_text('My name is Charles Manson and my federal inmate number is 12345-049')
        print(results)
        self.assertIn('INMATE', str(results))
    
        # Negative test case
        results = analyze_text('My name is Harold Martin and my number is 28215-290') 
        print(results)
        self.assertNotIn('INMATE', str(results))

        # Negative test case for number of digits
        results = analyze_text('My name is Harold Martin and my number is 282156-090')
        print(results)
        self.assertNotIn('INMATE', str(results))
