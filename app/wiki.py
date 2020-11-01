import requests


class Wiki_requests:
    """Contain requests of API wikipedia."""

    def __init__(self):
        """Initialise."""
        self.url = "https://fr.wikipedia.org/w/api.php"

    def search_page(self, wanted: str) -> str:
        """Return a title of a existante wiki page."""
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": wanted,
        }
        response = requests.get(self.url, params)
        data = response.json()
        page_title = data["query"]["search"][0].get("title")
        if page_title is None:
            print("page not found")
        return page_title

    def get_resume(self, page_title: str) -> str:
        """Return a resume of wiki page."""
        params = {
            "action": "query",
            "prop": "extracts",
            "exsentences": "15",
            "exlimit": "1",
            "titles": page_title,
            "explaintext": "1",
            "formatversion": "2",
        }
        response = requests.get(self.url, params)
        data = response.json()
        text = data["query"]["pages"][0].get("extract")
        return text
