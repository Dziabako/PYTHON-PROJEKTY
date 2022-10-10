print("Sprzedawca samochodow!")

cena = int(input("\nPodaj cene podstawowa samochodu: "))
podatek = int(cena*0.15)
rejestracja = int(cena*0.20)
prowizja = int(cena*0.05)
dostawa = int(2000)

total = cena + podatek + rejestracja + prowizja + dostawa

print("\nFaktyczna cena samochodu wynosi: ", total, " zl")
input("\n\nAby zakonczyc nacisnij klawisz ENTER")