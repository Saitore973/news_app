from flask import render_template, request, url_for, redirect
from . import main
from ..requests import get_sources, get_articles
# from ..models import Source

@main.route('/')
def home():
    return render_template('home.html')
@main.route('/sources')
def index():
    general = get_sources()
    return render_template('index.html', message = general)

# @main.route('/articles/<source_id>')
# def articles(source_id):
#     get_id = get_sources()
#     id = get_id.id
#     articles = get_articles(id)

#     return render_template('artices.html',articles = articles)

@main.route('/about/<source_id>')
def about(source_id):   
    # get_id = get_sources()
    articles = get_articles(source_id)
    return render_template('about.html', articles = articles)