# coding: utf-8
import numpy as np
from collections import Counter
import pprint
pp = pprint.PrettyPrinter(indent=4)
import copy

with open("clean.txt") as file:
    doc = file.read()


counts = Counter(doc)
word_counts = Counter(doc.split())
table = {}
np.random.seed(76)
for c in counts:
    table[c] = np.random.choice([-1, 1], size=(10000,))

def estimate_counts():
    counts_v = np.zeros(10000)
    for c in doc:
        counts_v = np.add(counts_v, table[c])

    freq_est = {}
    for c in table:
        est_count = np.dot(counts_v, table[c])
        freq_est[c] = (est_count, counts[c])

    pp.pprint(freq_est)
    return counts_v

def ngrams(n):
    ngrams = np.zeros(10000)
    for i in range(n-1, len(doc)):
        for j in range(n-1, 0, -1):
            ngrams = np.add(np.roll(table[doc[i-j]], -j), ngrams)
    return ngrams
#ngrams = ngrams(4)

def skip3gram_table():
    skiptable = copy.deepcopy(table)
    skip3grams = np.zeros(10000)
    for i in range(2, len(doc)):
        c = doc[i-1]
        for j in [0, 2]:
            skiptable[c] = np.add(np.roll(table[doc[i-j]], -j), skiptable[c])
    return skiptable
#l_table = skip3gram_table()

def words(doc):
    words_vec = np.zeros(10000)
    i = 0
    for c in doc:
        if c == " ":
            #words_vec = np.add(np.roll(table[cb], i-l), words_vec)
            i = 0
        else:
            i += 1
        words_vec = np.add(np.roll(table[c], i), words_vec)
    return words_vec
profile = words(doc)

def count_word(word):
    return (np.dot(profile,words(word))/D, word_counts[word])
estimate_counts()
