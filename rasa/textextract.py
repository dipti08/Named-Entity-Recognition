#this file allows the pdf to be uploaded externally using rest api(rest api channel can be used with rasa) and 
#allows the bot to reply with the pdf tagged with the custom entites.

#this file includes the data preprocessing of the text extracted from the pdf and then tagging of the 
#important words found in the pdf with the custom entities.

from __future__ import unicode_literals, print_function
import requests
import nltk
import spacy
import re
import spacy
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#tika library helps in reading any file: .txt,.pdf,etc
import tika
from tika import parser

message = ""

count = 1
if count == 1:

    #contractions consists of the various short forms of the common words
    #it will map the short form to their full form to help ease data preprocessing
    contractions = {"ain't": "am not", "aren't": "are not", "can't": "cannot", "can't've": "cannot have",
                    "'cause": "because", "could've": "could have", "couldn't": "could not",
                    "couldn't've": "could not have", "didn't": "did not", "doesn't": "does not", "don't": "do not",
                    "hadn't": "had not", "hadn't've": "had not have", "hasn't": "has not", "haven't": "have not",
                    "he'd": "he would", "he'd've": "he would have", "we've": "we have", "i'm": "i am",
                    "i'd": "i would"}

    #function to remove contractions and punctuations from the extracted data
    def clean_text(text):
        if True:
            text = text.split()
            new_text = []
            for word in text:
                if word in contractions:
                    new_text.append(contractions[word])
                else:
                    new_text.append(word)
                    text = " ".join(new_text)
                    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
                    text = re.sub(r'\<a href', ' ', text)
                    text = re.sub(r'&amp;', '', text)
                    text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
                    text = re.sub(r'<br />', ' ', text)
                    text = re.sub(r'\'', ' ', text)
        return text

    #input the pdf file name required to be tagged
    filename = input('Enter file name - ')
    parsedPDF = parser.from_file(filename)
    pdf = parsedPDF["content"]
    pdf = pdf.replace('\n\n', '')
    #split the sentences inside the pdf to process each sentence one by one
    sentences = nltk.sent_tokenize(pdf)
    # print(sentences)

    #spaCy with pre-built models can parse text and compute various NLP related features.
    # Initialize spacy 'en_core_wev_sm' model.
    nlp = spacy.load('en_core_web_sm')
    #remove the words 'no' and 'not' from the stopwords dictionary as they are important
    all_stopwords = nlp.Defaults.stop_words
    all_stopwords.remove("no")
    all_stopwords.remove("not")

    #preprocessing for each sentence
    for sentence in sentences:
        input_str = sentence
        input_str = input_str.lower()

        # remove starting and ending white spaces
        input_str = input_str.strip()

        # remove numbers
        text = input_str
        text = ''.join(c if c not in map(str, range(0, 10)) else "" for c in text)

        # expanding contractions
        input_str = clean_text(text)
        # remove punctuations and stopwords (stopwords are unnecessary words not required for tagging)
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        text = tokenizer.tokenize(input_str)
        text = [w for w in text if not w in all_stopwords]
        text = " ".join(text)
        message = message + text + " "

    # print(message)

    #messageList is a list that consists of all the useful words extracted from the pdf(it may also contain dupliacte words)
    messageList = message.split(" ")

    #final_list removes the repeated/duplicate words present in the messageList
    final_list = list(dict.fromkeys(messageList))

    correct = ""

    #correct string is the final string consisting of all the words and their entities present in the pdf
    #based upon the custom dataset prepared for the bot.
    for element in final_list:
        correct = correct + element + " "

    #uploading the pdf externally on localhost:5002 port for the bot to tag
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": correct})

    #reply from the bot
    print("The entities are: ", end='\n')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")
    count = count + 1

