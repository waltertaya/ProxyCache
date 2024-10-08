import os
import requests
from flask import Flask, request, jsonify

from cache import Cache

def create_app():
    ''' Creates the Flask app '''
    app = Flask(__name__)
    cache = Cache()

    origin_server = os.getenv('ORIGIN_URL')

    @app.route('/<path:url>', methods=['GET'])
    def proxy(url):
        full_url = f'{origin_server}/{url}'

        if cache.exists(full_url):
            response = cache.get(full_url)
            print('X-Cache: HIT')
            return jsonify(response), 200, {'X-Cache': 'HIT'}

        response = requests.get(full_url)
        
        cache.set(full_url, response.json())

        print('X-Cache: MISS')

        return jsonify(response.json()), 200, {'X-Cache': 'MISS'}
    
    return app
