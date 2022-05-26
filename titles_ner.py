import pickle

with open("data.pickle","rb") as f:
  data = pickle.load(f)

for d in data[:1]:
  entities = d['ne_sub']
  for entity in entities:
    if entity['category'] == 'PRICE' or entity['category'] == 'AMOUNT':
      print(entity)
