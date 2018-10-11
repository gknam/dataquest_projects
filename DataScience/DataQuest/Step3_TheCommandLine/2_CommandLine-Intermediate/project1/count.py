from collections import Counter, OrderedDict
from read import load_data
from sys import argv

import pandas as pd
import re

def printTop100HeadlineWords():
    """
    Prints 100 words which appear most often
    in headlines, in a descending order
    """
    
    # ensure no argument is provided in command line
    if len(argv) > 1:
        print("Usage: python count.py")
        return

    # read in dataset
    df = load_data()

    # concatenate all headlines separated by a space
    h_con = ""

    for val in df[df["headline"].notnull()]["headline"].values:
        h_con += val.lower() + " "

    # split concatenated headlines into a list of strings
    h_con_l = h_con.split()

    # strip non-word characters (including underscore)
    h_con_l = [string for string in h_con_l if re.match("\W|_", string) is None]

    # count number of occurences of each word in headlines
    count = Counter(h_con_l)

    # print 100 most often occuring words
    count_ordered = OrderedDict(sorted(count.items(), key=lambda t: t[1], reverse=True))

    c = 0
    for word, count in list(count_ordered.items()):
        print(word + ": " + str(count))
        c += 1
        if c == 100:
            break

if __name__ == "__main__":
    printTop100HeadlineWords()