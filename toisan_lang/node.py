from lrparsing import Token
from .keyword import ToisanKeyword as K
from .grammar import ToisanGrammar


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
            result.compiled = (result.token,)
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

    def adjusted_exp(self, compiler):
        exp = self.rhs[1]
        return exp.compiled

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

    def block(self, compiler):
        return tuple(s.compiled for s in self.rhs if not isinstance(s.rule, Token))

    def START(self, compiler):
        begin_program, block = self.rhs[0], self.rhs[1]

        return (
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
