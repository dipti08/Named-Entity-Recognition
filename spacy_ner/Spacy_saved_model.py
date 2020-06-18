#!/usr/bin/env python
# coding: utf8

# Training additional entity types using spaCy
from __future__ import unicode_literals, print_function
import pickle
import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding

# Loading training data


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def main(model=None, new_model_name='new_model', output_dir=r'C:\Users\DIPTI AGARWAL\Desktop\robot\spacy_ner\spacy saved model', n_iter=6):
    """Setting up the pipeline and entity recognizer, and training the new entity."""

    print("Loading from", output_dir)
    nlp2 = spacy.load(output_dir)
    test = 'HPE use Python, MongoDB, Node.js and JSON for developing NLP and Machine Learning applications for phone and Tablet '
    print(test)
    doc2 = nlp2(test)
    for ent in doc2.ents:
        print(ent.label_, ent.text)


if __name__ == '__main__':
    plac.call(main)
    
