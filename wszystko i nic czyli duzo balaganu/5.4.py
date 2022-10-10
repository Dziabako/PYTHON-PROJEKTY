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

tree = {"Dicaprio":{"Leonardo" : "Al pacino"},
        "Romek":{"Andrzej" : "Zbigniew"},
        "Francuz":{"Napoleon" : "Bonaparte"},
        "Wowa":{"Wolodia" : "Wladimir"},
        "Mirek":{"Zbyszek" : "Heniek"}}

choice = None

while choice != 0:
    choice = int(input("Co wybierasz?: "))
    if choice == 0:
        print("Do widzenia!")
    elif choice == 1:
        dziadek = input("Kto jest jego dziadkiem?: ")
        ojciec = input("Kogo syna szukasz?: ")
        print("Wnukiem", dziadek, "i synem", ojciec, "jest następujaca osoba:")
        if dziadek in tree and ojciec in tree[dziadek]:
            print(tree[dziadek][ojciec])
        else:
            print("Nie ma takiej osoby w bazie danych!")
    elif choice == 2:
        dziadek = input("Imie dziadka?:")
        if dziadek not in tree:
            tata = input("Imie ojca?: ")
            syn = input("Kto jest synem/wnukiem?: ")
            tree[dziadek] = {tata: syn}  # dodanie nowej pary do slownika
            print("Dodane!")
        else:
            print("Juz istnieje taka para!")
    elif choice == 3:
        change = input("Komu chcesz zmienic wnuka?: ")
        if change in tree:
            lojciec = input("Podaj nowe imie ojca: ")
            newson = input("Kto jest teraz jego nowym synem?: ")
            tree[change] = {lojciec: newson}
            print("Zmienione")
        else:
            print("Taka osoba nie widnieje w bazie danych!")
    elif choice == 4:
        change = input("Kogo chcesz usunac?: ")
        if change in tree:
            remove = tree.pop(change)
            print("Usuniete!")
            print("Usunięto: ", remove)
        else:
            print("Taka osoba nie widnieje w bazie danych!")
    elif choice == 5:
        for x, y in tree.items():                       # .items = zwraca slownik jako 2 skladnikowa krotka (przez co nie wysakuje blad o zbyt duzej ilosci info do rozpakowania0
            print("Dziadek ", x, "ma syna/wnuka: ")     # 1 - klucz     2 - wartosc
            for z in y:                                 # x - klucz glownego slownika,   y - klucz podslownika
                print(z + ",", y[z])                    # z - mozna powiedziec ze to wartosc w podslowniku
    else:                                               # najpierw iteruje przez glowny slownik (pierwsza petla for)
        print("Nieprawidlowa opcja!")                   # nastepnie przez podslowniki   (druga petla for (jak przy iteracji w 5.3))
