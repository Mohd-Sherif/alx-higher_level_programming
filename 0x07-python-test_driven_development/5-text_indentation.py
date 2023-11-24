#!/usr/bin/python3
"""Defines a printing text indented function"""


def text_indentation(text):
    """
    Printing a text with 2 new lines after
    each of these characters: `.`, `?` and `:`

    :param text: to be modified
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    elements_list = text.split(' ')
    elements_list = [element for element in elements_list if element != '']
    new_text = ' '.join(elements_list)
    new_text = new_text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ", ":\n\n")
    print(new_text, end="")
