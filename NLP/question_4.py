import csv
import re
import nltk 
import heapq

with open('data_science.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    next(csv_reader)
    for row in csv_reader:
        texts = row[0]
clean_text = re.sub(r'\[[0-9]*\]', ' ', texts)
clean_text = re.sub(r'\s+', ' ', clean_text)
format_text = re.sub('[^a-zA-Z]', ' ', clean_text )
format_text = re.sub(r'\s+', ' ', format_text)

# Sentence_list
sentence_list = nltk.sent_tokenize(clean_text)

# Stopwords
stopwords = nltk.corpus.stopwords.words('english')

# Calculate word frequencies
word_frequencies = {}
for word in nltk.word_tokenize(format_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

# Sentence scores
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

# summary
summary = ' '.join(summary_sentences)
print(summary)