def camelCaseSplit(string):
    """
    :param string:
    :return: string
    """
    word = string[0].upper()
    i = 1
    while i < len(string):
        char = string[i]
        if (word[i - 1].islower() or word[i - 1] == " ") and char.isupper():
            word += " " + char
        else:
            word += char
        i += 1

    return word


def snakeCaseSplit(string):
    """
    :param string:
    :return: string
    """

    word = string[0].upper()
    i = 1
    while i < len(string):
        char = string[i]
        if string[i] == "_":
            word += " "
        elif word[i - 1] == " ":
            word += char.upper()
        else:
            word += char
        i += 1

    return word


def caseSplit(string):
    """
    :param string:
    :return: string
    """
    if "_" in string:
        return snakeCaseSplit(string)
    return camelCaseSplit(string)
