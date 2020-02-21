import re


def check_code_for_braces(code):
    """
    Extended codewars task just for practice.
    Additional function, check complete code, leave only braces and check if order is correct
    :param code: string
    :return: bool
    """
    # remove docstrings with content
    brackets = re.sub("(\"\"\")*(\"\"\")", "", code)
    # remove double quotes with content
    brackets = re.sub("\"[^\"]*\"", "", brackets)
    # remove single quotes with content
    brackets = re.sub("\'[^\']*\'", "", brackets)

    brackets = "".join(filter(lambda char: char in "()[]{}", [char for char in brackets]))
    while "()" in brackets or "[]" in brackets or "{}" in brackets:
        brackets = brackets.replace("()", "")
        brackets = brackets.replace("[]", "")
        brackets = brackets.replace("{}", "")
    return brackets == ""


def valid_braces(string):
    """
    First try in solving codewars KATA for checking if string has a correct number and order of braces
    :param string:
    :return: bool
    """
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
    assert valid_braces("()") is True
    assert valid_braces("[(])") is False
    assert valid_braces("(}") is False
    assert valid_braces("[(])") is False
    assert valid_braces("[({})](]") is False
    assert valid_braces("{()}[][{}]") is True
    assert valid_braces("())({}}{()][][{]") is False
    assert valid_braces("(({})){((){}[])}{[()]}[]") is True

    assert check_code_for_braces("()") is True
    assert check_code_for_braces("[(])") is False
    assert check_code_for_braces("(}") is False
    assert check_code_for_braces("[(])") is False
    assert check_code_for_braces("[({})](]") is False
    assert check_code_for_braces("{()}[][{}]") is True
    assert check_code_for_braces("())({}}{()][][{]") is False
    assert check_code_for_braces("(({})){((){}[])}{[()]}[]") is True

    test_code_true_1 = """counters = string.count("(") == string.count(")") and \
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
                    
                    """

    test_code_true_2 = """
    class Category(models.Model):
        name = models.CharField(max_length=256, verbose_name='Nazwa')
    
        def __str__(self):
            return self.name
    
        class Meta:
            verbose_name = 'Kategoria'
            verbose_name_plural = 'Kategorie'
    
    
    class Institution(models.Model):
    
        types = (
            (FOUNDATION, 'Fundacja'),
            (ORGANIZATION, 'Organizacja pozarządowa'),
            (LOCAL_COLLECTION, 'Zbiórka lokalna')
        )
        name = models.CharField(max_length=256, verbose_name='Nazwa')
        description = models.TextField(null=True, verbose_name='Opis')
        type = models.IntegerField(choices=types, default=FOUNDATION)
        categories = models.ManyToManyField(Category)
    
        def __str__(self):
            return self.name
    
        class Meta:
            verbose_name = 'Instytucja'
            verbose_name_plural = 'Instytucje'
    
    
    class Donation(models.Model):
        quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Worki')
        categories = models.ManyToManyField(Category)
        institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name='Instytucja')
        address = models.CharField(max_length=128)
        phone_number = models.CharField(max_length=15)
        city = models.CharField(max_length=64)
        zip_code = models.CharField(max_length=10)
        pick_up_date = models.DateField()
        pick_up_time = models.TimeField()
        pick_up_comment = models.TextField(blank=True)
        user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, verbose_name='Użytkownik')
        is_taken = models.BooleanField(default=False, verbose_name="Zrealizowane")
    
        class Meta:
            verbose_name = 'Darowizna'
            verbose_name_plural = 'Darowizny'
    """

    test_code_false = """
    class Category(models.Model):
        name = models.CharField(max_length=256, verbose_name='Nazwa')
    
        def __str__(self):
            return self.name
    
        class Meta:
            verbose_name = 'Kategoria'
            verbose_name_plural = 'Kategorie'
    
    
    class Institution(models.Model):
    
        types = (
            (FOUNDATION, 'Fundacja'),
            (ORGANIZATION, 'Organizacja pozarządowa'),
            (LOCAL_COLLECTION, 'Zbiórka lokalna')
        )
        name = models.CharField(max_length=256, verbose_name='Nazwa')
        description = models.TextField(null=True, verbose_name='Opis')
        type = models.IntegerField(choices=types, default=FOUNDATION)
        categories = models.ManyToManyField(Category)
    
        def __str__(self)):
            return self.name
    
        class Meta:
            verbose_name = 'Instytucja'
            verbose_name_plural = 'Instytucje'
    
    
    class Donation(models.Model):
        quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Worki')
        categories = models.ManyToManyField(Category)
        institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name='Instytucja')
        address = models.CharField(max_length=128)
        phone_number = models.CharField(max_length=15)
        city = models.CharField(max_length=64)
        zip_code = models.CharField(max_length=10)
        pick_up_date = models.DateField()
        pick_up_time = models.TimeField()
        pick_up_comment = models.TextField(blank=True)
        user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, verbose_name='Użytkownik')
        is_taken = models.BooleanField(default=False, verbose_name="Zrealizowane")
    
        class Meta:
            verbose_name = 'Darowizna'
            verbose_name_plural = 'Darowizny'
    """

    assert check_code_for_braces(test_code_true_1) is True
    assert check_code_for_braces(test_code_true_2) is True
    assert check_code_for_braces(test_code_false) is False
