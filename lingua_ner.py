import requests
import codecs
import time

SERVER_PATH = "http://api.italianlp.it"
INPUT_FILE = '/Users/fnascime/Documents/Sicily_Project/texts/lontano.txt'
text = codecs.open(INPUT_FILE, 'r', 'utf-8').read()

start_time = time.time()

# Loading document
r = requests.post(SERVER_PATH + '/documents/',
                  data={'text': text,
                        'lang': "IT",
                        'extra_tasks': ["syntax"]})
id_doc = r.json()['id']

result = requests.get(SERVER_PATH + '/documents/actions/named-entity/%s' % id_doc)
json_value = result.json()

print(json_value)

result = requests.get(SERVER_PATH + '/documents/details/%s' % id_doc)
json_value = result.json()

total = json_value['sentences']['count']

print(total)

for i in range(total):
    if (json_value['sentences'] ['data'][i]['tokens'][0]['named_entity_instance'] != None):
        print( json_value['sentences'] ['data'][i]['tokens'][0]['named_entity_instance'])
        print(json_value['sentences']['data'][i]['tokens'][0]['word'])

print (json_value)


