import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey=3c34a2ef4db449d6a9d1f8926d14304c'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/everything?domains=findallarticlespublishedonthenextweb.com.&apiKey=3c34a2ef4db449d6a9d1f8926d14304c'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=3c34a2ef4db449d6a9d1f8926d14304c'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
