import pytest

from toisan_lang import ToisanCompiler, ToisanGrammar

from .testcases.compiler.assign_statement import data as data_assign_statement


@pytest.mark.parametrize("program, transpiled", data_assign_statement)
def test_assign_statement(program, transpiled):
    toisan_compiler = ToisanCompiler()
    tree_factory = toisan_compiler.tree_factory
    _ = ToisanGrammar.parse(program, tree_factory=tree_factory)
    print(toisan_compiler.compiled())
    assert transpiled == toisan_compiler.compiled()
