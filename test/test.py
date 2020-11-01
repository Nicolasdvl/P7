import pytest
import requests
from ..app.wiki import Wiki_requests


class MockResponse(object):
    """Generate fake response."""

    def json(self):
        """Fake json resposne."""
        return {
            "query": {
                "search": [{"title": "found", "pageid": 123456}],
                "pages": [
                    {
                        "title": "Lorem ipsum",
                        "extract": "Lorem ipsum dolor sit amet,",
                    }
                ],
            }
        }


# instance à tester
wiki = Wiki_requests()


def test_search_page(monkeypatch):
    """Test search_page."""

    def get_mock(url, params):
        return MockResponse()

    monkeypatch.setattr(requests, "get", get_mock)
    assert wiki.search_page("search") == ("found")


def test_get_resume(monkeypatch):
    """Test get_resume."""

    def get_mock(url, params):
        return MockResponse()

    monkeypatch.setattr(requests, "get", get_mock)
    assert wiki.get_resume("title") == ("Lorem ipsum dolor sit amet,")
