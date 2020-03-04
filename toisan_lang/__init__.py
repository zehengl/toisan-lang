from lrparsing import ParseError, TokenError

from .compiler import ToisanCompiler
from .grammar import ToisanGrammar

toisan_compiler = ToisanCompiler()
tree_factory = toisan_compiler.tree_factory


def parse(program):
    try:
        parse_tree = ToisanGrammar.parse(program, tree_factory=tree_factory)
    except ParseError:
        raise RuntimeError("唔好意思！唔明你讲么！")
    except TokenError:
        raise RuntimeError("唔好意思！有乃字或者标点符号冇见过！")

    transpiled = toisan_compiler.compiled()
    parse_tree = ToisanGrammar.repr_parse_tree(parse_tree)

    return transpiled, parse_tree
