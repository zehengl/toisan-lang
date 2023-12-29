from lrparsing import (
    THIS,
    Grammar,
    List,
    Opt,
    Prio,
    Ref,
    Repeat,
    Token,
    TokenRegistry,
    Tokens,
)

from .keyword import ToisanKeyword as K
from .keyword import keywords


class ToisanGrammar(Grammar):
    """
    The toisan-lang grammar
    """

    class T(TokenRegistry):
        name = Token(re=rf"((?![{keywords}0-9])[a-zA-Z\u4e00-\u9fff])+")
        string = Token(re=r"“[^“”]*”")
        arabic_numeral = Token(re="[0-9]+")
        chinese_numeral = Token(re=rf"[{K.re_number}]")
        true = Token(re=rf"[{K.re_true}]")
        false = Token(re=rf"[{K.re_false}]")

    exp = Ref("exp")
    prefix_exp = Ref("prefix_exp")
    statement = Ref("statement")

    boolean = T.true | T.false
    number = T.arabic_numeral | T.chinese_numeral
    variable_ref = List(T.name, Token(K.dot_notation), min=1)
    subscript_exp = prefix_exp + "【" + exp + "】"
    var = variable_ref | subscript_exp
    var_list = List(var, "，", min=1)
    exp_list = List(exp, "，", min=1)

    block = Repeat(statement + Opt(Token(re=rf"[{K.re_ending}]")) + Tokens("。 ； ！"))
    begin_scope = THIS * 0
    end_scope = THIS * 0
    loop = THIS * 0
    begin_loop_scope = begin_scope + loop
    scope = begin_scope + block + end_scope
    loop_scope = begin_loop_scope + block + end_scope

    adjusted_exp = "（" + exp + "）"
    constant = boolean | number | T.string

    prefix_exp = Prio(adjusted_exp, var)

    dict_init = Token(K.dict_init)
    now = Token(K.now)
    truth = exp << Token(K.truth)
    greater_than = exp << Token(K.greater_than) << exp
    less_than = exp << Token(K.less_than) << exp
    add = exp << Token(K.add) << exp
    subtract = exp << Token(K.subtract) << exp
    multiply = exp << Token(K.multiply) << exp
    divide = exp << Token(K.divide) << exp
    inverse_divide = exp << Token(K.inverse_divide) << exp
    add_one = exp << Token(K.add_one)
    subtract_one = exp << Token(K.subtract_one)
    logic_and = exp << Token(K._and_) << exp
    logic_or = exp << Token(K._or_) << exp
    value_in = exp << Token(K._in_) << exp

    exp = Prio(
        constant,
        prefix_exp,
        now,
        dict_init,
        truth,
        multiply | divide | inverse_divide,
        add_one | subtract_one,
        add | subtract,
        greater_than | less_than,
        value_in,
        logic_and,
        logic_or,
    )

    st_assign = var_list + Token(K.assign) + exp_list

    st_if = (
        Token(K._if_)
        + exp
        + Token(K.then)
        + scope
        + Repeat(Token(K._elif_) + exp + Token(K.then) + scope)
        + Opt(Token(K._else_) + scope)
    )

    st_as_long_as = Token(K.as_long_as) + exp + Token(K.then) + loop_scope

    st_print = Token(K._print_) + (var | adjusted_exp) + Token(K.print_ending)

    statement = st_assign | st_if | st_print | st_as_long_as

    begin_program = begin_scope * 1
    end_program = end_scope * 1
    START = begin_program + block + end_program
