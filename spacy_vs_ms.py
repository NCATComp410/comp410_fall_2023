"""
This script compares the results of Microsoft Presidio and Spacy NLP libraries.
User can enter a string which will be analyzed by both libraries.
Added while loop to stay in the program until user enters <enter> to quit to improve load times.
"""
import spacy
from presidio_analyzer import RecognizerResult
from pii_scan import analyze_text, nlp
from typing import List


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
    while True:
        # input a test string
        test_str = input('Enter a test string or <enter> to quit: ')
        # Only run if a string was entered correctly
        if test_str:
            try_spacy(test_str)
            try_ms(test_str, show_explanation=False)
            print('----------------------------------------')
        else:
            break
