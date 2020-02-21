import argparse

from . import ToisanCompiler, ToisanGrammar


parser = argparse.ArgumentParser(
    description=(
        "A programming language based on Toisanese"
        ", aka Taishanese, a dialect of Cantonese"
    )
)
parser.add_argument("program", type=str, nargs=1, help="program written in toisan-lang")
parser.add_argument("--tree", action="store_true", help="show the parse tree")
args = parser.parse_args()


if args.tree:
    pare_tree = ToisanGrammar.parse(args.program)
    print(ToisanGrammar.repr_parse_tree(pare_tree))
else:
    print(ToisanGrammar.parse(args.program, tree_factory=ToisanCompiler().tree_factory))
