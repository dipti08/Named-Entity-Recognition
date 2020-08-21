
SpaCy is an open-source library for advanced Natural Language Processing in Python. 
It can be installed using the following steps
pip install -U spacy 
python -m spacy download en

The following three files are used to tag the custom entities in the input pdf file.

json_to_spacy.py  
Training dataset used is dataset(1).json
NER output is very close to the format used by Spacy, just that Spacy used Python tuples which are not supported by JSON standard, hence just use this file to convert JSON format to Spacy training data.
The training data used here is dataset(1) and is in json format

custom_ner.py
we are adding the entity recognizer to the pipeline. If an existing model is being used, we have to disable all other pipeline components during training using nlp.disable_pipes. This way, only the entity recognizer gets trained.
We add the new custom entity labels to the entity recognizer using the add_label method.


spacy saved model.py
Using tika python library we take the input as a pdf file and tag the custom entities in the file


Running the spacy_custom ner
firstly we run the json_to_spacy model to convert the dataset from json format to spacy supported format
This spacy formatted dataset is used in the custom_ner file ,and the output is stored as the spacy_model.
The spacy_model is run  as follows
Step 1: Open the command prompt and activate the ner spacy environment 
Chnage the directory to spacy_model
Step 2 : Run the python file spacy_ner.py
Step 3: The custom entities of the sentence would be tagged
