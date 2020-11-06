import pytest
from ..app.cleaner import Cleaner


cleaner = Cleaner()


def test_stop_word():
    """Test stop_word."""
    assert cleaner.stop_word("Sinon abord un chat") == "Sinon chat"
