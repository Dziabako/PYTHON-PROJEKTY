#KOD DO POPRAWY!!!!!!!!

print("Zgadywanka")
print("Ty wymyslasz, ja zgaduje\n\n")

import random
guess = random.randint(1, 100)
odpowiedz = int(input("Podaj liczbe do odgadniecia: "))
tries = 1

while guess != odpowiedz:
    if guess > odpowiedz:
        print("Czy ta liczba to: ", guess, "?")
        guess = random.randint(1, guess)
    elif guess < odpowiedz:
        print("Czy ta liczba to: ", guess, "?")
        guess = random.randint(guess, 100)
    elif guess == odpowiedz:
        print("Czy ta liczba to: ", guess, "?")
    tries += 1


print("Ha udalo sie! Twoja liczba to:", guess, "Potrzebowalem tylko: ", tries, "prob")