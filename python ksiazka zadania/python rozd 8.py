class Criter:
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "Szczesliwy"
        elif 5 <= unhappines <= 10:
            m = "Zadowolony"
        elif 11 <= unhappines <= 15:
            m = "Poddenerwowany"
        else:
            m = "Wsciekly"

        return m

    def talk(self):
        print(f"Nazywam się {self.name} i jestem {self.mood()} teraz\n")
        self.__pass_time()

    def eat(self):
        food = int(input("Ile jedzenia? "))
        print("Mniam, mniam. Dziekuje")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = int(input("Czas na zabawe? "))
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        print(f"Nastrój: {self.mood()}")
        print(f"Glod: {self.hunger}")
        print(f"Nuda: {self.boredom}")


def main():
    crit_name = input("Podaj imie zwierzaka: ")
    crit = Criter(crit_name)

    choice = None
    while choice != "0":
        print("""
        Opiekun zwierzaka
            0 - zakończ
            1 - słuchaj swojego zwierzaka
            2 - nakarm swojego zwierzaka
            3 - pobaw się ze swoim zwierzakiem
        """)
        choice = input("Wybierasz: ")
        print()
        # wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")
        # słuchaj swojego zwierzaka
        elif choice == "1":
            crit.talk()
        # nakarm swojego zwierzaka
        elif choice == "2":
            crit.eat()
        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            crit.play()
        elif choice == "4":
            crit.__str__()
        # nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()
input("Aby zakonczyc nacisnij klawisz ENTER")
