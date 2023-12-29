import pytest
from compiler.as_long_as_statement import data as data_as_long_as_statement
from compiler.assign_statement import data as data_assign_statement
from compiler.if_statement import data as data_if_statement

from toisan_lang import parse

data = data_assign_statement + data_if_statement + data_as_long_as_statement


@pytest.mark.parametrize("program, expected", data)
def test_assign_statement(program, expected):
    transpiled, _ = parse(program)

    assert transpiled == expected
