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

    def st_assign(self, compiler):
        var_list, exp_list = self.rhs[0], self.rhs[2]
        return [var_list.compiled, "=", exp_list.compiled]

    def st_print(self, compiler):
        return ["print(", self.rhs[1].compiled, ")"]

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

    pass
