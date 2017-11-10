
lista = []
lista.append(int(id_doc))
print(lista)


# JSON Output
r = requests.post(SERVER_PATH + '/documents/named_entity_extraction/',
                  data={'doc_ids': lista})

print(r)


id_doc_ner = r.json()['id']

result = requests.get(SERVER_PATH + '/documents/named-entity-extraction/%s' % id_doc_ner)
json_value = result.json()

print (json_value)

