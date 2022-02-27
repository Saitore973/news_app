from flask import render_template
from app import app
from .request import get_newsource

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

@app.route('/news/<int:news_id>')
def news(news_id):
    '''view news page function that returns the news page and its data
    '''
    return render_template('news.html',id = news_id)