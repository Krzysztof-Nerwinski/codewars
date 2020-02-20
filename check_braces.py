def validBraces(string):
    counters = string.count("(") == string.count(")") and \
               string.count("[") == string.count("]") and \
               string.count("{") == string.count("}")
    parentheses_open, brackets_open, curly_open = 0, 0, 0
    if len(string) % 2 == 0 and counters and string[-1] not in "([{":
        for indx, brace in enumerate(string):
            if brace == "(" and string[indx + 1] in "([{)":
                parentheses_open += 1
            elif brace == "[" and string[indx + 1] in "([{]":
                brackets_open += 1
            elif brace == "{" and string[indx + 1] in "([{}":
                curly_open += 1
            elif brace == ")":
                parentheses_open -= 1
            elif brace == "]":
                brackets_open -= 1
            elif brace == "}":
                curly_open -= 1
            else:
                return False
        if not (parentheses_open and brackets_open and curly_open):
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    assert validBraces("()") is True
    assert validBraces("[(])") is False
    assert validBraces("(}") is False
    assert validBraces("[(])") is False
    assert validBraces("[({})](]") is False
    assert validBraces("{()}[][{}]") is True
    assert validBraces("())({}}{()][][{]") is False
    assert validBraces("(({})){((){}[])}{[()]}[]") is True
