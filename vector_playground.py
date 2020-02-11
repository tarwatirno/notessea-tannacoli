# coding: utf-8
import numpy as np
from collections import Counter
import pprint

pp = pprint.PrettyPrinter(indent=4)
with open("clean.txt") as file:
    contents = file.read()


counts = Counter(contents)
table = {}
np.random.seed(76)
for c in counts:
    table[c] = np.random.choice([-1, 1], size=(10000,))

def estimate_counts():
    counts_v = np.zeros(10000)
    for c in contents:
        counts_v = np.add(counts_v, table[c])

    freq_est = {}
    for c in table:
        est_count = np.dot(counts_v, table[c])
        freq_est[c] = (est_count, counts[c])

    pp.pprint(freq_est)

