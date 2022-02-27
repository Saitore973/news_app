from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='News app'
    message = 'Welcome to my news app!'
    return render_template('index.html',message = message, title=title)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''view news page function that returns the news page and its data
    '''
    return render_template('news.html',id = news_id)