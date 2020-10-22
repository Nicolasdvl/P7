import pytest
from ..app.wiki import *

class MockResponse(object):

    def json(self):
        return {'query': {'search': [{'title' : 'found', 'pageid': 123456}]}}

#instance à tester
wiki = Wiki_requests()

def test_search_page(monkeypatch):
    
    def get_mock(url, params):       
        return MockResponse()

    monkeypatch.setattr(requests, 'get', get_mock)
    assert wiki.search_page('search') == ('found')