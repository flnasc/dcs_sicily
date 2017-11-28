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

summaryfile = open("/Users/fnascime/Dev/python_projects/Sicily/results/adjectives_summary.txt",'w')

for file in files:

    outfilename = os.path.splitext(file)[0] + "_adjs_nouns.txt"
    outfilename = outfilename.replace(" ","")
    print(outfilename)

    outfile = open(outfilename, 'w')

    adjs = []
    total_tokens = 0
    noun_counting = 0
    adj_counting = 0


    with open(file, 'r') as infile:
        json_value = json.load(infile)

    outfile.write("\n==== Adjectives List ====\n")


    for sentence in json_value['sentences']['data']:

        found = False


        for i,t in enumerate(sentence['tokens']):

            total_tokens += 1

            #print("Index: " + str(i))

            if (t['cpos'] == 'S'):
                noun_counting += 1

            if (t['cpos'] == 'A'):
                #outfile.write(t['lemma'] + '  ')
                found = True
                adjs.append(t['lemma'])
                adj_counting += 1


        if (found):
            #outfile.write("\n\n")
            found = False

    adj_counts = Counter (adjs)

    summaryfile.write(outfilename +  ' ')
    #Total Adjectives
    summaryfile.write(str(total_tokens) + ' ')
    #Total Adjectives
    summaryfile.write(str(adj_counting) + ' ')
    #Total Nouns
    summaryfile.write(str(noun_counting) + '\n')
    #Average
    #summaryfile.write('Adjectives per noun ratio ' + str(adj_counting / noun_counting * 100) + '% \n\n')

    for keys, values in adj_counts.most_common():
        outfile.write(str(keys) + " ")
        outfile.write(str(values))
        outfile.write('\n')

    infile.close()
    outfile.close()

summaryfile.close()
