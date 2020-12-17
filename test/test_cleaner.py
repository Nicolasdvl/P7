import pytest
from ..app.cleaner import Cleaner


cleaner = Cleaner()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Je voudrais visiter la Tour Eiffel", "Tour Eiffel"),
        (
            "Je vous transmets une adresse : 123 rue Bidon, Ville",
            "transmets adresse : 123 rue Bidon, Ville",
        ),
        (
            "Salut que pouvez vous faire pour moi dans l'immédiat ?",
            "Salut pouvez faire l'immédiat ?",
        ),
    ],
)
def test_stop_word(test_input, expected):
    """Test stop_word."""
    assert cleaner.stop_word(test_input) == expected
