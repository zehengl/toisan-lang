import datetime
import operator

from lrparsing import Grammar, Prio, Ref, Token, TokenRegistry, Tokens


class ToisanGrammar(Grammar):
    """
    The toisan-lang grammar
    """

    class T(TokenRegistry):
        number1 = Token(re="[0-9]+")
        number1["eval"] = lambda node: int(node[1])

        number2 = Token(re=r"[零一二三四五六七八九十]")
        number2["eval"] = lambda node: {
            "零": 0,
            "一": 1,
            "二": 2,
            "三": 3,
            "四": 4,
            "五": 5,
            "六": 6,
            "七": 7,
            "八": 8,
            "九": 9,
            "十": 10,
        }[node[1]]

        now = Token("丐时")
        now["eval"] = lambda _: datetime.datetime.now()

        true = Token(re=r"[真对]")
        true["eval"] = lambda _: True

        false = Token(re=r"[假错]")
        false["eval"] = lambda _: False

    expression = Ref("expression")

    truth = expression >> "岩唔岩啊"
    truth["eval"] = lambda node: operator.truth(node[1])

    greater_than = expression >> "大过" >> expression
    less_than = expression >> "细过" >> expression
    add = expression >> "加" >> expression
    subtract = expression >> "减" >> expression
    multiply = expression >> "乘" >> expression
    divide = expression >> "除以" >> expression
    binary_op = {
        "大过": operator.gt,
        "细过": operator.lt,
        "加": operator.add,
        "减": operator.sub,
        "乘": operator.mul,
        "除以": operator.truediv,
    }
    eval_binary_op = lambda node: ToisanGrammar.binary_op[node[2]](node[1], node[3])
    greater_than["eval"] = eval_binary_op
    less_than["eval"] = eval_binary_op
    add["eval"] = eval_binary_op
    subtract["eval"] = eval_binary_op
    multiply["eval"] = eval_binary_op
    divide["eval"] = eval_binary_op

    add_one = expression >> "多伱"
    subtract_one = expression >> "少伱"
    increment_op = {"多伱": operator.add, "少伱": operator.sub}
    eval_increment_op = lambda node: ToisanGrammar.increment_op[node[2]](node[1], 1)
    add_one["eval"] = eval_increment_op
    subtract_one["eval"] = eval_increment_op

    expression = Prio(
        (T.true | T.false | T.number1 | T.number2 | T.now),
        add_one,
        subtract_one,
        add,
        subtract,
        multiply,
        divide,
        (greater_than | less_than),
        truth,
    )

    START = expression

    @classmethod
    def eval_node(cls, node):
        return node[1] if "eval" not in node[0] else node[0]["eval"](node)
