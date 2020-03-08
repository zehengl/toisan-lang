from lrparsing import Token

from .grammar import ToisanGrammar
from .keyword import ToisanKeyword as K


class ToisanNode(tuple):
    INDENT, OUTDENT = range(2)
    compiled = None
    data = None
    rhs = None
    rule = None

    class Data(object):
        def __init__(self, **kwds):
            self.__dict__.update(kwds)

    def __new__(cls, compiler, nodes):
        result = super(ToisanNode, cls).__new__(cls, nodes)
        result.rule = nodes[0]
        result.rhs = nodes[1:]
        result.data = None
        if not isinstance(result.rule, Token):
            name = result.rule.name
        else:
            name = result.rule.name.split(".")[-1]
            result.token = nodes[1]
        if name in cls.__dict__:
            result.compiled = cls.__dict__[name](result, compiler)
        elif isinstance(result.rule, Token):
            token = result.token
            if token == "，":
                token = ","
            result.compiled = (token,)
        elif len(nodes) == 2:
            result.compiled = nodes[1].compiled
        else:
            result.compiled = tuple(n.compiled for n in nodes[1:])
        assert result.compiled is not None, str(result.rule)
        return result

    def constant(self, compiler):
        rule = self.rhs[0].rule
        token = self.rhs[0].compiled[0]

        if rule is ToisanGrammar.T.string:
            result = f"'{token[1:-1]}'"
        elif token in K.re_number:
            result = {
                "零": "0",
                "一": "1",
                "二": "2",
                "三": "3",
                "四": "4",
                "五": "5",
                "六": "6",
                "七": "7",
                "八": "8",
                "九": "9",
                "十": "10",
            }[token]
        elif token in K.re_true:
            result = "True"
        elif token in K.re_false:
            result = "False"
        else:
            result = token

        return (result,)

    def _binary_op(self, op, left, right):
        if op == K.inverse_divide:
            left, right = right, left

        mapping = {
            K.add: "+",
            K.subtract: "-",
            K.multiply: "*",
            K.divide: "/",
            K.inverse_divide: "/",
            K.greater_than: ">",
            K.less_than: "<",
            K._and_: "and",
            K._or_: "or",
            K._in_: "in",
        }
        return tuple([left, mapping[op], right])

    def _unary_op(self, op, left):
        if op == K.truth:
            return tuple(["bool(", left, ")"])
        if op == K.add_one:
            return tuple([left, "+", "1"])
        if op == K.subtract_one:
            return tuple([left, "-", "1"])
        raise NotImplementedError(op)

    def exp(self, compiler):
        rule = self.rhs[0].rule
        rhs = self.rhs[0].rhs

        if len(rhs) == 3:
            return self._binary_op(rhs[1].token, rhs[0].compiled, rhs[2].compiled)
        elif len(rhs) == 2:
            return self._unary_op(rhs[1].token, rhs[0].compiled)
        elif rule is ToisanGrammar.now:
            return ("datetime.now()",)
        elif rule is ToisanGrammar.dict_init:
            return ("dict()",)

        return self.rhs[0].compiled

    def variable_ref(self, compiler):
        path = [self.rhs[i].token for i in range(0, len(self.rhs), 2)]
        compiled = path[0]
        for key in path[1:]:
            compiled += f"['{key}']"
        return (compiled,)

    def adjusted_exp(self, compiler):
        return ("(", self.rhs[1].compiled, ")")

    def st_assign(self, compiler):
        var_list, exp_list = self.rhs[0], self.rhs[2]
        return [var_list.compiled, "=", exp_list.compiled]

    def st_print(self, compiler):
        return ["print(", self.rhs[1].compiled, ")"]

    def st_if(self, compiler):
        compiled = []
        i = 0
        while i < len(self.rhs) and (
            self.rhs[i].token == K._if_ or self.rhs[i].token == K._elif_
        ):
            kwd, condition, scope = (self.rhs[i], self.rhs[i + 1], self.rhs[i + 3])
            ife = "if" if kwd.token == K._if_ else "elif"
            compiled.extend(
                [
                    [ife, condition.compiled, ":"],
                    self.INDENT,
                    scope.compiled,
                    self.OUTDENT,
                ]
            )
            i += 4
        if i < len(self.rhs) and self.rhs[i].token == K._else_:
            scope = self.rhs[i + 1]
            compiled.extend([["else:"], self.INDENT, scope.compiled, self.OUTDENT])
        return tuple(compiled)

    def st_as_long_as(self, compiler):
        condition, loop_scope = self.rhs[1], self.rhs[3]
        return (
            ["while", condition.compiled, ":"],
            self.INDENT,
            loop_scope.compiled,
            self.OUTDENT,
        )

    def block(self, compiler):
        result = tuple(s.compiled for s in self.rhs if not isinstance(s.rule, Token))
        if not result:
            result = ("pass",)

        return result

    def START(self, compiler):
        begin_program, block = self.rhs[0], self.rhs[1]

        return (
            ["from datetime import datetime"],
            [""],
            [""],
            ["def main():"],
            self.INDENT,
            # begin_program.data.scope.compile(),
            block.compiled,
            self.OUTDENT,
            [""],
            ["if __name__ == '__main__':"],
            self.INDENT,
            ["main()"],
            self.OUTDENT,
        )
