from summarizer import Summarizer

# Open and read the input text file
with open("text.txt", "r") as f:
    text = f.read()

# Initialize the BERT summarizer model
model = Summarizer()

# Generate the summary
result = model(text, min_length=20, max_length=200, use_first=False, ratio=0.6)

# Join the result into a single string
summary = "".join(result)

# Write the summarized text to a new file
with open("summary.txt", "w") as summary_file:
    summary_file.write(summary)

# Print the size of the original and summarized texts
original_size = len(text)
summary_size = len(summary)

print(f"Original Text Size: {original_size} characters")
print(f"Summarized Text Size: {summary_size} characters")
print("Summary written to 'summary.txt':")
print(summary)


import pprint
import itertools
import re
import pke
import string
from nltk.corpus import stopwords

def get_nouns_multipartite(text):
    out=[]

    extractor = pke.unsupervised.MultipartiteRank()
    extractor.load_document(input=text)
    #    not contain punctuation marks or stopwords as candidates.
    pos = {'PROPN'}
    #pos = {'VERB', 'ADJ', 'NOUN'}
    stoplist = list(string.punctuation)
    stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    stoplist += stopwords.words('english')
    extractor.candidate_selection(pos=pos, stoplist=stoplist)
    # 4. build the Multipartite graph and rank candidates using random walk,
    #    alpha controls the weight adjustment mechanism, see TopicRank for
    #    threshold/method parameters.
    extractor.candidate_weighting(alpha=1.1,
                                  threshold=0.75,
                                  method='average')
    keyphrases = extractor.get_n_best(n=20)

    for key in keyphrases:
        out.append(key[0])

    return out

keywords = get_nouns_multipartite(full_text) 
print (keywords)
filtered_keys=[]
for keyword in keywords:
    if keyword.lower() in summarized_text.lower():
        filtered_keys.append(keyword)
        
print (filtered_keys)