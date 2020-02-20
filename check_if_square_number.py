from math import sqrt


def is_square(n):
    return n >= 0 and sqrt(n) % 1 == 0


if __name__ == '__main__':
    assert is_square(-1) is False
    assert is_square(0) is True
    assert is_square(3) is False
    assert is_square(4) is True
    assert is_square(25) is True
    assert is_square(26) is False
