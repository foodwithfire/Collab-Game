from objects.image import Image
from time import sleep
from objects.player import Player

"""
Welcome in the Random Things Functions Module!

Here are the list of all the functions, and of what they do:

max() -> Takes two integers and returns the biggest.
getVowel() -> Counts the vowels of a specified string and returns the number.
getCons() -> Counts the consonants of a specified string and returns the number.
convertBinary() -> Converts an integer in binary (does the same as bin())
typewriter() -> Prints a string in a "typewriter" way.
typewriterList() -> Variant of typewriter() for lists, prints each value in a "typewriter" way.
firstRemIdentity() -> Makes the first remarkable identity's equation.
secondRemIdentity() -> Makes the second remarkable identity's equation.
thirdRemIdentity() -> Makes the third remarkable identity's equation.
start() -> Makes the game start
"""


def max(a, b):
    """
    Gets two integers and sends back the biggest.
    """
    if a > b:
        return a
    else:
        return b


def getVowel(word, y_vowel=True):
    """
    Takes a string as a parameter and sends back the number of vowels.
    The parameter "y_vowel" allows the user to set Y as a vowel. By default, it's on True.
    """
    vowel_count = 0
    if y_vowel == True:
        vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    else:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in word:
        if letter in vowels:
            vowel_count += 1
        continue
    return vowel_count


def getCons(word, y_consonant=False):
    """
    Takes a word as a parameter and sends back the number of consonants.
    The parameter "y_consonant" allows the user to set Y as a consonant. By default, it's on False.
    """
    cons_count = 0
    if y_consonant == False:
        consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w",
                      "x", "z", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S",
                      "T", "V", "W", "X", "Z"]
    else:
        consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w",
                      "x", "y", "z", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S",
                      "T", "V", "W", "X", "Y", "Z"]
    for letter in word:
        if letter in consonants:
            cons_count += 1
        continue
    return cons_count


def convertBinary(n=1):
    """
    Converts a number in binary. By default, it's 1.
    """
    return bin(n)


def typewriter(string):
    """
    Prints a string in a typewriter style.
    """
    for char in string:
        sleep(0.05)
        print(char, end='')
    print("\n")


def typewriterList(list):
    """
    Prints a list of values in a single line in a typewriter style.
    """
    for value in list:
        sleep(0.1)
        print(value + " ")
    print("\n")


def firstRemIdentity(a, b):
    """
    Makes the first remarkable identity's equation:
        (a+b)² = a² + 2ab + b²
    and returns the result. Takes a and b as parameters.
    """
    result = a**2 + 2*(a*b) + b**2
    return result


def secondRemIdentity(a, b):
    """
    Makes the second remarkable identity's equation:
        (a-b)² = a² - 2ab + b²
    and returns the result. Takes a and b as parameters
    """
    result = a**2 - 2*(a*b) + b**2
    return result


def thirdRemIdentity(a, b):
    """
        Makes the third remarkable identity's equation:
            (a+b)(a-b) = a² - b²
        and returns the result. Takes a and b as parameters
    """
    result = a**2 - b**2
    return result

def start(screen, player_name, player_health, player_damage, mana, player_level, placeholder, player_weapon, player_money):
    global player, started, background
    player = Player(screen, player_name, player_health, player_damage, mana, player_level, placeholder, player_weapon, player_money)
    started = True