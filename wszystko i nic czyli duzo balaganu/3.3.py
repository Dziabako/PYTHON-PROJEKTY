print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób. Masz na to 10 prób\n")

import random

# ustaw wartości początkowe
the_number = random.randint(1, 100)
guess = int(input("Ta liczba to: "))
tries = 1

# pętla zgadywania
while guess != the_number:
    if tries > 9:
        print("Koniec gry wykorzystałeś swoje próby. Ta liczba to: ", the_number)
        break
    elif guess < the_number:
        print("Za mala...")
        print("Próba: ", tries)
    elif guess > the_number:
        print("Za duzo...")
        print("Próba: ", tries)
    guess = int(input("Ta liczba to: "))
    tries += 1

if guess == the_number:
    print("Odgadłeś! Ta liczba to", the_number)
    print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")