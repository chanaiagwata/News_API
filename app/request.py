from concurrent.futures import process
import urllib.request,json
from .models import Sources,Articles

# Getting api key
api_key = None
#Getting base url
sources_base_url = None
#Getting the Sources base url
source_base_url = None
#Getting the everything base url
everything_base_url = None
#Getting the headlines base url
headlines_base_url = None



# Functions that take in application instance and replaces the None values above with configuration objects
def configure_request(app):
    global api_key,sources_base_url,source_base_url,everything_base_url,headlines_base_url
    api_key  = app.config['NEWS_API_KEY']
    sources_base_url = app.config['NEWS_BASE_SOURCES_URL']
    source_base_url = app.config['NEWS_BASE_SOURCE_URL']
    everything_base_url = app.config['NEWS_BASE_EVERYTHING_URL']
    headlines_base_url = app.config['NEWS_BASE_HEADLINES_URL']

def get_news_sources(category):
    '''
    Function that gets json response to our url request
    '''
    get_news_url  = sources_base_url(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response= json.loads(get_news_data)
        
        news_source_results = None
        
        if get_news_response['sources']:
            news_source_results_list = get_news_response['sources']
            news_source_results = process_results(news_source_results_list)
            
    return news_source_results

#processing results
def process_results(source_list):
    '''
    Function  that processes the news source result and transform them to a list of Objects
    
    Args:
        source_list: A list of dictionaries that contain news source details
    Returns:
        news_source_results: A list of news source objects
    '''

    news_source_results = []
    for source_item in source_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        
        if name:
            source_object = Sources(name,description,url)
            news_source_results.append(source_object)
    
    return news_source_results
    





