import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamNull(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_au_medicare(self):
        """Test to make sure AU_MEDICARE works"""
        # https://stackoverflow.com/questions/3589345/how-do-i-validate-an-australian-medicare-number
        results = analyze_text('2123 45670 1')
        print(results)
        self.assertIn('AU_MEDICARE', str(results))

    def test_ssn_detection(self):
        """Test to make sure SSN is detected"""
        results = analyze_text('My SSN is 123-45-6789')
        print(results)
        self.assertIn('US_SSN', str(results))

        results = analyze_text('My SSN is 123-00-1234')
        print(results)
        self.assertIn('US_SSN', str(results))

        # negative testcase - should not detect a SSN
        results = analyze_text('My SSN is 123-45-678')
        print(results)
        self.assertNotIn('US_SSN', str(results))

    def test_crypto_wallet_detect(self):
        """Test to make sure crypto wallet is detected"""
        # positive testcase
        results = analyze_text('my wallet address is: 16Yeky6GMjeNkAiNcBY7ZhrLoMSgg1BoyZ')
        print(results)
        self.assertIn('CRYPTO', str(results))

        # negative testcase
        results = analyze_text('my wallet address is: 16Yeky6GMjeNkAiNcBY7ZhrLoMSgg1')
        print(results)
        self.assertNotIn('CRYPTO', str(results))

    def test_medical_license(self):
        """Tests to make sure a potential license is detected"""
        # positive test case
        results = analyze_text('my certificate number is: BB1388568')
        self.assertIn('MEDICAL_LICENSE', str(results))

        # negative test case
        results = analyze_text('my certificate number is: BB18568')
        self.assertNotIn('MEDICAL_LICENSE', str(results))

    def test_merge_1(self):
        """This test will create a merge conflict"""
        self.assertEqual(1+1, 2)
        self.assertNotEqual('This', 'That')
       
    def test_merge_2(self):
        """This is the second part of the merge conflict example"""
        # this is merge_2 test
        self.assertEqual('Merge2', "Merge2")
        self.assertNotEqual('Merge2', 'Merge1')
       