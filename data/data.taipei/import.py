import json
from pymongo import MongoClient

if __name__ == '__main__':

    f = open('taipei.json') 
    
    j = json.load(f)

    db = MongoClient('localhost',3001).meteor
    source = 'data.taipei'
    db.resources.remove({'source': source})

    for r in j['result']['results']:
        r['meta'] = r['title']
        r['source'] = source
        id = r['id']
        for resource in r['resources']:
            if 'resourceId' in resource and 'format' in resource and len(resource['format']) > 0:
                pass
            else:
                continue
            link = 'http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid='+resource['resourceId']

            
            for format in ['json', 'xml', 'csv']:
                doc = r.copy()
                if 'resourceName' in resource:
                    doc['meta'] = doc['meta'] + ' ' + resource['resourceName']
                doc['link'] =  link
                if format != 'json':
                    doc['link'] = doc['link'] + '&format=' + format
                doc['format'] = format
                db.resources.insert(doc)
