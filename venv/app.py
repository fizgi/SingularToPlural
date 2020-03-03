""" A program for converting singular words to plural form.

    author: Fatih IZGI
    date: 02-Mar-2020
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
    elif string.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        string += "es"
    else:
        string += "s"

    return string


while True:  # loop for getting valid input from the user
    single_words: str = input("Please enter a string: ")
    if all(char.isalpha() or char.isspace() for char in single_words):
        break
    print("Please enter only alphabetic characters. "
          "If you want to enter multiple words, separate them with whitespaces.")

words: List[str] = single_words.split(" ")
plurals: List[str] = []

for word in words:
    if word != "":  # eliminate blank items, just put the words into operation
        plurals.append(plural(word))

final_string: str = " ".join(plurals)  # join the plural forms

print(final_string)
