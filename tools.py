# python3 built-ins:
from collections import defaultdict

# data wrangling libraries:
import numpy as np
import pandas as pd

# text manipulation libraries:
import textstat
import nltk
from nltk.corpus import stopwords

# Pandas settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

# reading data and storing it into a dict variable called freq
with open('en_50k.txt', 'r') as f:
    data = f.read()
    data = data.split()
    
    words = data[0::2]
    freqs = data[1::2]
    
    WORDS_RELATIVE_FREQ = defaultdict(lambda: 0, {k: int(v) for k, v in zip(words, freqs)})


def rarity(excerpt):
    """
    This functions returns the average rarity of an excerpt
    the lower the output is, the more rare the text is.
    """
    excerpt = excerpt.lower()  # passing to lower case
    excerpt = excerpt.replace('?', '').replace('.', '').replace(',', '') 
    excerpt = excerpt.replace('!', '').replace(':', '').replace(';', '')
    
    stopwords_list = set(stopwords.words('english'))
    
    # this filters the stopwords:
    excerpt_words = {word for word in excerpt.split() if word not in stopwords_list}
    
    suma = 0
    for word in excerpt_words:
        suma += WORDS_RELATIVE_FREQ[word]

    avg = suma / len(excerpt.split())

    return int(avg)


# Let's create a feature that measures the number of unique words in a excerpt:
def num_unique_words(text):
    text = text.lower()
    text = text.replace('?', '').replace('.', '').replace(',', '')
    text = text.replace(':', '').replace(';', '').replace('!', '')
    text = text.replace('(', '').replace(')', '')
    
    text_set = set(text.split())
    return len(text_set)


def num_punct_marks(text):
    # let's create a feature that measures the number of puntuation marks in the excerpt:
    total = text.count('?') + text.count('.') + text.count(',') + \
            text.count('!') + text.count(';') + text.count(':') + \
            text.count('(') + text.count(')')
    
    return total

