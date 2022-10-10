def formatted_string():
    first = "Jan"                                                       #sformatowany string pozwala latwiej zobaczyc output po wywolaniu
    last = "Kowalski"
    msg = f"{first} [{last}] chce sie nauczyc programowac"              #zaczynamy od poprzedzenia string litera f a potem zmienne wpisujemy w klamrach
    print(msg)

#import math  - fukncje matematyczne (mozna znalezc na necie)

#shift + f6 = zmiana nazwy zmiennej w calym kodzie


def car_simulator():
    started = False
    while True:
        i = input("> ").lower()                                         #teraz kazdy nas string bedzie zmieniany na male litery wiec w kolejnych wywolaniach zmiennej nie trzeba tego dawac
        if i == "help":
            print("""            
start - start engine
stop - stop engine
quit - quit program
""")
        elif i == "start":
            if started:                                                 #wykonuje sie kiedy started == True
                print("Engine is already running!")
            else:
                started = True                                          #wykonuje sie kiedy started == False i zmienia started na True
                print("Engine started! We are moving now!")
        elif i == "stop":
            if not started:                                             #wykonuje sie kiedy started == False, poniewaz not zmienia False na True
                print("Engine is already stopped!")
            else:
                started = False                                         #wykonuje sie kiedy started == True i zamienia started na False
                print("Engine stopped!")
        elif i == "quit":
            print("Good Bye!")
            break
        else:
            print("Wrong choice!")


def shopping_list_calculator():
    costs = [10, 20, 30]
    s = 0
    for i in costs:
        s += i
    print(s)

def nested_loop():
    from itertools import permutations
    list = [0, 1, 2]

    for x in range(3):                                                  #najpierw wskakuje na 0
        for y in range(3):                                              #x == 0 i sie drukuje (0, 0) a potem x dalej jest rowne 0 ale y == 1 az dojdzie do odpowiedniego zakresu
            print(f"({x}, {y})", end=" ")                               #nie jest to poprawna permutacja
    print("\n")
    perm = permutations(list, 2)
    for i in perm:
        print(i, end=" ")

def challenge1():
    numbers = [5, 2, 5, 2, 2]
    for num in numbers:
        output = "x" * num
        print(output)
    print("\n")
    for i in numbers:
        print("x" * i)
    print("\n")
    for i in numbers:
        output = " "
        for z in range(i):                                              #pierwsza iteracja jest od 0 do 5 poniewaz w glownej petli i == 5 (z listy numbers)
            output += "x"                                               #potem idzie po kolei
        print(output)

def lists_2d():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]                                                                   #lista 2d to inaczej lista w liscie
    print(matrix[0][1])                                                 #pierwsza index to lista glowna a drugi index to z listy indexu glownego
    for row in matrix:                                                  #tak sie iteruje przez kazdy pojedynczy element w liscie 2d
        for item in row:
            print(item, end=" ")

#lista.insert(index, element ktory chcemy dodac)
#lista.index(element ktory chcemy znalezc) - zwraca index podanego elementu

def remove_list_duplicates():
    lista = [5, 2, 1, 11, 5, 7, 11, 2, 1, 1, 5, 8, 9, 8]
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    print(l)

#x, y, z = krotka / lista = w ten sposob przypisujemy do 3 zmiennych 3 pierwsze elementy z listy lub krotki

#METODY SLOWNIKOW ITP ZNALEZC W GOOGLE

def challegne2():
    slownik = {1: "jeden",
               2: "dwa",
               3: "trzy",
               4: "cztery",
               5: "piec",
               6: "szesc",
               7: "siedem",
               8: "osiem",
               9: "dziewiec",
               0: "zero"}
    liczba = list(input("Liczba: "))
    for i in liczba:
        print(slownik[int(i)], end=" ")

    #WERSJA Z FILMIKU
    print("\n")

    phone = input("Phone: ")
    digits_mapping = {"1": "one",
                      "2": "two",
                      "3": "three",
                      "4": "four"}
    output = ""
    for ch in phone:
        output += digits_mapping.get(ch, "!") + " "                 #.get odnajduje wartosc w slowniku a jak jej nie ma pokazuje wartosc domyslna ktora jest po przecinku
    print(output)

def emoji_converter():
    message = input("> ")                                           #nie mozemy uzyc funkcji list tutaj bo dzieli wtedy kazda pojedyncza litere/znak
    words = message.split(" ")                                      #dzieli str tam gdzie wystepuje spacja i wrzuca do listy
    emoji = {":)": "😊",
             ":(": "😥"}
    output = " "                                                    #koncowy str
    for word in words:
        output += emoji.get(word, word) + " "                       #.get szuka word w words i jak go nie znajduje domyslnie jest word i na koniec daje spacje
    print(output)

def errors():
    try:
        age = int(input("Age: "))                                   #po try wpisujemy blok kodu ktory moze wygenerowac blad
        print(age)
    except ValueError:                                              #po except wpisujemy jaki blad ma byc pominiety / moze byc kilka except z roznymi bledami
        print("Invalid value")                                      #oraz co ma wyskoczyc po jego wystapieniu wiec program sie nie zepsuje

#CLASS
#class nie jest wylacznie dla python lecz jest uzywany takze przez inne jezyki programowania
#sluza do okreslania nowych typow zmiennych (liczby, string, prawda/falsz, listy, slowniki)

def classy():
    class Point:                                                    #dobra praktyka programowania mowi ze przy okreslaniu class pierwsze litery nazwy sa z duzej litery
        def __init__(self, x, y):                                   #self jest odniesieniem do aktualnego obiektu ktory w domysle zawsze jest jako argument dlatego zawsze musi byc self przy defiowaniu funkcji
            self.x = x                                              #jest to tzw constructor
            self.y = y                                              #jest to rownoznaczne do np point.x = 10, gdzie point jest opisany jako self a drugi x to 10

        def move(self):                                             #wewnatrz class definujemy wszystkie funkcje i metody ktore chcemy by nalezaly do danej classy
            print("move")

        def draw(self):
            print("draw")
    #tworzac class tworzy plan nowego obiektu ktory mozemy przypisac do zmiennej


    point = Point(5, 15)                                            #w ten sposob przypisujemy wartosci do zmiennych wczesniej zdefiniowanych i nie musimy marowac linijek kodu na kolejne ich przypisywanie
    print(point.x)
    point1 = Point(10, 20)                                          #w ten sposob tworzymy nowy obiekt przypisany do zmiennej
    point1.x = 10                                                   #do stworzonego obiektu mozemy przypisac zmienne w ten sposob lub zmiennic wartosc zmiennej domyslnie przypisana
    point1.y = 20                                                   #nie trzeba tego tak definiowac jest wczesniej w class stworzymy tzw constructor
    print(point1.x)
    point1.draw()                                                   #w ten sposob mozemy wykonywac operacje na obiekcie poprzez wybranie okreslonej funkcji/metody z class

    point2 = Point(30, 40)                                          #to jest juz kompletnie nowy obiekt przypisany do nowej zmiennej
    print(point2.move())


def challenge3():
    class Person:
        def __init__(self, name):
            self.name = name

        def name(self):                                             #ta metoda nie dziala bo wyskakuje blad TypeError - str is not callable
            print(self.name)

        def talk(self, t):
            self.t = input(t)
            print(self.t)
            print(f"This is {self.name}")                           #to sie pojawia po wcisnieciu ENTER


    person = Person("Dawid")
    print(person.name)
    person.talk(f"trololo {person.name}")

def inheritance():
    class Mammal:                                                   #to jest class w ktorym wystepuja metody ktore chcemy dalej wykorzystywac
        def walk(self):
            print("walk")

    class Dog(Mammal):                                              #w ten sposob nowy class "dziedziczy" funkcje z innego miejsca
        pass                                                        #to piszemy kiedy nie ma metod specyficznych dla danego class zeby nie zostawiac go pustego

    class Cat(Mammal):
        def meow(self):
            print("meow!")

    dog1 = Dog()
    dog1.walk()

    cat1 = Cat()
    cat1.meow()
    cat1.walk()


def modules():
    import converters                                               #nowy modul z ktorego bierzemy projekty musi byc w folderze glownym python
    from converters import lbs_to_kg                                #ctrl + spacja = lista wszystkich funkcji w danym module

    print(converters.kg_to_lbs(70))
    print(lbs_to_kg(70))


def packages():
    #python package jest to folder w ktorym beda przechowywane inne moduly ktore mozemy uzyc wszedzie
    #__init__.py przez to python traktuje ten folder jako paczke z modulami

    import ecommerce.shipping                                       #w ten sposob importujemy caly modul z paczki
    ecommerce.shipping.cal_shipping()                               #w ten strzbnej funkcji przy importowaniu calosciowym

    from ecommerce.shipping import cal_shipping                     #w ten sposob importujemy tylko jedna fukcje ale posob musimy tak jakby podac sciezke do potrzeba tak jakby podac sciezke do niej
    cal_shipping()

    from ecommerce import shipping                                  #kolejny sposob na wywolanie modulu
    shipping.cal_shipping()                                         #dobry kiedy nie wiemy ktora funkcje chcemy z modulu i traktowana jest jako obiekt


def roll_dice():
    import random
    class Dice:
        def roll(self):
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            return x, y


    roll_dice = Dice()
    print(roll_dice.roll())

def files_and_directories():
    from pathlib import Path                                        #pathlib tworzy class do tworzenia obiekow do operacji na folderach i plikach

    #Absolute path
    #c:\Prigram FIles\Python
    #Relative path
    path = Path("ecommerce")                                        #jezeli nic nie podamy bedzie sie odnosic do aktualnie uzywanego folderu / do czego ma sie odnosic podajemy jako str
    print(path.exists())                                            #zwraca czy istnieje czy nie (True / False)
    path.mkdir()                                                    #tworzy nowy folder
    path.rmdir()                                                    #usuwa folder
    for file in path.glob("*.py"):                                  #do znalezenia czegos w danym folderze, * oznacza ze skanujemy wszystko / po kropce dajemy rozszerzenie pliku jaki chcemy znalezc
        print(file)                                                 #w ten sposob pokaza sie nam wszystkie pliki ktore szukamy


#pypi.org - nowe dodatkowe moduly z roznymi funkcjami tworzone przez innych / samemu tez mozna cos dodac


roll_dice()
import polyaxon_sdk