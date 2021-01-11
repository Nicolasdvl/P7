import requests


class Wiki_requests:
    """Contain requests of API wikipedia."""

    def __init__(self):
        """Initialise."""
        self.url = "https://fr.wikipedia.org/w/api.php"

    def search_page(self, coord: str) -> str:
        """Return a title of a existante wiki page."""
        params = {
            "action": "query",
            "format": "json",
            "list": "geosearch",
            "gsradius": "10000",
            "gscoord": coord,
        }
        response = requests.get(self.url, params)
        data = response.json()
        page_title = data["query"]["geosearch"][0].get("title")
        if page_title is None:
            print("page not found")
        return page_title

    def get_resume(self, page_title: str) -> str:
        """Return a resume of wiki page."""
        params = {
            "action": "query",
            "prop": "extracts",
            "exsentences": "5",
            "exlimit": "1",
            "titles": page_title,
            "explaintext": "1",
            "formatversion": "2",
            "format": "json",
        }
        response = requests.get(self.url, params)
        data = response.json()
        text = data["query"]["pages"][0].get("extract")
        return text
