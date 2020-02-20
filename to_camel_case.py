import re


def to_camel_case(text):
    words_list = re.split("_|-", text)
    text = [word.capitalize() if word != words_list[0] else word for word in words_list]
    return "".join(text)


if __name__ == '__main__':
    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
