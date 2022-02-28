from unicodedata import category
from app import app
import urllib.request,json
from .models import news,articles


News = news.News
Articles = articles.Article
#geting the apikey 
apiKey = '3b107a99439c4eb6bdd954f519de17cd'
# Getting the movie base url
base_url = app.config["NEWS_SOURCE_URL"]
article_base_url = app.config["ARTICLES_URL"]

def get_newsource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsource_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsource_response = json.loads(get_newsource_data)

        news_results = None

        if get_newsource_response['sources']:
            news_sources_list = get_newsource_response['sources']
            news_results = process_results(news_sources_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
 

        if url:
            news_object = News(id,name,description,url,category)
            news_results.append(news_object)

    return news_results

def get_news(id):
    get_news_details_url = base_url.format(id,apiKey)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            category = news_details_response.get('category')
            

            news_object = News(id,name,description,url,category)

    return news_object

def get_articles(newsource_id):
    article_url = article_base_url.format(newsource_id ,apiKey)
    with urllib.request.urlopen(article_url) as url:
        article_details = url.read()
        article_response = json.loads(article_details)

        article_results= None

        if article_response['articles']:
            article_results_list = article_response['articles']
            article_results = process_result(article_results_list)

    return article_results

def process_result(article_list):
    '''function to process article results'''
    article_results = []
    for articles in article_list:
        author = articles.get('author')
        title = articles.get('title')
        description = articles.get('description')
        url = articles.get('url')
        urlToImage = articles.get('urlToImage')
        publishedAt = articles.get('publishedAt')
        content = articles.get('content')
        
        article_object = Articles(author,title,  description, url, urlToImage, publishedAt, content)
        article_results.append(article_object)
    return article_results