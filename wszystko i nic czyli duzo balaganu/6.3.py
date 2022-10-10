def instructions():
    print("\tWitaj w grze 'Jaka to liczba'!")
    print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
    print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób. Masz na to 10 prób\n")

import random

def ask_number(question, low, high):
 """Poproś o podanie liczby z odpowiedniego zakresu."""
 response = None
 while response not in range(low, high):
    response = int(input(question))
 return response

def guessing():
    the_number = random.randint(1, 100)
    tries = 1
    guess = None
    while guess != the_number:
        guess = ask_number("Ta liczba to: ", 1, 100)
        if tries > 9:
            print("Koniec gry wykorzystałeś swoje próby. Ta liczba to: ", the_number)
            break
        elif guess < the_number:
            print("Za mala...")
            print("Próba: ", tries)
        elif guess > the_number:
            print("Za duzo...")
            print("Próba: ", tries)
        elif guess == the_number:
            print("Odgadłeś! Ta liczba to", the_number)
            print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!")
            break
        tries += 1

def main():
    instructions()
    guessing()

main()   # to jest caly kod programu ktory sie wykonuje na podstawie zdefiniowanych funkcji

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")