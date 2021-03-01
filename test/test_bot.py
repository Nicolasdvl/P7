from ..app.bot import Bot
import pytest


bot = Bot()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Je voudrais visiter la Tour Eiffel", True),
        ("hhzzhhzhhh", False),
        ("SALUT SAI   KOI  OPENCLASSROMS", True),
        (
            "Arthur ne savait pas trop quelle disparition il remarqua d'abord",
            False,
        ),
        ("", False),
        ("Mais ! Qu'est-ce donc que la gare d'Hyères ?", True),
    ],
)
def test_is_it_a_place_data(test_input, expected):
    """Test integration of cleaner and if API requests succeed."""
    result = bot.is_it_a_place(test_input)
    assert result["data"] == expected


@pytest.mark.parametrize(
    "test_input",
    [
        ("Je voudrais visiter la Tour Eiffel"),
        ("hhzzhhzhhh"),
        ("SALUT SAI   KOI  OPENCLASSROMS"),
        ("Arthur ne savait pas trop quelle disparition il remarqua d'abord"),
        (""),
        ("Mais ! Qu'est-ce donc que la gare d'Hyères ?"),
    ],
)
def test_is_it_a_place_dict(test_input):
    """Test format return according to API response."""
    result = bot.is_it_a_place(test_input)
    if result["data"]:
        assert (
            type(result.get("map")) == dict
            and type(result.get("wiki")) == str
            and result.get("message") is None
        )
    else:
        assert (
            result.get("map") is None
            and result.get("wiki") is None
            and type(result.get("message")) == list
        )
