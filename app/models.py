class Source:
    def __init__(self,id,name):
      self.id = id
      self.name = name

class Articles:
    def __init__(self, publishedAt, urlToImage,title,content,author,url):
      self.publishedAt = publishedAt
      self.urlToImage= urlToImage
      self.title = title
      self.content =content
      self.author = author
      self.url = url