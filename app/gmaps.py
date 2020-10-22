import requests
from dotenv import load_dotenv
load_dotenv()
import os

class Gmaps_requests:

    def __init__(self):
        self.key = os.getenv("GMAPS_KEY")
        self.params = {'query': '123+main+street', 'key': self.key}

    def search_place(self):
        result =[]
        r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json', self.params)
        result = r.json()
        return result
    
    def get_place(self):
        pass
