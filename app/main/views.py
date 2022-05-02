from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_sources,get_allArticles,get_headlines
from ..models import Sources, Articles

#views
@main.route('/')
def index():
    
    #getting sources
    business_sources = get_news_sources('business')
    sports_sources = get_news_sources('sports')
    technology_sources = get_news_sources('technology')
    entertainment_sources = get_news_sources('entertainment')
    
    title = "News Break"
    
    return render_template('index.html', title = title, business = business_sources, sports = sports_sources, technology  = technology_sources, entertainment = entertainment_sources)


    



