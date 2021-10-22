import unicodedata2
from unidecode import unidecode

#Inspiration from Stackoverflow search.

def deEmojify(inputString):
    returnString = ""

    for character in inputString:
        try:
            character.encode("ascii")
            returnString += character
        except UnicodeEncodeError:
            replaced = unidecode(str(character))
            if replaced != '':
                returnString += replaced
            else:
                try:
                     returnString += "[" + unicodedata2.name(character) + "]"
                except ValueError:
                     returnString += "[x]"

    return returnString
