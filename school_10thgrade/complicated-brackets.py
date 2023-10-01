#in process...


def complicated_brackets(brackets_string):
    opened_brackets = ['(', '[', '{', '<']
    closed_brackets = [')', ']', '}', '>']
    brackets_shifts = [0, 0, 0, 0]
    for bracket in brackets_string:
        try:
            i = opened_brackets.index(bracket)
            brackets_shifts[i] += 1
        except ValueError:
            i = closed_brackets.index(bracket) 
            brackets_shifts[i] -= 1
        if sum(1 for n in brackets_shifts if n < 0) > 0:
            return False
    if sum(brackets_shifts) == 0:
        return True


def test_cases():
    assert complicated_brackets('({[[((()))]]})[{{{<>}}}]') == True
    assert complicated_brackets('({[}[((()))]]})[{{{<>}}}]') == False
    assert complicated_brackets('(]') == False
    assert complicated_brackets(')((())))') == False
    assert complicated_brackets('[{{(})}]') == False

 
test_cases()
