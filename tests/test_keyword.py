from toisan_lang.keyword import ToisanKeyword, keywords


def test_keywords():
    assert set(keywords) == set(
        ""
        + ToisanKeyword._and_
        + ToisanKeyword._elif_
        + ToisanKeyword._else_
        + ToisanKeyword._if_
        + ToisanKeyword._in_
        + ToisanKeyword._or_
        + ToisanKeyword._print_
        + ToisanKeyword.add
        + ToisanKeyword.add_one
        + ToisanKeyword.as_long_as
        + ToisanKeyword.assign
        + ToisanKeyword.dict_init
        + ToisanKeyword.divide
        + ToisanKeyword.dot_notation
        + ToisanKeyword.greater_than
        + ToisanKeyword.inverse_divide
        + ToisanKeyword.less_than
        + ToisanKeyword.multiply
        + ToisanKeyword.now
        + ToisanKeyword.print_ending
        + ToisanKeyword.re_ending
        + ToisanKeyword.re_false
        + ToisanKeyword.re_number
        + ToisanKeyword.re_true
        + ToisanKeyword.subtract
        + ToisanKeyword.subtract_one
        + ToisanKeyword.then
        + ToisanKeyword.truth
    )
