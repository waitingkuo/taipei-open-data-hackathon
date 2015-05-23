import csv
from datetime import datetime
from elasticsearch import Elasticsearch
from pymongo import MongoClient


if __name__ == '__main__':

    f = open('data.csv')
    csv_file = csv.reader(f)

    field_names = []
    lines = []
    for index, row in enumerate(csv_file):
        if index == 0:
            field_names = row
        lines.append(row)
        
    
    #es = Elasticsearch("192.168.59.103")
    #es.indices.create(index='data', ignore=400)
    
    db = MongoClient('localhost',3001).meteor
        
    #count = 0
    source = 'data.gov.tw'
    db.resources.remove({'source': source})
    #db.resources.remove({})
    for line in lines:
        doc = {}
        for i, field in enumerate(field_names):
            doc[field] = line[i] 
        #print(body)
        #body['analysis'] = {
        #    'analyzer': 'cjk'
        #}
        doc['meta'] = line[0]
        doc['link'] = line[2]
        doc['format'] = line[1]
        doc['source'] = source
        
        #es.index(index='data', doc_type='data', body=body)
        db.resources.insert_one(doc) 

        #count = count + 1
        #if count == 10: break
