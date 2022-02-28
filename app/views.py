from flask import render_template
from app import app
from .request import get_newsource,get_news,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='News app'
    business_news = get_newsource('business')
    general_news = get_newsource('general')
    sports_news = get_newsource('sports')
    technology_news = get_newsource('technology')
    return render_template('index.html',business=business_news,general=general_news, sports=sports_news, technology=technology_news, title=title)

@app.route('/news/<newsource_id>')
def news(newsource_id):
    '''view news page function that returns the news page and its data
    '''
    article_source = get_articles('general')
    technology_source = get_articles('technology')
    business_source = get_articles('business')
    sports_source = get_articles('sports')


    title = f'{newsource_id} Articles'

    return render_template('news.html',title = title, name = newsource_id, articles = article_source,techn = technology_source, buss =business_source, sport = sports_source)

    # return render_template('news.html', title = title, article = article)
