import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())
    
    def test_political_standings(self):
        """ Test to make sure political standing is detected"""
        #positive testcase
        results = analyze_text("I am a republican")
        print(results)
        self.assertIn('NPR', str(results))
        #negative testcase
        results = analyze_text("I am a neutral supporter")
        print(results)
        self.assertNotIn('NPR', str(results))

    def test_student_id_detect(self):
        """Test to show if a student ID is detected"""

        #positive test case
        result = analyze_text('my student ID is: 926491673')
        print(result)
        self.assertIn('STUDENT_ID', str(result))

        #positive test case
        result = analyze_text('my student ID is: 123456789')
        print(result)
        self.assertIn('STUDENT_ID', str(result))

        #negative test case
        result = analyze_text('my student ID is: 92649')
        print(result)
        self.assertNotIn('STUDENT_ID', str(result))


