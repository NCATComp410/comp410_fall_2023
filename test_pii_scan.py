import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestPIIScan(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_show_supported(self):
        """Test to make sure the default supported entities are returned"""
        results = analyze_text('', show_supported=True)
        self.assertIn('PERSON', str(results))

    def test_uuid(self):
        """Test to make sure a valid UUID is detected"""
        # Test to make sure the recognizer supports UUID
        results = analyze_text('', show_supported=True)
        self.assertIn('UUID', str(results))

        results = analyze_text('This is a UUID: 123e4567-e89b-12d3-a456-42665234000c')
        self.assertIn('UUID', str(results))

        # test some uppercase letters
        results = analyze_text('This is a UUID: 123E4567-e89B-12d3-a456-4266523400FF')
        self.assertIn('UUID', str(results))

        # test an invalid UUID for detection
        results = analyze_text('This is not a UUID: 123e4567-e89b-12d3-a456-42665234000')
        self.assertNotIn('UUID', str(results))
