import urllib.request,json
from .models import Sources,Articles

# Getting api key
api_key = None
#Getting base url
base_url = None
#Getting the Sources base url
source_base_url = None
#Getting the everything base url
everything_base_url = None
#Getting the headlines base url
headlines_base_url = None



# Functions that take in application instance and replaces the None values above with configuration objects
def configure_reques(app):
    global api_key,sources_base_url,articles_base_url
    api_key  = app.config['NEWS_API_KEY']





