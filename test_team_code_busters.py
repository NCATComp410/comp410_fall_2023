import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_eye_color_detect(self):
        '''Testing if eye color is detected'''

        #positive test case
        results = analyze_text('Eye color: red')
        print(results)
        self.assertIn('EYE_COLOR', str(results))

        #negative test case
        results = analyze_text('Eye color: Ball')
        print(results)
        self.assertNotIn('EYE_COLOR', str(results))
