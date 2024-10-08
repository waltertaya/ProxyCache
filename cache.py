class Cache:
    ''' Implements a cache for the cache proxy server '''
    def __init__(self):
        ''' Initializes the cache '''
        self.cache = {}
    
    def exists(self,url):
        ''' Checks if the url exists in the cache '''
        return url in self.cache
    
    def get(self,url):
        ''' Gets the url from the cache '''
        return self.cache.get(url)
    
    def set(self,url,response):
        ''' Sets the url in the cache '''
        self.cache[url] = response

    def clear(self):
        ''' Clears the cache '''
        self.cache = {}
