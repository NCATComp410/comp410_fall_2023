"""
    Main file for PII scanner
    Initial version shows supported entities
"""
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, PatternRecognizer, Pattern, RecognizerResult
from presidio_analyzer.predefined_recognizers import SpacyRecognizer, UsSsnRecognizer
import os
import sys
import re
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
    # https://microsoft.github.io/presidio/analyzer/adding_recognizers/

    # custom for place of birth
    place_of_birth_terms = ['place of birth', 'birthplace', 'born']
    pob_recognizer = PatternRecognizer(supported_entity="POB", deny_list=place_of_birth_terms)
    registry.add_recognizer(pob_recognizer)
    
    #Email addresses recognizer
    email_pattern = Pattern(name='email_pattern',
                            regex=r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',
                            score=0.9)
    email_recognizer = PatternRecognizer(supported_entity='EMAIL_ADDRESS',
                                         patterns=[email_pattern])
    registry.add_recognizer(email_recognizer)


    # Create an additional pattern to detect a 8-4-4-4-12 UUID
    uuid_pattern = Pattern(name='uuid_pattern',
                           regex=r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b',
                           score=0.9)
    uuid_recognizer = PatternRecognizer(supported_entity='UUID',
                                        patterns=[uuid_pattern])
    registry.add_recognizer(uuid_recognizer)

    # MAC address recognizer
    mac_pattern = Pattern(name='mac_pattern', 
                          regex=r'\b([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})\b', 
                          score=0.9)
    mac_recognizer = PatternRecognizer(supported_entity='MAC_ADDRESS',
                                       patterns=[mac_pattern])
    registry.add_recognizer(mac_recognizer)

    # username recognizer
    username_pattern = Pattern(name='USERNAME',
                               regex=r'@[\w]{3,25}',
                               score=0.8)
    username_recognizer = PatternRecognizer(supported_entity='USERNAME',
                                            patterns=[username_pattern])
    registry.add_recognizer(username_recognizer)

    # Create an additional pattern to detect a UDID
    udid_pattern = Pattern(name='udid_pattern',
                           regex=r'\b[a-fA-F0-9]{8}-[a-fA-F0-9]{16}\b',
                           score=0.9)
    udid_recognizer = PatternRecognizer(supported_entity='UDID',
                                        patterns=[udid_pattern])
    registry.add_recognizer(udid_recognizer)

    interest_pattern = Pattern(name='interestPattern',
                               regex=r'(?<=((?<!(doe?s?n\'?t\s|not\s))(like\s|love\s|enjoy\s|interested\sin\s)))[^\.\,\;]+',
                               score=0.9)
    interest_recognizer = PatternRecognizer(supported_entity='INTEREST', patterns=[interest_pattern])
    registry.add_recognizer(interest_recognizer)

    # Custom recognizer for detecting a 3-digit credit score
    # only recognizes a number between 300 and 850
    credit_score_pattern = Pattern(name='credit_score_pattern',
                                   regex=r'\b(3[0-9]{2}|[4-7][0-9]{2}|850)\b',
                                   score=0.9)
    credit_score_recognizer = PatternRecognizer(supported_entity='CREDIT_SCORE',
                                                patterns=[credit_score_pattern])
    registry.add_recognizer(credit_score_recognizer)

    # Creating detector for philosophical beliefs
    philosophical_beliefs_list = [
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
    philbeliefs_recognizer = PatternRecognizer(supported_entity="PHILBELIEFS", deny_list=philosophical_beliefs_list)
    registry.add_recognizer(philbeliefs_recognizer)

    # Creating detector for race
    race_pattern = Pattern(name="race_pattern",
                           regex='[Bb]lack|[Ww]hite',
                           score=0.15)
    specific_race_pattern = Pattern(name="specific_race_pattern",
                                    regex='[Aa]frican [Aa]merican|[Cc]aucasion|[Nn]ative [Aa]merican|[Hh]ispanic|['
                                          'Aa]sian|[Ii]ndian',
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
    maritalstats_recognizer = PatternRecognizer(supported_entity="MARITALSTATS", deny_list=marital_status_list)
    registry.add_recognizer(maritalstats_recognizer)

    # political terms
    political_terms = ['liberal', 'democrat', 'republican', 'republicans', 'democrats', 'liberals', 'conservative',
                       'conservatives']
    political_recognizer = PatternRecognizer(supported_entity="NPR", deny_list=political_terms)
    registry.add_recognizer(political_recognizer)

    # Create an additional pattern to detect a 123456789 Student Id
    student_id_pattern = Pattern(name='student_id',
                                 regex=r'\b(?i:student|id)\D*\d{9}\b',
                                 score=0.8)
    student_id_recognizer = PatternRecognizer(supported_entity='STUDENT_ID',
                                              patterns=[student_id_pattern])
    registry.add_recognizer(student_id_recognizer)

    # Create a pattern to detect fourteen digit phone numbers
    international_pn_pattern = Pattern(name='international_pn',
                                       regex=r'^\d{3}-\d{3}-\d{4}-\d{4}',
                                       score=0.9)
    international_pn_recognizer = PatternRecognizer(supported_entity='INTERNATIONAL_PN',
                                                    patterns=[international_pn_pattern])
    registry.add_recognizer(international_pn_recognizer)

    # detects zipcode
    zipcode_pattern = Pattern(name='zipcode_id',
                              regex=r'((\d{5}-\d{4}) | (\b\d{5}\b))',
                              score=0.9)
    zipcode_recognizer = PatternRecognizer(supported_entity='ZIPCODE',
                                           patterns=[zipcode_pattern])
    registry.add_recognizer(zipcode_recognizer)

    # DEWBERRY CUSTOM REGEX FOR LOCATIONS!
    dewLocPattern = Pattern(name='DewLOCATION',
                            regex=r'[0-9]+\s[A-Za-z]+\s[A-Za-z]+\s[A-Za-z]+,\s[A-Za-z]+,\s[A-Za-z][A-Za-z]\s\d\d\d\d\d',
                            score=.9)
    dewLocRecognizer = PatternRecognizer(supported_entity='DewLocEnt', patterns=[dewLocPattern])
    registry.add_recognizer(dewLocRecognizer)
    # END DEWBERRY CUSTOM REGEX ADDITION

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

    # Creating detector for philosophical beliefs
    genders_list = [
        "female",
        "male",
        "non-binary"
    ]

    genders_recognizer = PatternRecognizer(supported_entity='GENDER', deny_list=genders_list)
    registry.add_recognizer(genders_recognizer)

    # Customize SpacyRecognizer to include some additional labels
    # First remove the default SpacyRecognizer
    registry.remove_recognizer("SpacyRecognizer")

    # Add ORGANIZATION as an entity even though it is not recommended
    entities = [
        "DATE_TIME",
        "NRP",
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
        "USERNAME"
    ]
    # Add FAC to be identified as a location
    # FAC = buildings, airports, highways, bridges, etc
    label_groups = [
        ({"LOCATION"}, {"GPE", "LOC", "FAC"}),
        ({"PERSON", "PER"}, {"PERSON", "PER"}),
        ({"DATE_TIME"}, {"DATE", "TIME"}),
        ({"NRP"}, {"NORP"}),
        ({"ORGANIZATION"}, {"ORG"}),
        ({"USERNAME"}, {"USER"})
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

    # Custom Regex for detecting 12 digit license
    thorlicenseNum = Pattern(name='ThorPattern', regex=r'\b\d{12}\b', score=.9)
    thorLicenseRecognizer = PatternRecognizer(supported_entity='NCDL', patterns=[thorlicenseNum])
    registry.add_recognizer(thorLicenseRecognizer)

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


def scan_files(start_path):
    # Define a list of PII types this scanner will support
    # This is based on each team's work
    supported_pii_list = ['CREDIT_CARD', 'EMAIL_ADDRESS', 'MEDICAL_LICENSE', 'DewLocEnt', 'PHILBELIEFS', 'ZIPCODE',
                          'IP_ADDRESS', 'AU_MEDICARE', 'US_PASSPORT', 'UUID', 'INTERNATIONAL_PN', 'PERSON', 'BIRTHDATE',
                          'POB', 'NPR', 'US_BANK_NUMBER', 'EYE_COLOR', 'UDID', 'INTEREST', 'GENDER',
                          'CRYPTO', 'MARITALSTATS', 'LOCATION', 'US_SSN', 'US_ITIN', 'MAC_ADDRESS', 'STUDENT_ID',
                          'RACE', 'USERNAME', 'CREDIT_SCORE', 'PHONE_NUMBER', 'NCDL']

    # check to make sure start_path is a directory
    if not os.path.isdir(start_path):
        print(f'{start_path} is not a directory')
        sys.exit(1)

    # Walk each file in the directory tree
    for root, dirs, files in os.walk(start_path):
        for file in files:
            # Only process .txt files
            if file.lower().endswith('.txt'):
                # print the full file path
                print('----------------------------------------')
                print(os.path.join(root, file))
                # Open the file
                with open(os.path.join(root, file), 'r') as f:
                    expected_entity = ''
                    # read each line
                    for line in f.readlines():
                        # If a line begins with a # then print it but don't analyze it
                        if line.startswith('#'):
                            print(line.strip())
                            # Try to find an expected_entity in the line
                            m = re.search(r'([A-Z_]{3,})', line)
                            if m:
                                expected_entity = m.group(1)
                            else:
                                expected_entity = ''
                        else:
                            # analyze each line
                            detected = False
                            for result in analyze_text(line, score_threshold=0.1):
                                if result.entity_type in supported_pii_list:
                                    if expected_entity:
                                        if result.entity_type == expected_entity:
                                            detected = True
                                    else:
                                        detected = True
                                    print('  ---')
                                    print('  '+line.strip())
                                    print('  ', end='')
                                    print(result)
                                    # if this is a no_ file then print a warning
                                    if file.startswith('no_') and detected:
                                        print('  ** FALSE DETECTION **')
                                        detected = False
                            # if there were no results detected and this is a has_ file then print it
                            if file.startswith('has_') and not detected:
                                print('  ---')
                                print('  **NOT DETECTED** '+line.strip())


if __name__ == '__main__':
    # check to make sure one argument is passed if not print helo message
    if len(sys.argv) != 2:
        print("Usage: python pii_scan.py <file path>")
        sys.exit(1)
    scan_files(sys.argv[1])
