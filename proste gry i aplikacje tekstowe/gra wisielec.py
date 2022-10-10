import random
HANGMAN = (
"""
 ------
 |   |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 |  -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-/
 |   |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-/
 |   |
 |   |
 |   |
 | |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-/
 |   |
 |   |
 | |   |
 | |   |
 |
----------
""")
max_fail = len(HANGMAN)
WORDS = ("wisielec", "krotka", "lista", "hangman", "python")
word = random.choice(WORDS)
print(word)
lenght = len(word)
kreski = "-" * lenght
used = []
print("Zgadnij slowo skladajace sie z ", lenght, "liter!\n", "Masz 7 szans!")


def str_replace(string, word, guess):
    for i in range(len(word)):
        if guess in word[i]:                                                    # w ten sposob dobierany jest odpowiedni numer indexu przez co str jest zamieniany w odpowiednim miejscu
            if guess not in string:
                string = string[0:i] + guess + string[i + 1:]                   # str ciachany jest od 0 do podanej liczby, potem dodawany jest na odpowienim indexie str a ptem dodawana jest reszta
            elif guess in string:
                string = string[0:i] + guess + string[i + 1:]
    return string


while max_fail > 0 and kreski != word:
    print("\nWykorzystales nastepujace litery: ", used)
    print("To slowo wyglada tak: ", kreski)
    print(HANGMAN[-max_fail])
    guess = input("Podaj litere: ")
    if guess not in word and guess not in used:
        used.append(guess)
        print("Nie ma tej litery w slowie!\n")
        max_fail -= 1
    elif guess not in word and guess in used:
        print("Juz wykorzystales ta litere\n")
    elif guess in word:
        kreski = str_replace(kreski, word, guess)


if kreski == word:
    print("Wygrales!", word.upper)
else:
    print("Przegrales")

