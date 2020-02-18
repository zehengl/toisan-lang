import pytest

from toisan_lang.grammar import ToisanGrammar


@pytest.mark.parametrize(
    "expression, value",
    [
        # add
        ("一加一", 2),
        ("一加1", 2),
        ("1加一", 2),
        ("1加1", 2),
        # subtract
        ("二减一", 1),
        ("二减1", 1),
        ("2减一", 1),
        ("2减1", 1),
        # multiply
        ("二乘三", 6),
        ("二乘3", 6),
        ("2乘三", 6),
        ("2乘3", 6),
        # divide
        ("四除以二", 2),
        ("四除以2", 2),
        ("4除以二", 2),
        ("4除以2", 2),
        # greater than
        ("五大过4", True),
        ("4大过五", False),
        ("5大过5", False),
        # less than
        ("五细过4", False),
        ("4细过五", True),
        ("5细过5", False),
    ],
)
def test_expression_binary_op(expression, value):
    assert ToisanGrammar.parse(expression, ToisanGrammar.eval_node) == value
