from src.ch04.statement_conversion import infix_to_postfix, postfix_eval


def test_infix_to_postfix():
    assert infix_to_postfix('') == ''
    assert infix_to_postfix('A') == 'A'
    assert infix_to_postfix('A + B') == 'A B +'

    assert infix_to_postfix('A * B + C * D') == 'A B * C D * +'
    assert infix_to_postfix('( A + B ) * ( C + D )') == 'A B + C D + *'
    assert infix_to_postfix('( A + B ) * C') == 'A B + C *'
    assert infix_to_postfix('A + B * C') == 'A B C * +'

    assert infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )') == \
        'A B + C * D E - F G + * -'


def test_postfix_eval():
    assert postfix_eval('1') == 1
    assert postfix_eval('7 8 + 3 2 + /') == 3
