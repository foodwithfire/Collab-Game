import os


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
    Takes a word as a parameter and sends back the number of vowels.
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


def convertBinary(n = 1):
    return bin(n)


def getMcChat(path):
    chat_logs = []
    with open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r") as logfile:
        for line in logfile:
            if ": [CHAT]" in line:
                chat_logs.append(line)
    with open(path, "w+") as file:
        for value in chat_logs:
            file.write(value)


def getMcErrors(path):
    errors_logs = []
    with open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r") as logfile:
        for line in logfile:
            if "[Client thread/ERROR]" in line:
                errors_logs.append(line)
    with open(path, "w+") as file:
        for value in errors_logs:
            file.write(value)
            
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


def typewriterLines(list):
    """
    Prints a list of values on several lines in a typewriter style.
    """
    for line in list:
        sleep(0.1)
        print(line)
    print("\n")
