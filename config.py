import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_BASE_SOURCE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/everything?domains={}&apiKey={}'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
