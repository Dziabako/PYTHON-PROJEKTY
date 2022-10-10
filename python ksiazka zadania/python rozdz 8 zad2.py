class Tele:
    def __init__(self, channel=1, volume=10):
        self.volume = volume
        self.channel = channel

    def volume_up(self):
        vol = int(input("O ile chcesz podglosic? "))
        if self.volume >= 0 and self.volume <= 20:
            self.volume += vol
            print(f"Glosnosc zostala zmieniona i wynosi {self.volume} teraz")
        else:
            print("Podana wartosc nie nalezy do odpowiedniego zakresu")

    def volume_down(self):
        vol = int(input("O ile chcesz sciszyc? "))
        if self.volume >= 0 and self.volume <= 20:
            self.volume -= vol
            print(f"Glosnosc zostala zmieniona i wynosi {self.volume} teraz")
        else:
            print("Podana wartosc nie nalezy do odpowiedniego zakresu")

    def change_ch(self):
        ch = int(input("Podaj numer kanalu od 1 do 20: "))
        if self.channel >= 1 and self.channel <= 20:
            self.channel = ch
            print(f"Aktualny kanal to {self.channel}")
        else:
            print("Podany kanal jest poza zasiegiem")

    def check_info(self):
        print(f"Glosnosc wynosi: {self.volume}")
        print(f"Aktualny kanal to: {self.channel}")


def main():
    tv = Tele()

    choice = " "
    while choice != '0':
        print("""\nSymulator telewizora!
        Wybierz jedna z opcji:
        0 - wylaczenie tv
        1 - sprawdzenie statusu
        2 - podglaszanie
        3 - sciszanie
        4 - zmiana kanalu\n""")
        
        choice = input("Co wybierasz: ")
        if choice == '0':
            print("Out!")
        elif choice == '1':
            tv.check_info()
        elif choice == '2':
            tv.volume_up()
        elif choice == '3':
            tv.volume_down()
        elif choice == '4':
            tv.change_ch()
        else:
            print("Nieprawidlowa opcja! Sprobuj ponownie\n")


main()
input("Aby zakonczyc nacisnij klawisz ENTER")
