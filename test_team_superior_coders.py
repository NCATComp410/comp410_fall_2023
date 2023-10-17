import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_ipv4_address(self):
        """Test to make sure ipv4 address id detected"""

        # positive test case
        results = analyze_text('My IP address is 123.123.123.123')
        print(results)
        self.assertIn('IP_ADDRESS', str(results))

        # negative test case
        results = analyze_text('My IP address is 123.123.23')
        print(results)
        self.assertNotIn('IP_ADDRESS', str(results))
