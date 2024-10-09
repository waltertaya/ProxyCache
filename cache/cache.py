import redis
import ast

import dotenv
import os

dotenv.load_dotenv()

r = redis.Redis(
  host=os.getenv('REDIS_HOST'),
  port=os.getenv('REDIS_PORT'),
  password=os.getenv('REDIS_PASSWORD')
  )

class Cache:
    ''' Uses Redis as a cache for the cache proxy server '''
    def __init__(self):
        ''' Initializes the cache '''
        self.cache = r

    def exists(self,url):
        ''' Checks if the url exists in the cache '''
        return self.cache.exists(url)
    
    def get(self,url):
        ''' Gets the url from the cache '''
        bytes_obj = self.cache.get(url)
        cached = ast.literal_eval(bytes_obj.decode('utf-8'))
        return cached
    
    def set(self,url,response):
        ''' Sets the url in the cache '''
        self.cache.set(url, str(response))

    def clear(self):
        ''' Clears the cache '''
        self.cache.flushall()
