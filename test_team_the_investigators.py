import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTheInvestigators(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())


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

    def test_place_of_birth_detect(self):
        """Test to make sure the place of birth is detected"""
        #positive test
        test_str = 'I was born in College Station, Texas.'
        results = analyze_text(test_str)
        self.assertIn('LOCATION', str(results))
        # expect POB to be detected
        self.assertIn('POB', str(results))

        #negative test
        test_str = 'I live in College Station, Texas.'
        results = analyze_text(test_str)
        self.assertIn('LOCATION', str(results))
        # expect POB to be detected
        self.assertNotIn('POB', str(results))