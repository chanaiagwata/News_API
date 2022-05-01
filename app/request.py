from urllib import request
import json


#testing api call
def get_sources():
    base_url= 'https://newsapi.org/v2/top-headlines/sources?apiKey=3c34a2ef4db449d6a9d1f8926d14304c'
    
    with request.urlopen(base_url) as url:
        get_sources_data = url.read()
        py_readable_urlData = json.loads(get_sources_data)
        
        print(py_readable_urlData)
        
get_sources()