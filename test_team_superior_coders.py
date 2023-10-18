import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

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



    def test_passport_number_detect(self):
        """Test to show if a passport number is detected"""

        #positive test case
        result = analyze_text('my passport number is: 123456789')
        print(result)
        self.assertIn('US_PASSPORT', str(result))

        #positive test case
        result = analyze_text('my passport number is: 345627440')
        print(result)
        self.assertIn('US_PASSPORT', str(result))

        #negative test case
        result = analyze_text('my passport number is: 12345678')
        print(result)
        self.assertNotIn('US_PASSPORT', str(result))

        #negative test case
        result = analyze_text('my passport number is: 12345678AG1')
        print(result)
        self.assertNotIn('US_PASSPORT', str(result))

    def test_ipv4_address(self):
        """Test to show if a ipv4 address is detected"""

        #positive test case
        result = analyze_text('My ip address is: 123.123.45.233')
        print(result)
        self.assertIn('IP_ADDRESS', str(result))

        #negative test case
        result = analyze_text('My ip address is: 123.123')
        print(result)
        self.assertNotIn('IP_ADDRESS', str(result))

    def test_detect_race(self):
        """Test to make sure race is detected properly"""

        race_pattern = Pattern(name="race_pattern",
                               regex='[Bb]lack|[Ww]hite',
                               score=0.01)

        specific_race_pattern = Pattern(name="specific_race_pattern",
                                        regex='[Aa]frican [Aa]merican|[Cc]aucasion|[Nn]ative [Aa]merican|[Hh]ispanic|[Aa]sian|[Ii]ndian',
                                        score=0.40)

        race_context = ['race']
        # Define the recognizer with one or more patterns
        race_recognizer = PatternRecognizer(supported_entity="RACE",
                                            patterns=[race_pattern],
                                            context=race_context)

        specific_race_recognizer = PatternRecognizer(supported_entity="RACE",
                                            patterns=[specific_race_pattern],
                                            context=race_context)

        # Add the recognizer to the registry
        registry = RecognizerRegistry()
        registry.add_recognizer(race_recognizer)
        registry.add_recognizer(specific_race_recognizer)
        analyzer =  AnalyzerEngine( registry=registry, context_aware_enhancer = LemmaContextAwareEnhancer(context_similarity_factor=0.45, min_score_with_context_similarity=0.4))

        #Positive Test Case
        result = analyzer.analyze(text = 'I am African American', language = 'en')
        print(result)
        self.assertIn('NRP', [] ,result)

        #Positive Test Case
        result = analyzer.analyze(text = 'I am Native American', language = 'en')
        print(result)
        self.assertIn('NRP', [], result)

        #Negative Test Case
        result = analyzer.analyze(text = 'I am brown', language = 'en')
        print(result)
        self.assertNotIn('NRP', [], result)


    test_detect_race(unittest.TestCase)




