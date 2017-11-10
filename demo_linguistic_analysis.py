import requests
import codecs
import time

SERVER_PATH = "http://api.italianlp.it"
INPUT_FILE = '/Users/fnascime/Documents/Sicily_Project/texts/lampedusa_il_gattopardo.txt'
text = codecs.open(INPUT_FILE, 'r', 'utf-8').read()

start_time = time.time()

# Loading document
r = requests.post(SERVER_PATH + '/documents/',
                  data={'text': text,
                        'lang': "IT",
                        'extra_tasks': ["syntax"]})
print(r)

id_doc = r.json()['id']
# JSON Output
result = requests.get(SERVER_PATH + '/documents/details/%s' % id_doc)
json_value = result.json()

print (json_value)

# CONLL Output
result = requests.get(SERVER_PATH + '/documents/details/%s' % id_doc,
                        {'requested_output': "conll",
                         'conll_level': "parsed"})

print (result.json()['output'])
