import sys
import json
import codecs
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

files = glob.glob("/Users/fnascime/Dev/python_projects/Sicily/results/*_tagged.txt")

for file in files:

    outfilename = os.path.splitext(file)[0] + "_adj.txt"
    outfilename = outfilename.replace(" ","")
    print(outfilename)

    outfile = open(outfilename, 'w')

    with open(file, 'r') as infile:
        json_value = json.load(infile)

    outfile.write("\n==== Adjectives Counter ====\n")


    for sentence in json_value['sentences']['data']:

        toks = []
        list_len = len(sentence['tokens'])

        for i,t in enumerate(sentence['tokens']):

            #print("Index: " + str(i))

            if (t['cpos'] == 'S'):
                if ((i > 0) and (sentence['tokens'][i-1]['cpos'] == 'A')):
                    add_adj(t['word'], sentence['tokens'][i-1]['word'])
                elif ((i < list_len - 1) and (sentence['tokens'][i+1]['cpos'] == 'A')):
                    add_adj(t['word'], sentence['tokens'][i+1]['word'])


    ## Loop throught the list of words and verify the ones with more adjective

    nouns_counting = len(a)
    adj_counting = 0

    for key in a:
        adj_counting = adj_counting + len(a[key])

    outfile.write('Total number of nouns     : ' + str(nouns_counting) + '\n')
    outfile.write('Total number of adjectives: ' + str(adj_counting) + '\n')

    average_adj = int(adj_counting / nouns_counting)

    outfile.write('Average adjectives/noun.  : ' + str(average_adj) + '\n')

    for key in a:
        if (len(a[key]) > average_adj):
            outfile.write("\n\nSostantivo: " + key + '\n')
            outfile.write("Aggetivi: " + str(Counter(a[key])))
            # for adj in a[key]:
            #    print ()


    infile.close()
    outfile.close()
