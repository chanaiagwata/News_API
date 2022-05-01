class Sources:
    '''
    Sources class to define Sources objects
    '''
    def __init__(self, name, description, url):
        self.name=name
        self.description=description
        self.url=url
        
class Articles:
    '''
    Articles class to define Articles objects
    '''
    
    def __init__(self, source, title, author, description, urlToImage, publishedAT, url):
        self.source=source
        self.title=title
        self.author=author
        self.description=description
        self.urlToImage=urlToImage
        self.publishedAT=publishedAT
        self.url=url
    
