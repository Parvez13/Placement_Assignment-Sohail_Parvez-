from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd 

# Download the NLTK stopwords corpus
import nltk
nltk.download('stopwords')

df_comments = pd.read_csv('comments.csv')

# Tokenize the comments
tokenized_comments = df_comments['Comment'].apply(word_tokenize)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_comments = tokenized_comments.apply(
    lambda comment: [word for word in comment if word.lower() not in stop_words])

# Count word frequencies
word_frequencies = filtered_comments.explode().value_counts()


N = 10  # Number of top words to extract
top_words = word_frequencies.head(N).index.tolist()

print('Top', N, 'words:')
for word in top_words:
    print(word)
