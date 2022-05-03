from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_sources,get_allArticles,get_headlines
from ..models import Sources, Articles

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # getting sources
    business_sources = get_news_sources('business')
    sports_sources = get_news_sources('sports')
    technology_sources = get_news_sources('technology')
    entertainment_sources = get_news_sources('entertainment')
    
    # news_sources = get_news_sources('sources')
    
    title = "Breaking News"
    
    return render_template('index.html', title = title, business_sources = business_sources, sports_sources=sports_sources, technology_sources=technology_sources,entertainment_sources=entertainment_sources)

@main.route('/articles')
def articles():
    '''
    view article page
    '''
    articles = get_allArticles(id)
    return render_template("articles.html", id = id, articles = articles)

@main.route('/headlines')  
def headlines():
    '''
    view headline page
    '''
    #getting headlines
    headline_id = get_headlines('id')
    headline_name = get_headlines('name')
    
    title = 'Top Headlines'
    return render_template('headlines.html', title = title, headline_id= headline_id, headline_name=headline_name)
    



