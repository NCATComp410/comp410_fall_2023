import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, PatternRecognizer, Pattern, RecognizerResult
from presidio_analyzer.predefined_recognizers import SpacyRecognizer
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
    # https://microsoft.github.io/presidio/analyzer/adding_recognizers/
    # Create an additional pattern to detect a 8-4-4-4-12 UUID
    uuid_pattern = Pattern(name='uuid_pattern',
                           regex=r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b',
                           score=0.9)
    uuid_recognizer = PatternRecognizer(supported_entity='UUID',
                                        patterns=[uuid_pattern])
    registry.add_recognizer(uuid_recognizer)

    # Customize SpacyRecognizer to include some additional labels
    registry.remove_recognizer("SpacyRecognizer")
    # Add FAC to be identified as a location
    # FAC = buildings, airports, highways, bridges, etc
    label_groups = [
        ({"LOCATION"}, {"GPE", "LOC", "FAC"}),
        ({"PERSON", "PER"}, {"PERSON", "PER"}),
        ({"DATE_TIME"}, {"DATE", "TIME"}),
        ({"NRP"}, {"NORP"}),
        ({"ORGANIZATION"}, {"ORG"}),
    ]
    spacy_recognizer = SpacyRecognizer(check_label_groups=label_groups)
    registry.add_recognizer(spacy_recognizer)

    # create a custom US_SSN recognizer
    ssn_pattern = Pattern(name='ssn_pattern',
                           regex=r'(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)',
                           score=0.9)
    ssn_recognizer = PatternRecognizer(supported_entity='US_SSN',
                                        patterns=[ssn_pattern])
    registry.add_recognizer(ssn_recognizer)

    # Set up analyzer with our updated recognizer registry
    analyzer = AnalyzerEngine(registry=registry)

    # Show all entities that can be detected for debugging
    if show_supported:
        return analyzer.get_supported_entities()

    if show_details:
        results = analyzer.analyze(text=text,
                                   score_threshold=score_threshold,
                                   language="en",
                                   return_decision_process=show_details)
        print(results)
        for r in results:
            decision_process = r.analysis_explanation
            print(decision_process)
    else:
        results = analyzer.analyze(text=text,
                                   score_threshold=score_threshold,
                                   language='en')
    return results


if __name__ == '__main__':
    print(show_aggie_pride())
    print('Displaying supported entities')
    pp.pprint(analyze_text('This is a test', show_supported=True))
