# wymieszane litery
# komputer wybiera losowo slowo, a potem miesza jego litery
import random

WORDS = ("python", 'ziom', "dlaczego", "ziomeczek", "dom")

word = random.choice(WORDS)
print(word)

correct = word

# utworz pomieszana wersje slowa
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(jumble)

# rozpocznij grę
print(
    """
               Witaj w grze 'Wymieszane litery'!
    
       Uporządkuj litery, aby odtworzyć prawidłowe słowo.
    (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
    """
)
print("Zgadnij, jakie to słowo:", jumble)

def hint():
    if correct == "python":
        print("Pierwsza litera to 'p' a ostatnia 'n'")
    elif correct == "ziom":
        print("Pierwsza litera to 'z' a ostatnia 'm'")
    elif correct == "dlaczego":
        print("Pierwsza litera to 'd' a ostatnia 'o'")
    elif correct == "ziomeczek":
        print("Pierwsza litera to 'z' a ostatnia 'k'")
    elif correct == "dom":
        print("Pierwsza litera to 'd' a ostatnia 'm'")

tries = 1
tips = 0
points = 10

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    tip = input("Czy potrzebujesz podpowiedzi? Y/N: ")
    if tip == "Y":
        hint()
        tips += 1
        points -= 5
    guess = input("Twoja odpowiedź: ")
    tries += 1

if guess == correct and tips == 0:
    print("Zgadza się! Zgadłeś! Potrzebowales tylko:", tries, "prob oraz uzyskales maksymalna liczbe punktow!")
    print("Twoja liczba punktow to: ", points)
elif guess == correct and tips == 1:
    print("Zgadza się! Zgadłeś! Potrzebowales tylko:", tries, "prob lecz nie uzyskales maksymalnej liczby punktow...")
    print("Twoja liczba punktow to: ", points)
else:
    print("Zgadza się! Zgadłeś! Potrzebowales tylko:", tries, "prob lecz nie otrzymales zadnych punktow...")
    print("Twoja liczba punktow to: ", points)

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")