import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamTechniGALS(unittest.TestCase):

    def test_int_num_detect(self):
        results = analyze_text('123-123-1234-1234')
        print(results)
        self.assertIn('INTERNATIONAL_PN', str(results))

        results = analyze_text('123-123-1234-123')
        print(results)
        self.assertNotIn('INTERNATIONAL_PN', str(results))

        results = analyze_text('1231231234123')
        print(results)
        self.assertNotIn('INTERNATIONAL_PN', str(results))
