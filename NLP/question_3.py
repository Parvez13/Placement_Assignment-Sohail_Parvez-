import yake 
import csv 

with open('data_science.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    next(csv_reader)
    for row in csv_reader:
        texts = row[0]

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(texts)
for kw, _ in keywords:
  print(kw)