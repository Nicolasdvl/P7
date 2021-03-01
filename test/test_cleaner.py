import pytest
from ..app.cleaner import Cleaner


cleaner = Cleaner()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "Je voudrais visiter la Tour Eiffel.",
            "voudrais visiter tour eiffel",
        ),
        (
            "Je vous transmets une adresse : 123 rue Bidon, Ville",
            "transmets adresse 123 rue bidon ville",
        ),
        (
            "Salut que pouvez vous faire pour moi dans l'immédiat ?",
            "pouvez faire immédiat",
        ),
        ("Une  phrase   trop      espacé     .", "phrase espacé"),
        ("     :)     ", ""),
        ("$ some ? extra ;;symboLE !", "some extra symbole"),
    ],
)
def test_stop_word(test_input, expected):
    """Test stop_word."""
    assert cleaner.stop_word(test_input) == expected
