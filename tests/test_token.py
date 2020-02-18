import datetime
from unittest.mock import patch

import pytest

from toisan_lang.grammar import ToisanGrammar


@pytest.mark.parametrize(
    "token, value",
    [
        ("零", 0),
        ("一", 1),
        ("二", 2),
        ("三", 3),
        ("四", 4),
        ("五", 5),
        ("六", 6),
        ("七", 7),
        ("八", 8),
        ("九", 9),
        ("十", 10),
        ("0", 0),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("10", 10),
        ("真", True),
        ("对", True),
        ("假", False),
        ("错", False),
    ],
)
def test_toisan_lang_token_int_and_bool(token, value):
    assert ToisanGrammar.parse(token, ToisanGrammar.eval_node) == value


@patch("toisan_lang.grammar.datetime")
def test_toisan_lang_token_now(_datetime):
    now = datetime.datetime.now()
    _datetime.datetime.now.return_value = now
    assert ToisanGrammar.parse("丐时", ToisanGrammar.eval_node) == now
