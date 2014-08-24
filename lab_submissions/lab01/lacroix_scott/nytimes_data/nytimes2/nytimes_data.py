#! /usr/bin/env python
import sys
import json
import csv

out_file = open(sys.argv[2], 'w')
writer = csv.writer(out_file)
with open(sys.argv[1], 'r') as json_file:
    articles = json.load(json_file)
    writer.writerow(['pub_date', 'section', 'subsection', 'word_count', 'url']) 
    for article in articles['response']['docs']:
        writer.writerow([article['pub_date'], article['section_name'], 
            article['subsection_name'], article['word_count'], article['web_url']])

out_file.close()
