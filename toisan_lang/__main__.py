import argparse

from . import ToisanGrammar


parser = argparse.ArgumentParser(
    description=(
        "A programming language based on Toisanese"
        ", aka Taishanese, a dialect of Cantonese"
    )
)
parser.add_argument(
    "program", type=str, nargs=1, help="the program written in toisan-lang"
)
args = parser.parse_args()

print(ToisanGrammar.parse(args.program))
