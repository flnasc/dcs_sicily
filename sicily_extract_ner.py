import sys
import json
import codecs
import glob
import os

json_value = ""

files = glob.glob("/Users/fnascime/Dev/python_projects/Sicily/results/*_tagged.txt")

for file in files:

    outfilename = os.path.splitext(file)[0] + "_places.txt"
    outfilename = outfilename.replace(" ","")
    print(outfilename)

    sentencesfilename = os.path.splitext(file)[0] + "_geo_sentences.txt"
    sentencesfilename = sentencesfilename.replace(" ","")

    sentencesfile = open(sentencesfilename, 'w')
    outfile = open(outfilename, 'w')

    with open(file, 'r') as infile:
        json_value = json.load(infile)

    outfile.write("\n==== Places in the file ====\n")

    for sentence in json_value['sentences']['data']:
        toks = []
        sent = []
        has_place = False
        for i,t in enumerate(sentence['tokens']):
            #print("Index: " + str(i))

            sent.append(t['word'] + ' ')
            val = ""

            if t['named_entity_instance'] != None:
                if t['named_entity_instance']['entity_type'] == "GPE":
                    val = t['word']
                    has_place = True

            #val = "" if t['named_entity_instance'] is None else t['word'] \
            #                                                           + " ENTITY:" + t['named_entity_instance'][
            #                                                               'entity_type']
            if (val != ""):
                toks.append(val.strip() + '\n')

        if (has_place):
            sentencesfile.write("".join(sent) + '\n\n')

        outfile.write("".join(toks))


    outfile.close()
    sentencesfile.close()
    infile.close()
