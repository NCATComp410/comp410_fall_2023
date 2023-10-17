import unittest
import re
from pii_scan import show_aggie_pride, analyze_text


class TestTeamTechniGALS(unittest.TestCase):   
    def test_detect_usernames(self):
        # Test a valid username
        valid_result = analyze_text('@comp410Rocks')
        self.assertIn("USERNAME", str(valid_result), "Valid username not detected")

        # Test an invalid organization
        invalid_result = analyze_text('John Smith')
        self.assertNotIn("USERNAME", str(invalid_result), "Invalid organization incorrectly detected")
