import requests
import codecs
import time
import sys

SERVER_PATH = "http://api.italianlp.it"
INPUT_FILE = '/Users/fnascime/Documents/Sicily_Project/texts/lampedusa_il_gattopardo.txt'
text = codecs.open(INPUT_FILE, 'r', 'utf-8').read()
start_time = time.time()

# Loading document, requesting both syntax and named_entity tasks
r = requests.post(SERVER_PATH + '/documents/',
                  data={'text': text,
                        'lang': "IT",
                        'async': "true",
                        'extra_tasks': ["syntax", "named_entity"]})
id_doc = r.json()['id']
page = 1

outfile = codecs.open("out.txt", 'w', 'utf-8')

while True:
  result = requests.get(SERVER_PATH + '/documents/details/%s?page=%s' % (id_doc, page))
  json_value = result.json()

  # WAITING FOR COMPLETE EXECUTION OF TASKS
  if not json_value['parsing_executed'] and not json_value['named_entity_executed']:
    print ("WAITING FOR RESULTS...")
    time.sleep(15)
    continue
  # ALL TASKS COMPLETED
  outfile.write("\n==== NEW PAGE====\n")
  for sentence in json_value['sentences']['data']:
    toks = []
    for t in sentence['tokens']:
      val = t['word'] if t['named_entity_instance'] is None else t['word'] \
        + " ENTITY:" + t['named_entity_instance']['entity_type']
      toks.append(val)
    outfile.write(" ".join(toks) + "\n")
  if json_value['sentences']['next']:
    # FETCH NEW PAGE
    page += 1
  else:
    # NOTHING MORE TO FETCH
    break
