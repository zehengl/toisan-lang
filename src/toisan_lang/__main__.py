import argparse

from . import parse

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

transpiled, parse_tree = parse(program)

if show_tree:
    print("\nParse Tree:")
    print(parse_tree)

if show_code:
    print("\nTranspiled Python Code:")
    print(transpiled)

exec(transpiled)
