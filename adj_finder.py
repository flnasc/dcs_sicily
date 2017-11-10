from nltk.corpus.reader import ConllCorpusReader
from collections import Counter
from collections import Counter

## This is the main dictionaty
a = {}


## Function to add an adjective to a noun key
def add_adj(noun_param, adj_param):
    if (noun_param in a):
        a[noun_param].append(adj_param)
    else:
        a[noun_param] = [adj_param]


filedir = '/Users/fnascime/Documents/Sicily_Project/texts/'
filename = 'ilgattopardo_prima'

mycorpus = ConllCorpusReader(filedir, filename + '.conll',
                             ('ignore', 'words', 'ignore', 'pos', 'ignore', 'ignore', 'ignore', 'ignore'))

words = mycorpus.tagged_words()
list_len = len(words)

## Loop through file and retrieve adjetives directly associated with nouns (adjunct words)
for i in range(list_len):

    if (words[i][1] == 'S'):
        if ((i > 0) and (words[i - 1][1] == 'A')):
            add_adj(words[i][0], words[i - 1][0])
        elif ((i < list_len - 1) and (words[i + 1][1] == 'A')):
            add_adj(words[i][0], words[i + 1][0])

## Loop throught the list of words and verify the ones with more adjective

nouns_counting = len(a)
adj_counting = 0

for key in a:
    adj_counting = adj_counting + len(a[key])

print('Total number of nouns     : ' + str(nouns_counting))
print('Total number of adjectives: ' + str(adj_counting))

average_adj = int(adj_counting / nouns_counting)

print('Average adjectives/noun.  : ' + str(average_adj))

for key in a:
    if (len(a[key]) > average_adj):
        print("\nSostantivo: " + key)
        print("Aggetivi: " + str(Counter(a[key])))
        # for adj in a[key]:
        #    print ()

# Counter (a['fernando'])

