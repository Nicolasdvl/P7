import requests

class Wiki_requests:

    def __init__(self):
        pass

    def search_page(self, wanted:str) -> str:
        url = "https://fr.wikipedia.org/w/api.php"
        params = {"action": "query", "format": "json", "list": "search", "srsearch": wanted}
        response = requests.get(url, params)
        data = response.json()
        page_title = data['query']['search'][0].get('title')
        if page_title == None:
            return print('page not found')
        return page_title

    def get_resume(self, page_title:str):
        pass
