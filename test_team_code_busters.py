import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamCodeBusters(unittest.TestCase):
      
    def test_birthdate_detect(self):
        #Positive test case

        results = analyze_text(" My birthdate: 11/01/2002")
        print(results)
        self.assertIn('DATE_TIME', str(results))

        #Negative test case
        results = analyze_text(" My birthdate: ABC/de/frog.")
        print(results)
        self.assertNotIn('DATE_TIME', str(results))