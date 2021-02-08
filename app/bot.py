from app.cleaner import Cleaner
from app.wiki import Wiki_requests
from app.gmaps import Gmaps_requests


cleaner = Cleaner()
wiki_requests = Wiki_requests()
gmaps_requests = Gmaps_requests()


class Bot:
    """Contain methods to bot response."""

    def __init__(self):
        """Initialise."""
        self.conversation = {}
        self.conversation["salutation"] = ["Bien le bonjour !", "Bonjour mon petit ! "]
        self.conversation["incompréhension"] = [
            "Ton jargon m'est inconnu, tu peux reformuler ?"
        ]
        self.conversation["introduce_wiki"] = ["Hmm... Je me rappel de ceci."]

    def is_it_a_place(self, entry: str) -> dict:
        """Check if user entry allows to find a place."""
        reply = {}
        cleaned = cleaner.stop_word(entry)
        gmaps_response = gmaps_requests.search_place(cleaned)
        if gmaps_response["status"] == "ZERO_RESULTS":
            reply["data"] = False
            reply["message"] = self.conversation["incompréhension"]
        else:
            reply["data"] = True
            reply["map"] = self.formate_map(gmaps_response)
            coord = str(reply["map"]["lat"]) + "|" + str(reply["map"]["lng"])
            reply["wiki"] = self.wiki_answer(coord)
            print(reply)

        return reply

    def wiki_answer(self, cleaned: str) -> str:
        """Use wiki methods to return a response."""
        wiki_result = wiki_requests.search_page(cleaned)
        wiki_response = wiki_requests.get_resume(wiki_result)
        return wiki_response

    def formate_map(self, gmaps_response: str) -> dict:
        """Use gmaps methods to return a response."""
        reply = {}
        reply["address"] = gmaps_response["candidates"][0]["formatted_address"]
        reply["lat"] = gmaps_response["candidates"][0]["geometry"]["location"]["lat"]
        reply["lng"] = gmaps_response["candidates"][0]["geometry"]["location"]["lng"]
        return reply
