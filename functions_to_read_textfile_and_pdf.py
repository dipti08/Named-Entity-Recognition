import nltk
import spacy
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet
from nltk import word_tokenize
from nltk.corpus import stopwords

#this function helps in reading contents from a file. Here the file read is 'dipti.txt'.
def read_file():
    #to read the contents from a file
    f=open("F:\hpe\dipti.txt","r")
    contents=f.read()

    #spaCy with pre-built models can parse text and compute various NLP related features.
    #It determines the part-of-speech tag by default and assigns the corresponding lemma.

    # Initialize spacy 'en' model, keeping only tagger component needed for lemmatization out of the three namely 'parser', 'tagger' and 'entity recogniser'.
    nlp = spacy.load('en', disable=['parser', 'ner'])
    sentences=sent_tokenize(contents)
    for sentence in sentences:
        # Parse the sentence using the loaded 'en' model object `nlp`
        doc=nlp(sentence)
        # Extract the lemma for each token and join
        print(" ".join([token.lemma_ for token in doc]))

# This function helps to copy the content from one text file to another.
def copy_from_one_file_to_another():
    with open("F:\hpe\dipti.txt","r") as fread:
        # It will copy the contents to new file 'dipti_copy' if it already exists or will create a new file if it does not exists.
        with open("F:\hpe\dipti_copy.txt","w") as fwrite:
            for line in fread:
                fwrite.write(line)
    f=open("F:\hpe\dipti_copy.txt","r")
    contents=f.read();
    #print(contents)

def read_pdf():
    # Importing required modules
    import PyPDF2
    # Creating a pdf file object
    pdfFileObj = open('F:\hpe\International_Journal_of_Application_or.pdf', 'rb')
    # Creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Getting number of pages in pdf file
    pages = pdfReader.numPages
    # Loop for reading all the Pages
    for i in range(pages):
        # Creating a page object
        pageObj = pdfReader.getPage(i)
        # Printing Page Number
        print("Page No: ", i)
        # Extracting text from page and splitting it into chunks of lines
        text = pageObj.extractText().split("  ")
        # Finally the lines are stored into list for iterating over list a loop is used
        for i in range(len(text)):
            # Printing the line
            # Lines are seprated using "\n"
            print(text[i], end="\n\n")
        # For Seprating the Pages
        print()
    # closing the pdf file object
    pdfFileObj.close()

def pdf_copy():
    import PyPDF2
    pdfFileObj = open('F:\hpe\International_Journal_of_Application_or.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader.numPages
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
    #TEST = pageObj.extractText()
    #if TEST.find("TEXT") == 1:
        pdfWriter.addPage(pageObj)

    pdfOutput = open('F:\hpe\pdf_copy.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

