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
parser.add_argument("--code", action="store_true", help="show the transpiled code")
args = parser.parse_args()

program = args.program
show_tree = args.tree
show_code = args.code

if show_tree and show_code:
    print("Flag --code is omitted.")

toisan_compiler = ToisanCompiler()
tree_factory = toisan_compiler.tree_factory
parse_tree = ToisanGrammar.parse(program, tree_factory=tree_factory)

if show_tree:
    print(ToisanGrammar.repr_parse_tree(parse_tree))
else:
    transpiled = toisan_compiler.compiled()
    if show_code:
        print(transpiled)
    exec(transpiled)
