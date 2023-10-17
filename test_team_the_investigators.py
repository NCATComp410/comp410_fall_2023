import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTheInvestigators(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

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