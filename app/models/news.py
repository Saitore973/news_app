from unicodedata import name


class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,category):
        self.id =id
        self.name = name
        self.description = description
        self.url = 'https://abcnews.go.com' + url
        self.category= category
        