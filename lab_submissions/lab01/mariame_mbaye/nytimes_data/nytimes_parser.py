#! /usr/bin/env python
import sys
import json
import csv

# open file in write mode and create writer for csv format
out_file = open(sys.argv[2], 'w')
writer = csv.writer(out_file)

with open(sys.argv[1], 'r') as json_file:
    
    # load articles from json file
    articles = json.load(json_file)

    # write header row
    writer.writerow(['pub_date', 'section', 'subsection', 'word_count', 'url'])

    # parse json file and write data row by row
    for article in articles['response']['docs']:
        writer.writerow([article['pub_date'], article['section_name'], 
            article['subsection_name'], article['word_count'], article['web_url']])

# close file
out_file.close()
