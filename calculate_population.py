from unittest import TestCase


def nb_year(p0, percent, aug, p):
    population = p0
    years = 0
    while population < p:
        population = population + population * percent / 100 + aug
        years += 1
    return years


if __name__ == '__main__':
    assert nb_year(1000,2,50,1500) == 7
    assert nb_year(1000,4,30,2000) == 12

