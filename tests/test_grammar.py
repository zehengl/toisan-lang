import lrparsing

from toisan_lang.grammar import ToisanGrammar


def test_grammar_compilation():
    lrparsing.compile_grammar(ToisanGrammar)
