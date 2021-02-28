import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Gmaps_requests:
    """Contain requests of gmaps API."""

    def __init__(self):
        """Initialise."""
        self.key = os.getenv("GMAPS_KEY")
        self.params = {
            "key": self.key,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
            "language": "fr",
        }

    def search_place(self, wanted: str) -> str:
        """Return an adress and a localisation of a place."""
        self.params["input"] = wanted
        r = requests.get(
            "https://maps.googleapis.com/maps/api/"
            + "place/findplacefromtext/json",
            self.params,
        )
        data = r.json()
        return data
