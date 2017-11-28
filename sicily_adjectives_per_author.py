import json
from collections import Counter
import glob
import os

## This is the main dictionaty
a = {}


## Function to add an adjective to a noun key
def add_adj(noun_param, adj_param):
    if (noun_param in a):
        a[noun_param].append(adj_param)
    else:
        a[noun_param] = [adj_param]



json_value = ""

author = "pirandello"
#author = "lampedusa"
#author = "sciascia"
#author = "verga"

dir_name = "/Users/fnascime/Dev/python_projects/Sicily/data_by_author/"

files = glob.glob(dir_name + author + "/*.txt")


outfile = open(dir_name + author + "_adjectives.txt", 'w')

outfile.write("\n==== Adjectives Counter ====\n")

adjs = []
total_tokens = 0
noun_counting = 0
adj_counting = 0

for file in files:

    print(file)

    with open(file, 'r') as infile:
        json_value = json.load(infile)

    for sentence in json_value['sentences']['data']:

        toks = []
        list_len = len(sentence['tokens'])

        for i,t in enumerate(sentence['tokens']):

            total_tokens += 1


            if (t['cpos'] == 'S'):
                noun_counting += 1

            if (t['cpos'] == 'A'):
                adjs.append(t['lemma'])
                adj_counting += 1

adj_counts = Counter (adjs)

for keys, values in adj_counts.most_common():
    outfile.write(str(keys) + " ")
    outfile.write(str(values))
    outfile.write('\n')


infile.close()
outfile.close()
