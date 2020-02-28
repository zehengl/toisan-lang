import argparse

from lrparsing import ParseError

from . import ToisanCompiler, ToisanGrammar


parser = argparse.ArgumentParser(
    description=(
        "A programming language based on Toisanese"
        ", aka Taishanese, a dialect of Cantonese"
    )
)
parser.add_argument("program", type=str, nargs=1, help="program written in toisan-lang")
parser.add_argument("--show", type=str, nargs="+", help="show extra information")
args = parser.parse_args()

program = args.program
show = args.show or []

show_code, show_tree = False, False

if "code" in show:
    show_code = True

if "tree" in show:
    show_tree = True

other_options = set(show) - set(["code", "tree"])
if other_options:
    print(f"ignore invalid options: {other_options}")


toisan_compiler = ToisanCompiler()
tree_factory = toisan_compiler.tree_factory
try:
    parse_tree = ToisanGrammar.parse(program, tree_factory=tree_factory)
except ParseError:
    raise RuntimeError("唔知你讲么")

transpiled = toisan_compiler.compiled()

if show_tree:
    print("\nParse Tree:")
    print(ToisanGrammar.repr_parse_tree(parse_tree))

if show_code:
    print("\nTranspiled Python Code:")
    print(transpiled)

exec(transpiled)
