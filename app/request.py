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
    get_news_url  = sources_base_url.format(category,api_key)
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

def get_allArticles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = everything_base_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None
        
        if get_articles_response['articles']:
            articles_results_list = get_articles_response('articles')
            articles_results = process_results(articles_results_list)
            
        return articles_results
    
#processing articles results

def processs_results2(article_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects
    
    Args:
        article_list: A list of dictionaries that contain news source details
    Returns:
        articles_results: A list of articles objects
    '''
    articles_results = []
    
    for article_item in article_list:
        source = article_item.get('source')
        title = article_item.get('title')
        description = article_item.get('description')
        image = article_item.get('urlToImage')
        author = article_item.get('author')
        date = article_item.get('publishedAt')
        url = article_item.get('url')
        
        if image:
            article_object = Articles(source,title,description,image,author,date,url)
            articles_results.append(article_object)
    
    return articles_results
        
    





