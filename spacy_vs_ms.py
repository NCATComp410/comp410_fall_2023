"""
This script compares the results of Microsoft Presidio and Spacy NLP libraries.
User can enter a string which will be analyzed by both libraries.
"""
import spacy
from presidio_analyzer import RecognizerResult
from pii_scan import analyze_text
from typing import List

# make sure the correct spacy model is loaded
# en_core_web_sm en_core_web_md en_core_web_lg
spacy_model = 'en_core_web_lg'
try:
    nlp = spacy.load(spacy_model)
except OSError:
    from spacy.cli import download
    download(spacy_model)
    nlp = spacy.load(spacy_model)
    print(nlp.get_pipe("ner").labels)


# NLP on a string using spacy only
def try_spacy(text: str):
    print('<-- spacy only results -->')
    print('text:', text)
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


# NLP using Microsoft Presidio
def try_ms(text: str, show_explanation=False):
    print('<-- Microsoft Presidio results -->')
    print('text:', text)
    results: List[RecognizerResult] = analyze_text(text, show_supported=False)

    for r in results:
        # Get a substring from r.start to r.end
        r_text = text[r.start:r.end]
        print(f'result: {r_text} entity_type: {r.entity_type}, score: {r.score}, start: {r.start}, end: {r.end}')
        if show_explanation:
            print(r.analysis_explanation)


if __name__ == '__main__':
    # input a test string
    test_str = input('Enter a test string: ')
    # Only run if a string was entered
    if test_str:
        try_spacy(test_str)
        try_ms(test_str, show_explanation=False)
