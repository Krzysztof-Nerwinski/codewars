
def duplicate_encode(word):
    word = word.lower()
    result = ""
    for indx,char in enumerate(word):
        if char in word[:indx] or char in word[indx+1:]:
            result += ")"
        else:
            result += "("
    return result



if __name__ == '__main__':
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("SucceSs") == ")())())"
    assert duplicate_encode("(( @") == "))(("