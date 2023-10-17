"""
    Main file for PII scanner
    Initial version shows supported entities
"""
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, PatternRecognizer, Pattern, RecognizerResult
from presidio_analyzer.predefined_recognizers import SpacyRecognizer, UsSsnRecognizer
# Define a pretty printer for debugging
import pprint
pp = pprint.PrettyPrinter(indent=4)

# make sure en_core_web_lg is loaded correctly
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")


def show_aggie_pride():
    """Show Aggie Pride"""
    return 'Aggie Pride - Worldwide'


class SsnNoValidate(UsSsnRecognizer):
    # make sure the super class is called to initialize the recognizer
    def __init__(self):
        super().__init__()

    def invalidate_result(self, pattern_text: str) -> bool:
        """Override the default validation to always return false.  This allows us to use invalid SSNs for testing"""
        return False


def analyze_text(text: str, show_supported=False, show_details=False, score_threshold=0.0) -> \
        list[str] | list[RecognizerResult]:
    """Analyze text using Microsoft Presidio"""
    # Overview of Presidio
    # https://microsoft.github.io/presidio/analyzer/

    # Initialize the recognition registry with the default supported recognizers
    # https://microsoft.github.io/presidio/supported_entities/
    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()

    # Custom recognizers
    #custom for place of birth
    place_of_birth_terms = ['place of birth', 'birthplace', 'born']
    pob_recognizer = PatternRecognizer(supported_entity="POB", deny_list=place_of_birth_terms)
    registry.add_recognizer(pob_recognizer)
    # https://microsoft.github.io/presidio/analyzer/adding_recognizers/
    # Create an additional pattern to detect a 8-4-4-4-12 UUID
    uuid_pattern = Pattern(name='uuid_pattern',
                           regex=r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b',
                           score=0.9)
    uuid_recognizer = PatternRecognizer(supported_entity='UUID',
                                        patterns=[uuid_pattern])

    interest_pattern = Pattern(name='interestPattern',
                           regex='(?<=((?<!(doe?s?n\'?t\s|not\s))(like\s|love\s|enjoy\s|interested\sin\s)))[^\.\,\;]+',
                           score=0.9)
    interest_recognizer = PatternRecognizer(supported_entity='INTEREST', patterns=[interest_pattern])
    registry.add_recognizer(uuid_recognizer)
    registry.add_recognizer(interest_recognizer)


    #Create an additional pattern to detect a 123456789 Student Id
    student_id_pattern = Pattern(name='student_id',
                                 regex=r'\b\d{9}\b',
                                 score=0.8)
    student_id_recognizer = PatternRecognizer(supported_entity='STUDENT_ID',
                                              patterns=[student_id_pattern])
    registry.add_recognizer(student_id_recognizer)

#Custom recognizer for detecting a 5-digit zipcode

    zipcode_pattern = Pattern(name='zipcode_pattern',
                                   regex=r'(\b\d{5}(?!-)\b)| (\b\d{5}-\d{4}\b)',
                                   score=0.9)
    zipcode_recognizer = PatternRecognizer(supported_entity='ZIPCODE',
                                                patterns=[zipcode_pattern])
    registry.add_recognizer(zipcode_recognizer)

    # Customize SpacyRecognizer to include some additional labels
    # First remove the default SpacyRecognizer
    registry.remove_recognizer("SpacyRecognizer")
    # Add ORGANIZATION as an entity even though it is not recommended
    entities = [
        "DATE_TIME",
        "NRP",
        "LOCATION",
        "PERSON",
        "ORGANIZATION"
    ]
    # Add FAC to be identified as a location
    # FAC = buildings, airports, highways, bridges, etc
    label_groups = [
        ({"LOCATION"}, {"GPE", "LOC", "FAC"}),
        ({"PERSON", "PER"}, {"PERSON", "PER"}),
        ({"DATE_TIME"}, {"DATE", "TIME"}),
        ({"NRP"}, {"NORP"}),
        ({"ORGANIZATION"}, {"ORG"}),
    ]
    # noinspection PyTypeChecker
    spacy_recognizer = SpacyRecognizer(check_label_groups=label_groups, supported_entities=entities)
    registry.add_recognizer(spacy_recognizer)

    # create a custom US_SSN recognizer
    # Remove the default US_SSN recognizer
    registry.remove_recognizer('UsSsnRecognizer')
    # Add custom US_SSN recognizer
    ssn_recognizer = SsnNoValidate()
    registry.add_recognizer(ssn_recognizer)

    # Set up analyzer with our updated recognizer registry
    analyzer = AnalyzerEngine(registry=registry)
    # Add ORGANIZATION to the list of labels to be checked
    labels = analyzer.get_supported_entities()
    labels.append('ORGANIZATION')

    # Show all entities that can be detected for debugging
    if show_supported:
        return labels

    results = analyzer.analyze(text=text,
                               score_threshold=score_threshold,
                               language="en",
                               entities=labels,
                               return_decision_process=show_details)
    if show_details:
        print(results)
        for r in results:
            decision_process = r.analysis_explanation
            print(decision_process)

    return results


if __name__ == '__main__':
    print(show_aggie_pride())
    print('Displaying supported entities')
    pp.pprint(analyze_text('This is a test', show_supported=True))
