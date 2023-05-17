import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def count_pos_tags(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged_tokens = pos_tag(tokens)
    
    # Initialize counts
    counts = {'Noun': 0, 'Verb': 0, 'Pronoun': 0, 'Adjective': 0}
    
    # Count the occurrences of each part-of-speech
    for _, tag in tagged_tokens:
        if tag.startswith('NN'):
            counts['Noun'] += 1
        elif tag.startswith('VB'):
            counts['Verb'] += 1
        elif tag.startswith('PRP'):
            counts['Pronoun'] += 1
        elif tag.startswith('JJ'):
            counts['Adjective'] += 1
    
    return counts

# Test the function with a sample phrase
phrase = "The cat is sitting on the mat."
counts = count_pos_tags(phrase)
print(counts)