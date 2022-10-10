# WSZYSTKIE METODY ITP JEST W PDF Z KURSU
def ex1():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    lenght = len(my_string)

    print(lenght)


def ex4():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string.find("B"))


def ex7():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string.find("Bitcoin"))


def ex8():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string.startswith("X"))


def ex9():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string.swapcase()) #zamiana duzych liter na male i odwrotnie


def ex16():
    my_string = "In %s, someone paid %s %s for two pizzas."

    print(my_string % ("2010", "10k", "Bitcoin"))


def ex17():
    my_string = "In {}, someone paid {} {} for two pizzas."

    print(my_string.format("2010", "10k", "Bitcoin"))


def ex19():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string[-23: -16])


def ex21():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string[-9:])                                                                   # bez 9 pierwszych znakow


def ex23():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string[::7])                                                                   # zwraca co 7 element str


def ex25():
    my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

    print(my_string[:-4])                                                                   # bez 4 ostatnich znakow


def ex31():
    num1 = -11

    num2 = abs(num1)

    print(num2 == 11)                                                                       # zwraca odleglosc miedzy liczba w nawiasie do 0


def ex35():
    result = bool(150 % (10 ** 2 / 2))                                                      # zwraaca TRUE lub FALSE jesli jest jakas wartosc wewnatrz

    print(result)  # should return False


def zad42():
    my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

    my_list.extend([100, 101, 102])                                                         # dodawanie jedej listy do drugiej listy za pomoca odpowiedniej metody

    print(my_list)


def zad44():
    my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

    asc = sorted(my_list)                                                                   # w ten sposob tworzymy nowa liste a przez .sort() zmieniamy obecna

    print(asc)


def ex45():
    my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

    asc = sorted(my_list, reverse=True)                                                     # uporządkowana w odwrotnej kolejności

    print(asc)


def ex49():
    my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

    my_list.clear()                                                                         # usuwa wszystkie elementy z listy i zwraca pusta liste

    print(my_list)

# SETS
# set jest to niemutowalny obiekt bez powtorzen na ktorym mozna wykonywac add oraz remove
# frozenset jest to samo co set tylko ze nie mozna na nim wykonac jakichkolwiek operacji
# .pop() usuwa losowy obiekt z set powniewaz set jest NIEINDEXOWANY
# metody set sa w pliku z kursu


def ex71():
    # Przydzielanie elementow z krotki do konkretnej zmiennej
    my_tup = ("Romania", "Poland", "Estonia")

    (ro, po, es) = (my_tup[0], my_tup[1], my_tup[2])

    print(ro + ", " + po + ", " + es)  # returns 'Romania, Poland, Estonia

    my_tup = ("Romania", "Poland", "Estonia")

    (ro, po, es) = my_tup

    print(ro + ", " + po + ", " + es)  # returns 'Romania, Poland, Estonia'


def ex72():
    # w ten sposob mozna uzyskac ostatni element z listy str w kolejnosci alfabetycznej
    my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

    last = max(my_tup)

    print(last)  # should return Slovenia


def ex81():
    # zwraca range co 3
    my_range = range(10, 20, 3)

    print(list(my_range))  # [10, 13, 16, 19]

    my_range = range(10, 20)[::3]

    print(list(my_range))  # [10, 13, 16, 19]


def ex92():
    # usuwanie pary z dict za pomoca metody
    crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

    crypto.pop(3)

    print(crypto)


def ex100():
    # zwraca i usuwa ostanio dodany element
    crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

    crypto.popitem()

    print(len(crypto))


def ex112():
    # wykonuje sie gdy x to str i zaczyna sie z "T"
    x = "The days of Python 2 are almost over. Python 3 is the king now."

    if type(x) is str and x.startswith("T"):
        print("True!")


def ex113():
    # z jest w x lub y wystepuje co najmniej dwa razy w x
    x = "The days of Python 2 are almost over. Python 3 is the king now."

    if "z" in x or x.count("y") >= 2:
        print("True!")


def ex115():
    # sprawdza czy 3 ostatnie elementy str to liczby
    x = "The days of Python 2 are almost over. Python 3 is the king now."

    if x[-3:].isdigit():
        print("True!")
    else:
        print("False!")

def ex116():
    # czy dlugosc x jest wieksza lub rowna 8 oraz czy index 6 to float
    x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

    if len(x) >= 8 and x[6] == float(x[6]):
        print("True!")
    else:
        print("False!")

    x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

    if len(x) >= 8 and type(x[6]) is float:
        print("True!")
    else:
        print("False!")


def ex120():
    # jesli 115 wystepuje chociaz raz lub 115 jest pierwsze
    x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

    if 115 in x or x[0] == 115:
        print("True!")
    else:
        print("False!")

    x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

    if x.count(115) >= 1 or x.index(115) == 0:
        print("True!")
    else:
        print("False!")


def ex122():
    # czy 3 jest kluczem oraz czy najmnijesza wartosc alfabetycznie to C#
    x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

    if 3 in x.keys() and min(x.values()) == "C#":
        print("True!")
    else:
        print("False")

    x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

    if 3 in x and sorted(x.values())[0] == "C#":
        print("True!")
    else:
        print("False!")


def ex123():
    # czy ostatni element najwiekszej alfabetycznie wartosci to n
    x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

    if max(sorted(x.values()))[-1] == "n":
        print("True!")
    else:
        print("False!")

    x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

    if sorted(x.values())[-1][-1] == "n":
        print("True!")
    else:
        print("False!")


def ex125():
    # suma kluczy jest mniejsza niz dlugosc str z wartosci 5 pierwszysch kluczy
    x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

    if sum(x) < len(x[1] + x[2] + x[3] + x[4] + x[5]):
        print("True!")
    else:
        print("False!")


def ex135():
    # dlugosc najmniejszej wartosci jest rowna ilosci wystapienia a w kluczu 3
    x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

    if len(min(x.values())) == x[3].count("a"):
        print("True!")
    else:
        print("False!")

    x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

    if len(sorted(x.values())[0]) == x[3].count("a"):
        print("True!")
    else:
        print("False!")


def ex138():
    # for loop z odwrocona kolejnoscia:
    x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

    for i in x[::-1]:
        print(i * 10)

    x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

    for i in sorted(x, reverse=True):
        print(i * 10)

    x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

    for i in reversed(x):
        print(i * 10)


def ex139():
    # iterowanie przez liste i dzielenie przez dwa elementow a na koniec pokazanie wiadomosci
    # else wykonuje sie na koniec jak przy kazdym rodzaju petli
    x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

    for i in x:
        print(i / 2)
    else:
        print("Great job!")


def ex145():
    # wykonuje sie jesli spelniony jest warunek a jak x == 10 to robi cos innego
    x = 5
    y = 2

    while x >= 5 and x < 10:
        print(x * y)
        x = x + 1
    else:
        print(x / y)


def ex153():
    for i in range(1, 11, 2):
        if 3 <= i <= 8:
            # mnozy przez ostatni element z podanego zakresu czyli 10
            print(i * range(1, 11, 2)[-1])
        else:
            print("Outside!")


def ex159():
    # 2 sie nie pojawi jak w tym miejscu bedzie continue
    x = [1, 2]
    y = [10, 100]

    for i in x:
        for j in y:
            if i % 2 == 0:
                print(i * j)
                continue
            print(i)
        print(j)


def ex160():
    # jak sie spelnie warunek to przeskakuje dalej az bedzie 100 i sie druknie
    x = [1, 2]
    y = [10, 100]

    for i in x:
        for j in y:
            if i % 2 == 0:
                continue
                print(i * j)
            print(i)
        print(j)


def ex168():
    # to co po finally wykona sie z bledem czy bez bledu / mozna tez wstawic else ktore dziala tak jak w innych petlach
    try:
        print(25 % 0 ** 5 + 5)
    except:
        print("Bug!")
    finally:
        print("Result!")

# przy wyjatkach mozemy wywolac manualnie blad za pomoca raise
# wiec jezeli nie napiszemy przy except jaki to blad to przy raise except dalej sie wykona ale jeszcze pokaze sie blad
# po prostu raise wyrzuca blad na konsoli mimo wszystko

# assert sluzy z kolei do upewaniania sie ze wyniki danych funkcji sa takie jakie chcemy
# zwraca TRUE lub FALSE jest warunek jest spelniony
# sluzy glownie do sprawdzania czy program wykonuje sie poprawnie w penych miejscach
# jezeli jest nie tak to wyskakuje assert error

# do assert i raise mozemy dodac dodatkowa informacje ktora pojawi sie jak wyskoczy blad


def ex177():
    # dodaje do listy mnozenie liczby podanej do funkcji
    def my_func(x):
        my_new_list = []
        for i in range(5):
            my_new_list.append(i * x)
        return my_new_list

    result = my_func(2)
    print(result)


def ex178():
    # usuwanie duplikatow krotka metoda / lecz potem niewiele mozna z tym zrobic
    def my_func(x):
        return list(set(x))

    result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
    print(result)


def ex184():
    # *args do poczytania jeszcze
    def my_func(x, *args):
        return x * args[1]

    result = my_func(5, 10, 20, 30, 50)
    print(result)

# *args pozwala nam przy wywolywaniu funkcji podac tyle argumentow ile chcemy
# przydatne jesli chcemy zrobic funkcje matematyczna z duza iloscia wartosci
# non-keyworded, variable-lenght argument list

# **kwargs keyworded, variable-lenght list
# keyworded znaczy ze do zmiennych przypisana jest nazwa kiedy wrzucamy ja do funkcji
# jest to bardziej slownik

# w obu przypadkach mozemy wpisac tyle zmiennych przy wywolywaniu ile chcemy


def ex190():
    # sposoby wyswietlania liczby przecinkowej z okreslona liczba liczb po przecinku
    from math import pi

    print(round(pi, 4))
    print("%.4f" % pi)

# with open("python.txt", "w") as f
# w ten sposob nie trzeba zamykac pliku po skonczeniu pracy z nim


# MODUL RE - regular expression
# sluzy do znajdowania oraz dopasowywania str lub setow str
# flagi - sluza do modyfikowania szukania np pominiecie duzych i malych liter
# jezeli zaczniemy wyszukiwanie od r" " to zwrocony zostanie surowy str
# a przy wywolaniu group() zostanie zwrocona krotka z pasujacymy wzorami

# inne sposoby na sprawdzenie czy str sie zaczyna od podanych znakow:
# result = re.search("^Bitcoin was", s, re.I)
# result = re.match(r"B.{6} .{3}", s)
# a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
# kazdy nawias to inna grupa - dokladniej opisane jest w pliku z kursu

# w obu przypadkach jest to samo
# result = re.search(r'(\d\d\d\d)', s)
# result = re.search(r"(\d{4})\s", s)
# .*? - pomiedzy znaczy ze sa to jakiekolkwiek znaki wystepujace pomiedzy
# result = re.search(r"(\d{4}).*?(\d{4})", s)

# result = re.search(r"(.{3}\s\d\w\w\s\d{4})\s", s)
# .{3} - 3 dowolne znaki
# \s - spacje itp
# \d - liczby
# \w - litery itp

# result = re.search(r"(\w{2}[A-Z])", s) - szukanie str z 3 duzymi literami
# result = re.search(r"([A-Z]{3})", s) - to samo co wyzej
# \$ lub [$] - znaczy to samo czyli szukanie znaku $
# result = re.search(r"\s(.{6} .{3} .{2})\s", s) - szukanie slow o konkrenej dlugosci ze spacjami pomiedzy
# result = re.search(r"(\d{3}\,\d{3}\,\d{3}\,\d{3})", s) - liczba z duza iloscia przecinkow
# result = re.search(r"\$(\d{3},[0-9]{3},\d{3},[0-9]{3}),", s) - to samo co wyzej
# result = re.search(r"(\d\d,\d{3}\.\d\d)", s) - kropka tutaj oznacza kropke a nie dowolny element
# result = re.search(r"\$(\d{1,3},\d{1,3}\.\d{1,3}),", s) - to samo co wyzej
# result = re.search(r"(\d\d,\d{3},\d{3} [A-Z]{3})", s) - zamiast \s mozna dac zwykla spacje (chyba)
# result = re.search(r"\s([0-9]{2},[0-9]{3},[0-9]{3}\s.{3}),", s) - to samo co wyzej
# result = re.search(r"(\d{2}.\: \d\.\d{2}.)", s) - szukanie dziwnej liczby
# result = re.search(r"\s(.{4}\s\d\.\d\d%)", s) - szukanie dziwnej liczby
# result = re.search(r"([A-Z][a-z]{5} \d{2}[a-z]\: \$\d{2},\d{3},\d{3},\d{3})", s) - dlugie szukanie z roznymi literami, znakami i liczbami
# result = re.search(r"\.\d\d, (.{1,}:\s\$\d{2,},\d{2,},\d{2,},\d{2,}), ", s) - to samo co wyzej ale tego nie rozumiem
# result = re.search(r"(\w+ \w+: \d{2}.+? [A-Z]{3}), ", s) - bardzo dlugi ciag znakow

# result = re.findall(r"([2]..[3-9])", s) - szukanie dat / zaczyna sie od 2 potem .. a na komniec liczba od 3 do 9
# result = re.findall(r"\s(\d{4})", s) - to samo co wyzej
# result = re.findall(r"(\d+)", s) - znajdowanie wszystkich liczb w lancuchu
# result = re.findall(r"\d{1,}", s) - to samo co wyzej
# result = re.findall(r"\s([a-zA-Z]{3})\s", s) - szukanie 3 literowych wyrazow
# result = re.findall(r"\s(\w{3})\s", s) - to samo co wyzej
# result = re.findall(r"(\b[A-Z][A-Za-z]+)", s) - slowa zaczynajace sie z duzej litery
# result = re.findall(r"([A-Z]{1}.+?)\s", s) - to samo co wyzej
# result = re.findall(r"(\bo.)\s", s) - slowa dwuliterowe zaczynajace sie od o
# result = re.findall(r"\s(o.{1})\s", s) - to samo co wyzej
# /s - poza nawiasem znaczy ze miedzy slowami jest spacja ale nie wyszukuje jej jako wzor wiec wyszukuje same slowa
# result = re.findall(r"([a-zA-Z]{8,})", s) - slowa zawierajace conajmniej 8 liter lub wiecej
# result = re.findall(r"\w{8,}", s) - to samo co wyzej
# result = re.findall(r"\s([ac]\w{2,})\s", s) - wyrazy co najmniej 3 literowe zaczynajace sie od a lub c

# result = re.sub(r"\s(\d{4})", " XXXX", s) - zastapienie dat XXXX
# result = re.sub(r"\s\d{4}", " XXXX", s) - to samo co wyzej
# result = re.sub(r"\d{1,},*\d*\.\d{1,}", ".", s) - wszystkie liczby przecinkowe w str zamienione na kropke
# result = re.sub(r"([A-Z]{3})", "Bitcoin", s) - zamiana BTC na Bitcoin
# result = re.sub(r"[0-5]", "8", s) - wszystkie liczby mniejsze lub rowne 5
# result = re.sub(r"[A-Z]\w{1,}|[6-9]", "W", s) - wyrazy zaczynajace sie od duzej litery lub liczby wieksze lub rowne 6

# DODATKOWE FUNKCJE CLASS SA W PLIKU Z KURSU
def ex232():
    class ClassOne(object):
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

        def square(self, p3):
            print(p3 ** 2)

    p = ClassOne(1, 2)
# wyswietlanie wczesniej zdefiniowanej zmiennej w
    print(p.p1)


def ex235():
    class ClassOne(object):
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

        def square(self, p3):
            print(p3 ** 2)

    p = ClassOne(1, 2)
# funkcja do okreslania wartosci zmiennej w klass
    setattr(p, 'p2', 50)
# funkcja do uzyskania wartosci zmiennej w klass
    print(getattr(p, 'p2'))


def ex236():
    class ClassOne(object):
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

        def square(self, p3):
            print(p3 ** 2)

    p = ClassOne(1, 2)
# zwraca TRUE lub FALSE
    print(hasattr(p, "p2"))

# LIST ITP COMPREHENSION (skrocanie)
# cph = [i for i in range(1,5)] - robi to samo co petla for tylko ze jest w jednej linijce
# cph = [i ** 2 for i in range(5, 25, 3) if i <= 16] - to samo co wyzej tylko ze z warunkiem
# cph = {i: i * 3 for i in range(9)} - to jest z kolei slownik

# Lambda functions - anonymous functions
# lambda arg1, arg2, ..., arg n: an expression using the arguments #general syntax
# lam = lambda x, y: x * y - najpierw definiujemy zmienne a potem po : definiujemy akcje
def ex247():
    lam = lambda list1: [x * y for x in range(1, 5) for y in list1]

    print(lam([1, 2]))
# definiujemy w ten sposob liste w funkcji lambda

# itertools sluzy do pracy z iterowalnymi obiektami (czyli takie ktore mozna wrzucic do petli)
# permutacje, kombinacje itp
# result = list(itertools.chain(list1, list2)) - tworzy liste z dwoch list
# for i in itertools.count(20, 2):   - liczy od 20 co 2
#     if i <= 31:                    - az do 31
#         print(i)
#     else:
#         break

# lam = lambda x: x < 5
# result = list(itertools.filterfalse(lam, range(10))) - zwraca argumenty ktore daja FALSE w lam

ex236()
