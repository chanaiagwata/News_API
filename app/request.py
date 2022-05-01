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





