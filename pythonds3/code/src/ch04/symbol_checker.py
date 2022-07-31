from src.ch04.stack import Stack


def check_parentheses(symbol_string):
    s = Stack()

    for symbol in symbol_string:
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()
