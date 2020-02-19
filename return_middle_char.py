
def get_middle(word):
    # if len(word) % 2 == 0:
    #     middle = int(len(word)/2)
    #     return word[middle-1:middle+1]
    # else:
    #     middle = int(len(word)/2)+1
    #     return word[middle-1]

    #more clever
    index, odd = divmod(len(word), 2)
    return word[index] if odd else word[index-1,index+1]



if __name__ == '__main__':
    assert get_middle("test") == "es"
    assert get_middle("testing") == "t"
    assert get_middle("middle") == "dd"
    assert get_middle("A") == "A"
    assert get_middle("of") == "of"
