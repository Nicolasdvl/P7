import pytest
import requests
from ..app.gmaps import Gmaps_requests


class MockResponse(object):
    """Generate fake response."""

    def json(self):
        """Fake json response."""
        return {
            "candidates": [
                {
                    "formatted_address": "10 Quai de la Charente,"
                    + " 75019 Paris, France",
                    "geometry": {
                        "localisation": {"lat": 48.8975156, "lng": 2.3833993}
                    },
                }
            ],
            "status": "OK",
        }


gmaps = Gmaps_requests()


def test_search_place(monkeypatch):
    """Test search_place."""

    def get_mock(url, params):
        return MockResponse()

    monkeypatch.setattr(requests, "get", get_mock)
    result = gmaps.search_place("search")
    assert (result["candidates"][0]["formatted_address"]) == (
        "10 Quai de la Charente, 75019 Paris, France"
    )
