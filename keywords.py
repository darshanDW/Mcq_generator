import re
import nltk
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
from nltk.corpus import stopwords
from rake_nltk import Rake

from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor


nltk.download('punkt')
nltk.download('stopwords')

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def extract_keywords_with_ranks(text):
    rake = Rake(max_length=2,min_length=1,include_repeated_phrases=False)  
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases_with_scores() 


def extract_keywords(text):
    rake = Rake(max_length=2, min_length=1, include_repeated_phrases=False)
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()


def tokenize_sentences(text):
    sentences = [sent_tokenize(text)]
    sentences = [y for x in sentences for y in x]
    # Remove any short sentences less than 20 letters.
    sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20]
    return sentences



def get_sentences_for_keyword(keywords, sentences):
    keyword_processor = KeywordProcessor()
    keyword_sentences = {}
    for word in keywords:
        keyword_sentences[word] = []
        keyword_processor.add_keyword(word)
    for sentence in sentences:
        keywords_found = keyword_processor.extract_keywords(sentence)
        for key in keywords_found:
            keyword_sentences[key].append(sentence)

    for key in keyword_sentences.keys():
        values = keyword_sentences[key]
       
        values = sorted(values, key=len, reverse=True)
        keyword_sentences[key] = values
    return keyword_sentences



file_path = 'C:/Users/asus/OneDrive/Desktop/ai/summary.txt'

text = read_text_file(file_path)
filtered_text = remove_stopwords(text)
keywords=extract_keywords(filtered_text)
sentences = tokenize_sentences(text)
keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
