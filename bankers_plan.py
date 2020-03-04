def fortune(total, interest, allowance, years, inflation):
    while years > 0:
        total = round(total * (1 + interest / 100) - allowance, 2)
        allowance = round(allowance * (1 + inflation / 100), 2)
        years -= 1
    return total >= 0


# same with recursive function just for practice
def fortune_recurcsion(total, interest, allowance, years, inflation):
    total = total * (1 + interest / 100) - allowance
    allowance = allowance * (1 + inflation / 100)
    years -= 1
    if years > 0:
        return fortune_recurcsion(round(total, 2), interest, round(allowance, 2), years, inflation)
    return total >= 0


if __name__ == '__main__':
    assert fortune(100000, 1, 2000, 15, 1) is True
    assert fortune(100000, 1, 9185, 12, 1) is False
    assert fortune(100000000, 1, 100000, 50, 1) is True
    assert fortune(100000000, 1.5, 10000000, 50, 1) is False
    assert fortune(100000000, 5, 1000000, 50, 1) is True

    assert fortune_recurcsion(100000, 1, 2000, 15, 1) is True
    assert fortune_recurcsion(100000, 1, 9185, 12, 1) is False
    assert fortune_recurcsion(100000000, 1, 100000, 50, 1) is True
    assert fortune_recurcsion(100000000, 1.5, 10000000, 50, 1) is False
    assert fortune_recurcsion(100000000, 5, 1000000, 50, 1) is True
