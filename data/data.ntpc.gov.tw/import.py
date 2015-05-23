from pymongo import MongoClient

if __name__ == '__main__':

    db = MongoClient('localhost', 3001).meteor
    source = 'data.ntpc.gov.tw'
    rows = [
        {
            "meta": "新北市Wi-Fi熱點",
            "descriptionPage": "http://data.ntpc.gov.tw/od/detail?oid=CE74A94B-36D2-4482-A25D-670625ED0678",
            "format": "json",
            "link": "http://data.ntpc.gov.tw/od/data/api/04958686-1B92-4B74-889D-9F34409B272B?$format=json"
        },
        {
            "meta": "新北市Wi-Fi熱點",
            "descriptionPage": "http://data.ntpc.gov.tw/od/detail?oid=CE74A94B-36D2-4482-A25D-670625ED0678",
            "format": "csv",
            "link": "http://data.ntpc.gov.tw/od/data/api/04958686-1B92-4B74-889D-9F34409B272B?$format=csv"
        },
        {
            "meta": "新北市Wi-Fi熱點",
            "descriptionPage": "http://data.ntpc.gov.tw/od/detail?oid=CE74A94B-36D2-4482-A25D-670625ED0678",
            "format": "xml",
            "link": "http://data.ntpc.gov.tw/od/data/api/04958686-1B92-4B74-889D-9F34409B272B?$format=xml"
        }
    ]

    for row in rows:
        doc = row.copy()
        doc['source'] = source
        db.resources.insert(doc)

