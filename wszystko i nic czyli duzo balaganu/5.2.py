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

postac = {"Sila" : 0,
          "Zrecznosc" : 0,
          "Inteligencja" : 0,
          "Zdrowie" : 0}
statystyki = 30


while True:     # petla sie wypelnia jesli elementy w niej zawarte maja wartosc True czyli jest nieskonczona
    wybor = input("W co chcesz wpakowac/usunac punkty: ")
    adding = input("Chcesz dodac czy odjąc: ")
    if adding == "dodac":
        if wybor in postac and statystyki <= 30:
            punkty = int(input("Ile punktow chcesz wpakowac? "))  # int() jest przed input() bo input() bez tego to str
            postac[wybor] += punkty
            statystyki -= punkty
            print("Parametr", wybor, "zwiekszyl sie o: ", punkty, "i pozostalo ci ", statystyki, "pkt do rozdania.")
    elif adding == "odjac" and statystyki != 30:
        if wybor in postac:
            punkty = int(input("Ile punktow chcesz wpakowac? "))
            postac[wybor] -= punkty
            statystyki += punkty
            print("Parametr", wybor, "zmniejszyl sie o: ", punkty, "i pozostalo ci ", statystyki, "pkt do rozdania.")
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
    print(x, postac[x]) # w ten sposob wywolywany jest caly slownik

