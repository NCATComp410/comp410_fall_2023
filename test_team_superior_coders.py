import unittest
import re

from typing import List
import pprint

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, EntityRecognizer, Pattern, RecognizerResult
from presidio_analyzer.recognizer_registry import RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngine, SpacyNlpEngine, NlpArtifacts
from presidio_analyzer.context_aware_enhancers import LemmaContextAwareEnhancer


from pii_scan import show_aggie_pride, analyze_text


class TestSuperiorCoders(unittest.TestCase):
  
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

   
    '''Test to make sure race is detected properly.'''
    def test_detect_race(self):

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

        
    
    
       