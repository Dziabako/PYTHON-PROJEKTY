def zad2_1():
    danie1 = input("Podaj pierwsze danie: ")
    danie2 = input("Podaj drugie danie: ")
    polaczenie = danie1 + " " + danie2
    print("Twoje nowe danie to: ", polaczenie)

def zad2_2():
    bill = int(input("Podaj kwote rachunku: "))
    napiwek15 = bill * 0.15
    napiwek20 = bill * 0.2
    print("Napiwek 15% wynosi: ", napiwek15, "\n", "Napiwek 20% wynosi: ", napiwek20)

def zad2_3():
    cena = int(input("Podaj cene samochodu: "))
    podatek = cena * 0.2
    rejestracja = cena * 0.3
    oplata = 200
    dostawa = 500
    nowa_cena = cena + podatek + rejestracja + oplata + dostawa
    print("Cena samochodu z wszystkimi oplatami wynosi: ", nowa_cena)

def zad3_1():
    import random
    wrozba1 = "bla"
    wrozba2 = "blabla"
    wrozba3 = "blablabla"
    wrozba4 = "blablablabla"
    wrozba5 = "blablablablabla"
    wrozby = (wrozba1, wrozba2, wrozba3, wrozba4, wrozba5)
    wrozba = random.choice(wrozby)
    print("Wylosowales wrozbe: ", wrozba)

def zad3_2():
    import random
    moneta = ("orzel", "reszka")
    rzut = 0
    orzel = 0
    reszka = 0

    while rzut < 100:
        if random.choice(moneta) == "reszka":
            reszka += 1
        else:
            orzel += 1
        rzut += 1
    print("Orzel: ", orzel, "Reszka: ", reszka)

def zad3_3():
    import random
    print("\tWitaj w grze 'Jaka to liczba'!")
    print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
    print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")
    # ustaw wartości początkowe
    the_number = random.randint(1, 100)
    guess = int(input("Ta liczba to: "))
    tries = 1
    # pętla zgadywania
    while guess != the_number:
        if tries > 9:
            print("Koniec gry! Ta liczba to:", the_number)
            break
        elif guess > the_number:
            print("Za duża...")
        else:
            print("Za mała...")
        guess = int(input("Ta liczba to: "))
        tries += 1
    if guess == the_number:
        print("Odgadłeś! Ta liczba to", the_number)
        print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")

def zad3_4():
    import random
    the_number = int(input("Podaj liczbę do zgadniecia od 1 do 100: "))
    guess = random.randint(1, 100)
    tries = 1
    while guess != the_number:
        if guess > the_number:
            print("Czy ta liczba to: ", guess, "?")
            hint = input("Napisz tak, za duzo lub za malo: ")
            if hint == "tak":
                print("Wygrałem! Potrzebowałem tylko ", tries, "prob")
                break
            elif hint == "za duzo":
                print("To probuje dalej...")
            guess = random.randint(1, guess)
            tries += 1
        elif guess < the_number:
            print("Czy ta liczba to: ", guess, "?")
            hint = input("Napisz tak, za duzo lub za malo: ")
            if hint == "tak":
                print("Wygrałem! Potrzebowałem tylko ", tries, "prob")
                break
            elif hint == "za malo":
                print("To probuje dalej...")
            guess = random.randint(guess, 100)
            tries += 1

def zad4_1():
    begin = int(input("Poczatek: "))
    end = int(input("Koniec: "))
    space = int(input("Odstep: "))
    for i in range(begin, end, space):
        print(i, end=" ")

def zad4_2():
    message = input("Wiadomość: ")
    new_message = message[ : : -1]
    print(new_message)

def zad4_3():
    import random
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
        print("Zgadza się! Zgadłeś! Potrzebowales tylko:", tries,
              "prob lecz nie uzyskales maksymalnej liczby punktow...")
        print("Twoja liczba punktow to: ", points)
    else:
        print("Zgadza się! Zgadłeś! Potrzebowales tylko:", tries, "prob lecz nie otrzymales zadnych punktow...")
        print("Twoja liczba punktow to: ", points)

    print("Dziękuję za udział w grze.")

def zad4_4():
    import random
    WORDS = ("python", "kolacja", "robota")
    word = random.choice(WORDS)
    guess = ""
    tries = 5
    print("Zgadnij slowo skladajace się z ", len(word), " liter")
    while tries != 0:
        guess = input("Podaj litere: ")
        if guess in word:
            print("tak")
        else:
            print("nie")
        tries -= 1
    proba = input("Zgadnij slowo: ")
    if proba == word:
        print("Gratulacje! Zgadles!")
    else:
        print("Niestety to nie to")
        print("Slowo do zgadniecia to: ", word)

def zad5_1():
    import random
    words = ["kolo", 'bolo', 'olo', 'ulu', 'mulu', 'ulumulu']

    # shuffle zmienia kolejnosc listy lecz nie tworzy nic nowego z istniejacych elementow
    random.shuffle(words)
    print(words, end=" ")

def zad5_2():
    print("Kreator postaci!")
    print("Masz 30 pkt na rozdanie w celu stworzenia swojej postaci")
    print(
        '''
        Statystyki:
        1) sila
        2) zrecznosc
        3) inteligencja
        4) zdrowie

        '''
    )

    postac = {"Sila": 0,
              "Zrecznosc": 0,
              "Inteligencja": 0,
              "Zdrowie": 0}
    statystyki = 30

    while True:  # petla sie wypelnia jesli elementy w niej zawarte maja wartosc True czyli jest nieskonczona
        wybor = input("W co chcesz wpakowac/usunac punkty: ")
        adding = input("Chcesz dodac czy odjąc: ")
        if adding == "dodac":
            if wybor in postac and statystyki <= 30:
                punkty = int(
                    input("Ile punktow chcesz wpakowac? "))  # int() jest przed input() bo input() bez tego to str
                postac[wybor] += punkty
                statystyki -= punkty
                print("Parametr", wybor, "zwiekszyl sie o: ", punkty, "i pozostalo ci ", statystyki, "pkt do rozdania.")
        elif adding == "odjac" and statystyki != 30:
            if wybor in postac:
                punkty = int(input("Ile punktow chcesz wpakowac? "))
                postac[wybor] -= punkty
                statystyki += punkty
                print("Parametr", wybor, "zmniejszyl sie o: ", punkty, "i pozostalo ci ", statystyki,
                      "pkt do rozdania.")
        else:
            print("Nieprawidlowy komunikat")
        cont = input("Wykorzystales swoje punkty. Czy chcesz cos jeszcze zmienic? Y/N: ")
        if cont == "Y":
            continue
        else:
            break

    print("\nWykorzystales wszystkie mozliwe punkty statystyk")
    print("\nTwoje statystyki wygladaja nastepujaco: ")
    for x in postac:
        print(x, postac[x])  # w ten sposob wywolywany jest caly slownik

def zad5_3():
    print("Kto jest twoim tata?\n")
    print(
        """
        Mozliwe opcje do wykonania:
        0 - zakończ
        1 - znajdź ojca
        2 - dodaj ojca i syna
        3 - zmień syna
        4 - usuń ojca i syna
        5 - wyswietlenie bazy danych
        """
    )

    tree = {"Leonardo": "Al pacino",
            "Andrzej": "Zbigniew",
            "Napoleon": "Bonaparte",
            "Wolodia": "Wladimir",
            "Zbyszek": "Heniek"}
    choice = None

    while choice != 0:
        choice = int(input("Co wybierasz?: "))
        if choice == 0:
            print("Do widzenia!")
        elif choice == 1:
            ojciec = input("Czyjego syna szukasz?: ")
            if ojciec in tree:
                print("Synem ", ojciec, "jest następująca osoba: ")
                ojciec = tree[ojciec]
                print(ojciec)
            else:
                print("Brak danych!")
        elif choice == 2:
            tata = input("Kogo chcesz dodac?: ")
            if tata not in tree:
                syn = input("Kto jest jego synem?: ")
                tree[tata] = syn
                print("Dodane!")
            else:
                print("Podana osoba juz widnieje w bazie danych!")
        elif choice == 3:
            change = input("Komu chcesz zmienic syna?: ")
            if change in tree:
                newson = input("Kto jest jego nowym synem?: ")
                tree[change] = newson
                print("Zmienione!")
            else:
                print("Brak danych!")
        elif choice == 4:
            remove = input("Kogo chcesz usunac?:")
            if remove in tree:
                del tree[remove]
                print("Usuniete!")
            else:
                print("Brak danych!")
        elif choice == 5:
            for x in tree:
                print(x, tree[x])
        else:
            print("Bledny wybor!")

def zad5_4():
    print("Kto jest twoim tata?\n")
    print(
        """
        Mozliwe opcje do wykonania:
        0 - zakończ
        1 - znajdź wnuka/syna
        2 - dodaj ojca i syna
        3 - zmień wnuka/syna
        4 - usuń dziadka, ojca i syna
        5 - wyswietlenie bazy danych
        """
    )

    tree = {"Dicaprio": {"Leonardo": "Al pacino"},
            "Romek": {"Andrzej": "Zbigniew"},
            "Francuz": {"Napoleon": "Bonaparte"},
            "Wowa": {"Wolodia": "Wladimir"},
            "Mirek": {"Zbyszek": "Heniek"}}

    choice = None
    while choice != 0:
        choice = int(input("Co Wybierasz?: "))
        if choice == 0:
            print("Do widzenia!")
        elif choice == 1:
            dziadek = input("Czyj wnuk?: ")
            ojciec = input("Czyj syn?: ")
            print("Wnukiem ", dziadek, " i synem ", ojciec, "jest: ")
            if dziadek in tree and ojciec in tree[dziadek]:
                wnuk = tree[dziadek][ojciec]
                print(wnuk)
            else:
                print("Brak danych!")
        elif choice == 2:
            newd = input("Kogo dodajesz?: ")
            if newd not in tree:
                syn = input("Kto jest jego synem?: ")
                wnuk = input("Kto jest jego wnukiem?: ")
                tree[newd] = {syn: wnuk}
                print("Dodane!")
            else:
                print("Juz istnieje!")
        elif choice == 3:
            dziadek = input("Komu zmieniasz rodzine?: ")
            if dziadek in tree:
                nsyn = input("Nowy syn: ")
                nwnuk = input("Nowy wnuk: ")
                tree[dziadek] = {nsyn: nwnuk}
                print("Zmienione!")
            else:
                print("Brak danych!")
        elif choice == 4:
            remove = input("Kogo chces usunac?: ")
            if remove in tree:
                del tree[remove]
                print("Usunięte!")
            else:
                print("Brak danych!")
        elif choice == 5:
            for x, y in tree.items():                       # .items = zwraca slownik jako 2 skladnikowa krotka (przez co nie wysakuje blad o zbyt duzej ilosci info do rozpakowania)
                print("Dziadek ", x, "ma syna/wnuka: ")     # 1 - klucz     2 - wartosc
                for z in y:                                 # x - klucz glownego slownika,   z - klucz podslownika
                    print(z + ",", y[z])                    # y[z] - wartosc w podslowniku
        else:                                               # najpierw iteruje przez glowny slownik (pierwsza petla for)
            print("Nieprawidlowa opcja!")                   # nastepnie przez podslowniki   (druga petla for (jak przy iteracji w 5.3))

def funkcja_testowa():
    # Pobierz i zwróć
    # Demonstruje parametry i wartości zwrotne
    def display(message):
        print(message)

    def give_me_five():
        five = 5
        return five

    def ask_yes_no(question):
        """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
        response = None
        while response not in ("t", "n"):
            response = input(question).lower()                          #bedzie sie powtarzac dopoki nie zostana spelnione zalozenia petli while // input(question).lower() - powtarza pytanie i wymaga wprowadzenie odpowiedniej odpowiedzi
        return response

    # main
    display("To wiadomość dla Ciebie.\n")
    number = give_me_five()
    print("Oto co otrzymałem z funkcji give_me_five():", number)
    answer = ask_yes_no("\nProszę wprowadzić 't' lub 'n': ")            #w nawiasie wpisane jest pytanie które przy definiowaniu fukcji ma nazwe "question"
    print("Dziękuję za wprowadzenie:", answer)
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

def zad6_1():
    def ask_number(question, low, high, step = 1):
        """Poproś o podanie liczby z odpowiedniego zakresu."""
        response = None
        while response not in range(low, high, step):
            response = int(input(question))
        return response

def zad6_2():
    import random
    print("\tWitaj w grze 'Jaka to liczba'!")
    print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
    print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")
    # ustaw wartości początkowe
    the_number = random.randint(1, 100)
    guess = int(input("Ta liczba to: "))
    tries = 1
    def ask_number(question, low, high):
        """Poproś o podanie liczby z odpowiedniego zakresu."""
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response
    # pętla zgadywania
    while guess != the_number:
        if tries > 9:
            print("Koniec gry! Ta liczba to:", the_number)
            break
        elif guess > the_number:
            print("Za duża...")
        else:
            print("Za mała...")
        guess = ask_number("Ta liczba to?: ", 1, 100)
        tries += 1
    if guess == the_number:
        print("Odgadłeś! Ta liczba to", the_number)
        print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")

def zad6_3():
    def instructions():
        print("\tWitaj w grze 'Jaka to liczba'!")
        print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
        print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

    def ask_number(question, low, high):
        """Poproś o podanie liczby z odpowiedniego zakresu."""
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    # pętla zgadywania
    def guessing():
        import random
        the_number = random.randint(1, 100)
        guess = int(input("Ta liczba to: "))
        tries = 1
        while guess != the_number:
            if tries > 9:
                print("Koniec gry! Ta liczba to:", the_number)
                break
            elif guess > the_number:
                print("Za duża...")
            else:
                print("Za mała...")
            guess = ask_number("Ta liczba to?: ", 1, 100)
            tries += 1
        if guess == the_number:
            print("Odgadłeś! Ta liczba to", the_number)
            print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")
    def main():
        instructions()
        guessing()
    main()

def exercise():
    zad5_4()
exercise()