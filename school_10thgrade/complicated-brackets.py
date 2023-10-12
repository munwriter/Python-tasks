def valid_complicated_brackets(brackets_string):
    open_closed_brackets = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>',
    }
    # firs in|last out
    stack = []
    
    for bracket in brackets_string:
        if bracket in open_closed_brackets:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != open_closed_brackets[stack[-1]]:
            return False
        else:
            stack.pop()
    return len(stack) == 0


def test_cases():
    assert valid_complicated_brackets('({[[((()))]]})[{{{<>}}}]') == True
    assert valid_complicated_brackets('({[}[((()))]]})[{{{<>}}}]') == False
    assert valid_complicated_brackets('(]') == False
    assert valid_complicated_brackets(')((())))') == False
    assert valid_complicated_brackets('[{{(})}]') == False


test_cases()

