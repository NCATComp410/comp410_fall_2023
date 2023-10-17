import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamTechniGALS(unittest.TestCase):
    
    def test_bank_account_number(self):
        """Test to find bank account number"""
        results = analyze_text('my bank account number is: 1234567890')
        print(results)
        self.assertIn('BANKACC', str(results))

        results = analyze_text('my bank account number is: 12345678910')
        print(results)
        self.assertNotIn('BANKACC', str(results))
        
