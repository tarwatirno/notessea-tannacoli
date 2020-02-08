# coding: utf-8
import numpy as np
from collections import Counter
import pprint

pp = pprint.PrettyPrinter(indent=4)
with open("clean.txt") as file:
    contents = file.read()

characters = set(contents)
table = {}
np.random.seed(76)
for c in characters:
    table[c] = np.random.choice([-1, 1], size=(100000,))
counts = Counter(contents)

est_counts = np.zeros(100000)
for c in contents:
    est_counts = np.add(est_counts, table[c])

# In[73]:
freq_est = {}
for c in table:
    est_count = np.dot(est_counts, table[c])
    freq_est[c] = (est_count, counts[c])

pp.pprint(freq_est)
