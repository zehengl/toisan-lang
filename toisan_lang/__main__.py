import argparse

from . import ToisanGrammar


parser = argparse.ArgumentParser(
    description=(
        "A programming language based on Toisan Wah"
        ", aka Taishanese, a dialect of Cantonese"
    )
)
parser.add_argument("statements", type=str, nargs=1, help="toisan-lang statements")
args = parser.parse_args()

print(ToisanGrammar.parse(args.statements, ToisanGrammar.eval_node))
