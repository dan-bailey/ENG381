## This script analyzes a text file using the Shannon Entropy library.

## get the lirbraries loaded
from collections import Counter
from math import log

## make the Shannon function
def shannon(string):
    counts = Counter(string)
    frequencies = [i/len(string) for i in counts.values()]
    return - sum(f * log(f, 2) for f in frequencies)


## load the contents of a text file into a string
with open("written-sources-shannon.txt", "r") as words:
    lines = words.read()

## split the lines into a list of characters
analysisPacket = [*lines]

## Shannon Entropy
print("Shannon Entropy: ", shannon(analysisPacket))


