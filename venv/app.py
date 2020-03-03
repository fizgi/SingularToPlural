""" A program for converting singular words to plural.

    author: Fatih IZGI
    date: 03-Mar-2020
    version: python 3.8.1
"""

from typing import List


def plural(string: str) -> str:
    """ Takes a string and returns the plural form of the tokens
    """
    if string.endswith("y"):  # if starts with "y"
        if string[-2] in ('a', 'e', 'i', 'o', 'u'):  # ends with 'y', preceded by a vowel
            string += "s"
        else:
            string = string[:-1] + "ies"  # ends eith 'y', not preceded by a vowel
    elif string.endswith(('o','ch', 's', 'sh', 'x', 'z')):
        string += "es"
    else:
        string += "s"

    return string


while True:  # loop for getting valid input from the user
    string: str = input("Please enter a string: ")
    if all(x.isalpha() or x.isspace() for x in string):
        break
    else:
        print("Please enter only alphabetic characters. "
              "If you want to write multiple words, separate them with whitespace")

words: List[str] = [word for word in string.split(" ")]

plurals: List[str] = []

for word in words:
    if word != "":  # eliminate blank items, just put the words into operation
        plurals.append(plural(word))

final_string: str = " ".join([plural for plural in plurals])  # join the plural forms

print(final_string)
