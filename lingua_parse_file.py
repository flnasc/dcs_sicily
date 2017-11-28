import requests
import codecs
import time
import json
import sys

SERVER_PATH = "http://api.italianlp.it"
filename = 'lampedusa_il_gattopardo'
INPUT_FILE = '/Users/fnascime/Dev/python_projects/Sicily/data/' + filename + '.txt'
text = codecs.open(INPUT_FILE, 'r', 'utf-8').read()
start_time = time.time()

# Loading document, requesting both syntax and named_entity tasks
r = requests.post(SERVER_PATH + '/documents/',
                  data={'text': text,
                        'lang': "IT",
                        'async': "true",
                        #'extra_tasks': ["syntax"]})
                        'extra_tasks': ["syntax", "named_entity"]})
id_doc = r.json()['id']
page = 1

while True:
  result = requests.get(SERVER_PATH + '/documents/details/%s?page=%s' % (id_doc, page))
  json_value = result.json()

  # WAITING FOR COMPLETE EXECUTION OF TASKS
  if not json_value['parsing_executed'] and not json_value['named_entity_executed']:
    print ("WAITING FOR RESULTS...")
    time.sleep(15)
    continue

  # ALL TASKS COMPLETED - Write the output json to a file
  with open('/Users/fnascime/Dev/python_projects/Sicily/results/' + filename + '_tagged.txt', 'w') as outfile:
      json.dump(json_value, outfile)

  # Done writing the file
  break