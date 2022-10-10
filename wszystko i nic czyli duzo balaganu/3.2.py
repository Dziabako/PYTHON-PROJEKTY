print("Rzut moneta\n")

import random
moneta = ("orzel", "reszka")
rzut = 0
reszka = 0
orzel = 0

#random.choice = wybor pomiedzy dwona roznymi wyrazami

while rzut < 100:
    if random.choice(moneta) == "reszka":
        reszka += 1
    else:
        orzel += 1
    rzut += 1

print("Orly: ", orzel, "Reszka: ", reszka)
input("\nAby zakonczyc nacisnij klawisz ENTER")