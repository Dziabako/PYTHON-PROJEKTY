print("Zgadywaczoinator!")
print("Ja wymyslam slowo a ty zgadujesz")
print("Masz 5 prob by sprawdzic jakie litery znajduja sie w danym slowie\n")

import random
#zmienne
WORDS = ("python", "domek", "ziomus", "ulumulu", "konsola")
word = random.choice(WORDS)
guess = ""
tries = 5

#gra
print("\nZgadnij slowo skladajace sie z ", len(word), "slow!")
while tries != 0:
    guess = input("Zgadnij litere: ")
    if guess in word:
        print("Tak")
    else:
        print("Nie")
    tries -= 1

print("\nWykorzystales szanse! Teraz zgaduj!")
proba = input("Tajemnicze slowo to: ")
if proba == word:
    print("Gratulacje zgadles!")
else:
    print("Niestety to nie to slowo")