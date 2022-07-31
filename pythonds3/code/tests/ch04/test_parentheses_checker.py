from src.ch04.symbol_checker import check_parentheses


def test_check_parentheses():
    assert check_parentheses('')
    assert check_parentheses('()')
    assert check_parentheses('((()))')
    assert check_parentheses('((()()))')

    assert not check_parentheses('(')
    assert not check_parentheses('(()')
    assert not check_parentheses(')(')
