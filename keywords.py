import re
import nltk
from nltk.corpus import stopwords
from rake_nltk import Rake

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

file_path = 'C:/Users/asus/OneDrive/Desktop/ai/summary.txt'

text = read_text_file(file_path)

filtered_text = remove_stopwords(text)

print(f"\nFiltered Text (without stopwords):\n{filtered_text}")

keywords_with_ranks = extract_keywords_with_ranks(filtered_text)

print("\nRanked Keywords with Scores (single words or two-word phrases):")
for score, keyword in keywords_with_ranks:
    print(f"Keyword: {keyword} - Score: {score}")
