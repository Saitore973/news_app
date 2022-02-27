from unicodedata import category
from app import app
import urllib.request,json
from .models import news

News = news.News
#geting the apikey 
api_key = app.config['NEWS_API_KEY']
# Getting the movie base url
base_url = app.config["NEWS_SOURCE_URL"]

def get_newsource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsource_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsource_response = json.loads(get_newsource_data)

        news_results = None

        if get_newsource_response['results']:
            news_results_list = get_newsource_response['results']
            news_results = process_results(news_results_list)


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