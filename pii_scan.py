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


def create_analyzer():
    """Create Microsoft Presidio Analyzer"""
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

    #Custom recognizer for detecting a 3-digit credit score
    # only recongnizes a number between 300 and 850
    credit_score_pattern = Pattern(name='credit_score_pattern',
                                   regex=r'\b(3[0-9]{2}|[4-7][0-9]{2}|850)\b',
                                   score=0.9)
    credit_score_recognizer = PatternRecognizer(supported_entity='CREDIT_CARD',
                                                patterns=[credit_score_pattern])
    registry.add_recognizer(credit_score_recognizer)

    # Creating detector for philisophical beliefs
    philisophical_beliefs_list = [
        "atheism",
        "atheist",
        "secularism",
        "secularist",
        "idealism",
        "stoicism",
        "rationalism",
        "relativism",
        "marxism",
        "existentialism",
        "hedonism",
    ]

    philbeliefs_recognizer = PatternRecognizer(supported_entity="PHILBELIEFS", deny_list=philisophical_beliefs_list)
    registry.add_recognizer(philbeliefs_recognizer)

    # Creating detector for race
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
    registry.add_recognizer(race_recognizer)
    registry.add_recognizer(specific_race_recognizer)

    # Creating a Detector for Marital Statuses:
    marital_status_list = [
        "single",
        "married",
        "divorced",
        "separated",
        "widowed",
        "domestic partnership",
        "civil union",
        "annulled"
    ]
    maritalstats_recognizer = PatternRecognizer(supported_entity = "MARITALSTATS", deny_list= marital_status_list)
    registry.add_recognizer(maritalstats_recognizer)


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


    #DEWBERRY CUSTOM REGEX FOR LOCATIONS! 
    dewLocPattern = Pattern(name='DewLOCATION', regex=r'[0-9]+\s[A-Za-z]+\s[A-Za-z]+\s[A-Za-z]+,\s[A-Za-z]+,\s[A-Za-z][A-Za-z]\s\d\d\d\d\d', score=.9)
    dewLocRecognizer = PatternRecognizer(supported_entity= 'DewLocEnt', patterns=[dewLocPattern])
    registry.add_recognizer(dewLocRecognizer)
    #END DEWBERRY CUSTOM REGEX ADDITION

    eye_color_pattern = Pattern(name='eye_color_pattern',
                                regex=r'\bEye color:\s*(blue|green|hazel|brown|gray|amber|black|red|violet|pink|purple|orange)\b',
                                score=0.85)
    eye_color_recognizer = PatternRecognizer(supported_entity='EYE_COLOR',
                                             patterns=[eye_color_pattern])
    registry.add_recognizer(eye_color_recognizer)


    birthdate_pattern = Pattern(name='birthdate_pattern',
                                regex=r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$\b',
                                score=0.4)
    birthdate_recognizer = PatternRecognizer(supported_entity='BIRTHDATE',
                                             patterns=[birthdate_pattern])
    registry.add_recognizer(birthdate_recognizer)

    # Customize SpacyRecognizer to include some additional labels
    # First remove the default SpacyRecognizer
    registry.remove_recognizer("SpacyRecognizer")

    # Creating detector for philisophical beliefs
    genders_list = [
       "female",
       "male",
       "non-binary"
    ]

    genders_recognizer = PatternRecognizer(supported_entity='GENDER', deny_list=genders_list)
    registry.add_recognizer(genders_recognizer)

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
    return AnalyzerEngine(registry=registry)


# Create a global analyzer to speed up processing
analyzer = create_analyzer()


def analyze_text(text: str, show_supported=False, show_details=False, score_threshold=0.0) -> \
        list[str] | list[RecognizerResult]:

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






