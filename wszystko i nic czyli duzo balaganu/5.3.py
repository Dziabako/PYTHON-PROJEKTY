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

tree = {"Leonardo" : "Al pacino",
        "Andrzej" : "Zbigniew",
        "Napoleon" : "Bonaparte",
        "Wolodia" : "Wladimir",
        "Zbyszek" : "Heniek"}

choice = None

while choice != 0:
    choice = int(input("Co wybierasz?: "))
    if choice == 0:
        print("Do widzenia!")
    elif choice == 1:
        ojciec = input("Kogo szukasz?: ")
        print("Synem", ojciec, "jest następujaca osoba:")
        print(tree.get(ojciec, "Nie ma takiej osoby w bazie danych!"))
    elif choice == 2:
        tata = input("Kogo chcesz dodac?: ")
        if tata not in tree:
            syn = input("Kto jest jego synem?: ")
            tree[tata] = syn   # dodanie nowej pary do slownika
            print("Dodane!")
        else:
            print("Juz istnieje taka para!")
    elif choice == 3:
        change = input("Komu chcesz zmienic syna?: ")
        if change in tree:
            newson = input("Kto jest teraz jego nowym synem?: ")
            tree[change] = newson
            print("Zmienione")
        else:
            print("Taka osoba nie widnieje w bazie danych!")
    elif choice == 4:
        change = input("Kogo chcesz usunac?: ")
        if change in tree:
            del tree[change]
            print("Usuniete")
        else:
            print("Taka osoba nie widnieje w bazie danych!")
    elif choice == 5:
        for x in tree:
            print(x, tree[x])
    else:
        print("Nieprawidlowa opcja!")