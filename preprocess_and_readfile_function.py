import nltk
import spacy
import re
import spacy
import unidecode
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

contractions = {"ain't": "am not", "aren't": "are not", "can't": "cannot", "can't've": "cannot have",
                        "'cause": "because", "could've": "could have", "couldn't": "could not",
                        "couldn't've": "could not have", "didn't": "did not", "doesn't": "does not", "don't": "do not",
                        "hadn't": "had not", "hadn't've": "had not have", "hasn't": "has not", "haven't": "have not",
                        "he'd": "he would", "he'd've": "he would have", "we've": "we have", "i'm": "i am", "i'd": "i would"}

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

#this function helps in reading contents from a file. Here the file read is 'dipti.txt'.
def read_file():
    #to read the contents from a file
    f=open("F:\hpe\dipti.txt","r")
    contents=f.read()
    #contents="I'd like to have three cups of coffee from your Café."

    nlp = spacy.load('en_core_web_sm')
    all_stopwords = nlp.Defaults.stop_words
    all_stopwords.remove("no")
    all_stopwords.remove("not")

    sentences=sent_tokenize(contents)
    for sentence in sentences:
        #lowercase
        input_str = sentence
        input_str = input_str.lower()

        #remove starting and ending white spaces
        input_str = input_str.strip()

        # remove numbers
        text = input_str
        text = ''.join(c if c not in map(str, range(0, 10)) else "" for c in text)

        #converting accented characters
        text = unidecode.unidecode(input_str)

        #expanding contractions
        input_str=clean_text(text);

        # remove punctuations and stopwords
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        text = tokenizer.tokenize(input_str)
        text = [w for w in text if not w in all_stopwords]
        text = " ".join(text)

        #performing lemmatization instead of stemming
        #lemmatization
        sp = spacy.load('en', disable=['parser', 'ner'])
        doc = nlp(text)
        lemme=" ".join([token.lemma_ for token in doc])
        #print(lemme)

        #parts of speech tagging
        tokens=nltk.word_tokenize(text)
        result=nltk.pos_tag(tokens)
        print(result)

read_file()