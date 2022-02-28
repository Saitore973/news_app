# import urllib.request,json
import requests as rq
from .models import Source,Articles

api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']

def get_sources():
    '''
    A function that requests for data and processes it
    '''
    with rq.get(base_url.format(api_key)) as data:
        data = data.json()
        source_list = data.get('sources')
        source_results = []
        for source in source_list:
            id = source.get('id')
            name = source.get('name')
            source_object = Source(id, name)
            source_results.append(source_object)
        return source_results

#     with urllib.request.urlopen(base_url.format(api_key)) as url:
#         get_url_data = url.read()
#         get_source_response = json.loads(get_url_data)

#         source_results = None
#         if get_source_response['sources']:
#             source_list = get_source_response['sources']
#             source_results = process_result(source_list)

#         return source_results

# def process_result(source_list):
#     '''Function  that processes the source result and transform them to a list of Objects

#     Args:
#         source_list: A list of dictionaries that contain movie details

#     Returns :
#         source_results: A list of movie objects
#     '''
#     source_results = []

#     for item in source_list:
#         id = item.get('id')
#         name = item.get('name')
#         source_object = Source(id, name)
#         source_results.append(source_object)

#         return source_results
def get_articles(source):
    '''
    A function that returns a list of articles
    Arg:
        source id 
    '''
    with rq.get(article_url.format(source,api_key)) as data:
        data = data.json()
        articles_list = data.get('articles')
        article_results = []
        for artic in articles_list:
            publishedAt = artic.get('publishedAt')
            urlToImage=artic.get('urlToImage')
            title = artic.get('title')
            content = artic.get('content')
            author = artic.get('author')
            url = artic.get('url')
            article_object = Articles(publishedAt,urlToImage,title,content,author,url)
            article_results.append(article_object)
      
        return article_results
