# type(zmienna) - zwraca typ podanej zmiennej
# id(zmienna) - pokazuje pozycje wartosci zmiennej w pamieci koputera
# '==' - odnosi sie do wartosci zmiennej a nie samej zmiennej
# 'is' - sprawdza czy zmienne sa identyczne
# '==' - id() pokaze dwie rozne pozycje
# 'is' - id() pokaze dwie takie same pozycje jesli zmienne sa identyczne
# identyczne czyli jedna zmienna ma za zmienna poprzednia
# myvar = 10   /   myvar2 = myvar - te sa identyczne

def lab1():
    a = 10
    b = 10
    c = 10
    # wsyzstkie maja taki sam wskaznik komorki bo wartosc jest taka sama
    # id() odnosi sie do wartosci zpisanej w danym wskazniku komorki dlatego sa one inne pozniej
    print(f"a = {id(a)}, b = {id(b)}, c = {id(c)}")

    a = 20
    print(f"\na = {id(a)}, b = {id(b)}, c = {id(c)}")

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [1, 2, 3]
    print(f"\na = {id(a)}, b = {id(b)}, c = {id(c)}")
    # wskazniki sa takie same poniewaz odnosza sie one do listy ktora jest umieszczona w danym miejscu pamieci
    # dlatego dodanie wartosci do listy nic nie zmienia bo wskazywana jest lista a nie warotsci
    a.append(4)
    print(f"\na = {id(a)}, b = {id(b)}, c = {id(c)}")

    x = 10
    y = 10
    print(f"\nx = {id(x)}, y = {id(y)}")
    # wskazniki sa takie same bo optymalizator poradzil sobie z obliczeniami i latwo okreslil pozycje
    y = y + 1 - 1
    print(f"\nx = {id(x)}, y = {id(y)}")
    # tutaj wskazniki beda inne bo oblicenia byly zbyt duze
    # dlatego zostaly przyppisane nowe wskazniki do wartosci zmiennej
    y = y + 1234567890 - 1234567890
    print(f"\nx = {id(x)}, y = {id(y)}")

# przy zmianie wartosci zmiennej przypisujemy jej tak naprawdze nowy obszar pamieci
# ten obszar pamieci z wartoscia jest niezmienny dlatego zmienne sa niezmienne tak naprawde
# zmieniamy tylko nazwe zmiennej
# przy listach jest inaczej
# list2 = list - jest to jedna taka sama zmienna
# dlatego przy dodaniu czegos do list2 dodane zostanie to mimo wszystko dodane do list
# dzieje sie tak poniewaz obie list maja taka sama pozycje w pamieci (ten sam znacznik)
# list.copy() - w ten sposob tworzymy kopie danej listy
# przez co otrzymuje nowa pozycje (znacznik) w pamieci komputera i zmiany nie ingeruja w oryginalna liste
# list3 = list[:] - tak tez mozna zrobic kopie


def lab2():
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    workdays = days.copy()
    workdays.remove("sun")
    workdays.remove("sat")
    print(days)
    print(workdays)

# kazda wartosc przypisana do zmiennej konwertowana jest na wartosc True
# jezeli zmienna jest pusta jest False lub jak jest 0
# dlatego mozna to wykorzystac w petlach ktore sie wykonaja jesli zmienna ma wartosc


def lab3():
    def displayoptions(options):
        for i in range(len(options)):
            print(f"{i + 1} - {options[i]}")
        print("Aby zakonczyc wcisnij 'Enter'")

        choice = input("Co wybierasz: ")
        return choice

    options = ['load data', 'export data', 'analyze & predict']
    choice = 'x'
    # dziala tak dlugo poki choice ma jakas wartosc rozna od zero
    while choice:
        # funkcja zostala przypisana do zmiennej by poprawnie sie wykonywala
        choice = displayoptions(options)
        if choice:
            try:
                # w bloku try dajemy doslownie caly fragment kodu ktory moze generowac blad
                choice_num = int(choice)
                if choice_num > 0 and choice_num <= len(options):
                    print("Correct choice!")
                else:
                    print("Wrong choice!")
            except ValueError:
                print("Wrong format! Try again!")
        else:
            print("END!")

# MODUL OS - modul do interakcji z systemem opracyjnym
# daje dodatkowe mozliwosci do pracy z plikami
# jest w domysle juz zainstalowany z pythonem
# w skrocie sa to funkcje systemowe na plikach (usuwanie, przenoszenie, itp.)
# os.remove(path) - funkcja usuwajaca plik z komputera
# os.path.isfile(path) - sprawdza czy podana sciezka wskazuje na istniejacy plik na komputerze

# str = r"cos tam" - to 'r' oznacza ze wszystkie elementy w str maja byc traktowane jako str
# tzw.: raw string
# open(path, 'x').close() - tworzy nowy plik a jesli juz istnieje to wyskakuje x czyli ze jest blad
# 'x' to jeden z trybow pracy z plikiem tekstowym
# oznacza stworzenie nowego pliku lub zwrocenie bledu jesli juz istnieje
# .close() na koniec oznacza ze plik zaraz po stworzeniu jest zamykany bo chcemy by byl pusty

# w zmiennych mozna dawac wyrazenia logiczne ktore beda sie wykonywac pokolei
# wyrzenie logiczne bedzie wtedy przyjmowalo wartosc pierwszego napotkanego warunku jesli jest 'or'
# dzieje sie tak bo Python czyta to od lewej do prawej
# czyli moze byc True, False lub None
# przy koniunkcji ('and') jezeli jedna wartosc ma false to cale wyrazenie jest false


def lab4():
    import os

    def files(path):
        # ta metoda nie trzeba na koniec zamykac pliku bo zamyka sie autmatycznie
        with open(path, 'r') as f:
            # najpierw odczytujemy plik
            re = f.read()
            # potem dopiero mozemy podzielic plik ze zmiennej do ktorej czytany plik zostal przypisany
            s = re.split()
            lenght = len(s)
        return lenght

    path = r"C:\Users\dziab\OneDrive\Dokumenty\temp\my_text.txt"

    result = os.path.isfile(path) and files(path)
    print(result)

    if os.path.isfile(path):
        print(files(path))
    else:
        print("Error!")
    # mozna to takze napisac tak
    os.path.isfile(path) and print(files(path))


# pass - specjalna instrukcja do przeskakiwania linijek kodu
# tak samo jak w klass mozna jej uzyc w innych petlach
# to polecenie nic nie robi (nic nie wyswietla ani nie przerywa petli)
# przydatne do uzywania w tej czesci kodu ktora nie jest jeszcze do konca zaimplementowana

# uproszczona skladnia if (podobne do funkcji lambda)
# zmienna = 'cos tam' if zmienna2 == cos else cos
# przydatne jesli jest tylko jedno proste dzialania do wykonania
# w wiekszych i bradziej rozbudowanych petalch mozna tak skrocic kod
# bardziej zlozona forma
# zmienna = 'cos tam' if zmienna2 == cos else 'cos tam' if zmienna2 == cos else cos
# po else wtedy jest drugi warunek if zakonczony znowu else
# skladnia uproszczona jest najlepsza do warunkow prostych i krotkich by skrocic nieznacznie kod


def lab5():
    price = 123
    bonus = 23
    bonus_granted = True
    print(price - bonus) if bonus_granted else price

    rating = 5
    print("very good") if rating == 5 else print("good") if rating == 4 else print("weak")
    # mozna tez tak
    # import datetime as dt
    # today = dt.date().today().strftime("%A")
    # to jest praktycznie to samo co nizej
    from datetime import datetime as dt
    # w ten sposob dostajemy atualny dzien tygodnia z modulu datetime
    # dodatkowo skracamy nazwe modulu piszac 'as' i nowa nazwe po tym
    # sa w nim operacje z czasem i data
    # "%A" - zwraca dni tygodnia po angielsku z modulu datetime
    today_day = dt.today().strftime("%A")

    if today_day == "Monday":
        print("Ja nie moge bo pomagam mamie!")
    elif today_day == "Tuesday":
        print("Mam w domu pranie!")
    elif today_day == "Wednesday":
        print("Mam w domu pranie!")
    elif today_day == "Thursday":
        print("Mam dyżur!")
    elif today_day == "Friday":
        print("Mam dwa zebrania!")
    elif today_day == "Saturday":
        print("Na lekcje ganiam!")
    else:
        print("Ale za to niedziela bedzie dla nas!")
    #mozna to skrocic zaczynajac tylko od print a reszte kodu umiescic w nawiasie
    # print(".." if ... else '..' if ... else ...)
    print("Ja nie moge bo pomagam mamie!") if today_day == "Monday" else print("Mam w domu pranie!") if today_day == "Tuesday" else print("Mam w domu pranie!") if today_day == "Wednesday" else print("Mam dyżur!") if today_day == "Thursday" else print("Mam dwa zebrania!") if today_day == "Friday" else print("Na lekcje ganiam!") if today_day == "Saturday" else print("Ale za to niedziela bedzie dla nas!")


def lab6():
    import os
    # modul do pracy z linkami, stronami, cookies itp
    # mozna tez za pomoca tego dopisac link strony do pliku html
    import urllib.request

    data_dir = r"C:\Users\dziab\OneDrive\Dokumenty\temp"
    pages = [{'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
        {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
        {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

    for page in pages:
        try:
            # tworzenie nazwy pliku z koncowka .html
            file_name = f"{page['name']}.html"
            # tworzenie pliku html
            path = os.path.join(data_dir, file_name)
            # zapisane adresu strony w pliku html
            urllib.request.urlretrieve(page["url"], path)
        except:
            print("Error!")
            print('FAILURE processing web page: {}'.format(page["name"]))
            break
    else:
        print("Done!")


def lab6_2():
    import urllib.request
    import os

    data_dir = 'c:/temp'
    pages = [
        {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
        {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
        {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

    for page in pages:

        try:
            file_name = "{}.html".format(page["name"])
            path = os.path.join(data_dir, file_name)

            print("Processing: {}  => {} ...".format(page["url"], file_name))
            urllib.request.urlretrieve(page["url"], path)
            print('...done')

        except:
            print('FAILURE processing web page: {}'.format(page["name"]))
            print('Stopping the process!')
            break

    else:
        print('All pages downloaded successfully!!!')

# list = range(10) po wyswietleniu pokaze sie jaki ma range a nie lista z liczbami w podanym zakresie
# czyli pokaze sie range(0, 10)
# a jej klasa bedzie range a nie lista
# mozemy to skonwertowac do listy za pomoca funkcji 'list'


def lab7():
    colors = ["red", "orange", "green", "violet", "blue", "yellow"]

    def get_colors(n, colors):
        return colors[:n]
    # Zaczyna sie od jeden poniewaz chcemy by zaczelo wyswietlac pokolei kazdy element od pierwszego
    # pierwszy wycinek bedzie zatem [:i] czyli [:1]
    # ostatni jest plus jeden by wyswietlic ostatni element ktory bez tego sie nie wyswietli
    for i in range(1, len(colors) + 1):
        print(get_colors(i, colors))

    korpo = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu."
    # po pierwsszym indexie jest +1 by nie uwzgledniac pierwszego nawiasu
    # gdybysmy tego nie zrobili pokazałby sie pierwszy nawias
    print(korpo[korpo.index("(")+1:korpo.index(")")])

# enumerate - fukcja sluzaca do numerowania list itp
# takiego obiektu nie mozna latwo wyswietlic
# nalezy najpierw skonwertowac go do listy i potem wyswietlic
# enu = list(enumerate(lista))
# zwraca potem liste krotek gdzie znajduje sie kazdy element oryginalnej list z przypisanym numerem od 0
# sluzy glownie do uporzadkowania nieuporzadkowanych zbiorow danych

# polecenie 'zip' ma za zadanie polaczyc dwie niezalezne listy
# zip(lista1, lista2)
# tego tez nie mozna normalnie wyswietlic i trzeba go przypisac do listy

# for pos, (m, d) in enumerate(zip(lista1, lista2))
# pos przypisawane jest przez enumerate
# potem jest wykonywane polecenie zip i przypisywane jest kolejno 'm' oraz 'd'
# w ten sposob jest latwiej poniewaz nie trzeba sie meczyc z przypisywaniem do listy oraz potem idexowanie w petli for


def lab8():
    projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
    leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

    for p, l in zip(projects, leaders):
        print(f"The leader of {p} is {l}")

    print("\n")
    dates = ['2016-06-23', '2016-08-29', '1994-01-01']
    # w zip mozna dawac wiecej niz dwie listy
    for p, d, l in zip(projects, dates, leaders):
        print(f"The leader of {p} started {d} is {l}")

    print("\n")
    # do enumerate mozna dodac 1 by zaczynalo sie od 1
    for pos, (p, d, l) in enumerate(zip(projects, dates, leaders)):
        print(f"{pos + 1} - The leader of {p} started {d} is {l}")

# slownik = dict(zip(lista1, lista2)) tworzenie slownikow
# iterowanie po slowniku
# for key in dict
#    print(key, dict[key])
# dokladniej opisane w pliku 'przypomnienie.py'
#             for x, y in tree.items():
#                 print("Dziadek ", x, "ma syna/wnuka: ")
#                 for z in y:
#                     print(z + ",", y[z])
# jezeli chcemy tylko same wartosci mozemy wykorzystac metode values itp
# kolejnosc w slowniku w zaleznosci od wersji python moga byc rozne


def lab9():
    # moje dziala ale nie wyswietla tak jak w instrukcji
    banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    ammount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dict_denominations = dict(zip(banknotes_coins, ammount))

    dict_denominations[100] += 1
    dict_denominations[20] += 1
    dict_denominations[5] += 1
    dict_denominations[0.5] += 1

    dict_denominations[50] += 1
    dict_denominations[20] += 2
    dict_denominations[5] += 1
    dict_denominations[2] += 2

    dict_denominations[100] += 1
    dict_denominations[50] += 1
    dict_denominations[2] += 1

    for key in dict_denominations:
        print(f"Denominate: {key} - ammount {dict_denominations[key]}")


def lab9_2():
    # z odpowiedzi do lab
    banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    dict_denominations = {}
    # dodawanie wartosci do klucza w pustym slowniku z listy kluczy
    for b in banknotes_coins:
        dict_denominations[b] = 0

    dict_denominations[100] += 1
    dict_denominations[20] += 1
    dict_denominations[5] += 1
    dict_denominations[0.5] += 1

    dict_denominations[50] += 1
    dict_denominations[20] += 2
    dict_denominations[5] += 1
    dict_denominations[2] += 2

    dict_denominations[100] += 1
    dict_denominations[50] += 1
    dict_denominations[2] += 1

    for key in dict_denominations:
        # nominal maksymalnie 6 znakow oraz dwie liczby po przecinku
        # ilosc maksymalnie 5 znakow
        print("Denominate: {0:6.2f} - amount {1:5}".format(key, dict_denominations[key]))

# petla for tez moze byc jedno linijkowa
# robi sie tak samo jak petle if tylko moze byc bez else
# podobnie jest ze slownikami i listami
# lista = [ (a,b) for a in .....] - lista krotek z dwoch list
# slownik = { a:b for a in .....} - slownik z dwoch list ale nalezy pamietac o zasadach slownika


def lab10():
    # nie wiem czy do konca dobrze ale zrobilem to sam
    ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
    # ten sie dubluje
    lines = [(a, b) for a in ports for b in ports if a != b]
    print(lines)
    print(len(lines))

    # rozwiazanie z odp do lab

    routes = [(start, stop) for start in ports for stop in ports]
    print(routes)
    print(len(routes))

    routes = [(start, stop) for start in ports for stop in ports if start != stop]
    print(routes)
    print(len(routes))
    # tutaj chodzi chyba o kolejnosc alfabetyczna
    # w przypadku str kiedy jest znak < lub > to jest wyzej lub nizej w alfabecie
    # czyli poczatek alfabetu jest mniejszy niz koniec alfabetu
    # tak samo jak min oraz max przy string
    routes = [(start, stop) for start in ports for stop in ports if start < stop]
    print(routes)
    print(len(routes))

# generator to zapis informacji jak dalej nalezy generowac dany obiekt
# wyglada jak zagniezdzona petla for w jednej linijce
# generator tworzy sie tak jak list z petla for tylko uzywa sie normalnych nawiasow ()
# gen = ((a,b) for a in .....)
# przydaje sie w momentach gdzie do przetworzenia jest bardzo duzo danych
# nie marujemy w ten sposob pamieci co sie dzieje przy normalnej pracy na listach itp
# zeby wywolac wartosc z generatora nalezy obiekt poprzedzic formula 'next'
# w ten sposob pierwszy element z generatora zostanie wygenerowany
# kolejne trzeba wywolywac w ten sam sposob
# mozna tez wrzucic to do petli for co wygeneuje od razu wszystkie wartosci z generatora
# jezeli cos zostalo wygenerowane raz w obojetnie jaki sposob to drugi raz nie zostanie ten obiekt wygenerowany
# by wygenerowac dane od nowa nalezy znowu zdefiniowac generator
# przy recznym generowaniu wartosci w pewnym momencie wyskoczy nam blad
# dlatego mozna to wrzucic w petle (np. while) a potem w blok try/except
# w ten sposob przy wygenerowaniu bledu petla zakonczy sie


def lab11():
    ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

    routes = ((start, stop) for start in ports for stop in ports)
    counter = 0
    for start, stop in routes:
        print(f"{start} - {stop}")
        counter += 1
    print(counter)

    routes = ((start, stop) for start in ports for stop in ports if start != stop)
    counter = 0
    for start, stop in routes:
        print(f"{start} - {stop}")
        counter += 1
    print("\n", counter)

    routes = ((start, stop) for start in ports for stop in ports if start < stop)
    counter = 0
    for start, stop in routes:
        print(f"{start} - {stop}")
        counter += 1
    print("\n", counter)

# eval() - pobiera od uzytkownika fragment kodu ktory mozna samodzielnie uzyc w python
# przyjmuje tylko jedna linijke tekstu z kodem
# dzieki temu fragment kodu mozna przechowywac w bazie danych
# kawalek programu zapisywany jest jako zwykly string
# eval() wykonuje wtedy to co jest zapisane w fragmencie kodu
# tylko proste fuckcje programu
# nie mozna samodzielnie przypisywać wartosci zmiennych w funkcji
# wynik eval() nalezy przypisac do zmiennej
# maly problem jest taki ze mozna uzyskac dostep do danych bez wiedzy uzytkownika glownego
# dzieje sie to poprzez odwolanie sie w eval() do odpowiedniego fragmentu kodu
# drugi argument opcjonalny to srodowisko ze zdefiniowanymi zmiennymi

# globals() - pokazuje wszystkie domyslne funkcje python w danej sesji oraz wszystkie zdefiniowane zmienne
# globals() to inaczej slownik i mozemy go przypisac do zmiennej
# tworzac kopie globals().copy() tworzymy kopie tego slownika
# nastepnie mozemy usunac te klucze ktore nie chcemy by osoby postronne mialy dostep
# tworzac zmienna globals = {} tak jakby usuwamy cale srodowisko ale dostep do zmiennych dalej pozostaje
# dalej jednak mozna uzyskac sciezke do pliku glownego za pomoca odpowiedniej komendy


def lab12():
    import math

    f1 = "2*x"
    f2 = "math.sin(x)"
    f3 = "3*x**2+2*x-4"
    argument_list = []

    for i in range(100):
        argument_list.append(i/10)
    print(argument_list)

    formula = input("Podaj funkcje (x jako zmienna): ")
    for x in argument_list:
        # ten sposob jest przydatny jesli w str chcemy umiescic liczbe przecinkowa o okreslonej dlugosci
        print("{0:3.2f} {1:6.2f}".format(x, eval(formula)))

# exec() - funkcja ktora po uruchomieniu nie zwraca zadnej wartosci
# zmienia ona wartosci zmiennych w kodzie
# uzytkownik moze zmienic wartosci krytycznych zmiennych znajdujacych sie w programie
# przyjmuje fragment kodu ktory zawiera wiecej niz jedna linia kodu
# mozna w ten sposob wrzucic cala petle do funkcji albo zdefiniowac nowe zmienne w podanym fragmencie kodu
# nowe zmienne w exec() przy wywolywaniu pokazuja blad
# dzieje sie tak poniewaz sa one dopiero tworzone przy wywolaniu funkcji exec
# ktorej fragment kodu wraz z nowa zmienna zapisany jest jeszcze jako str w kodzie zrodlowym do wykorzystania

# oba rodzaje funkcji sa uzyteczne i niebezpieczne jednoczesnie
# mozna w pliku zapisywac podane przez uzytkownika fomuly i fragmenty kodu
# nastepnie za pomoca eval() lub exec() odnosic sie do odpowiednich fragmentow z pliku
# niestety daje to zbyt duza mozliwosc na zmiane waznych fragmentow kodu oraz zmiennych


def lab13():
    import os

    files_to_process = [
        r"C:\Users\dziab\OneDrive\Dokumenty\temp\funkcja1.txt",
        r"C:\Users\dziab\OneDrive\Dokumenty\temp\funkcja2.txt"
    ]

    for file in files_to_process:
        with open(file, "r") as f:
            # ta funkcja wczytuje nam tylko nazwe pliku z podanej sciezki do niego
            name = os.path.basename(file)
            print(f"Name of the file is: {name}")
            # odczytujemy dany plik w calosci
            result = f.read()
            # nastepnie sie wykonuje kod wczytany z pliku
            # jesli damy to w print() to najpierw sie wykona kod z pliku a potem wyskoczy None
            # None wyskakuje ze wzgledu na to ze chcemy wysiwetlic formule exec() a nie wynik kodu
            exec(result)


# kompilacja to inaczej wykonywanie przez program zadanego kodu
# compile(co kompilujemy, zrodlo(plik), tryb) - jest to funkcja ktora prekompiluje fragment kodu
# w drugim miejscu nie musimy koniecznie podawac sciezki do pliku jak go nie ma
# mozna wtedy napisac cokolwiek
# przy podawaniu sciezki do pliku podczas wystapienia bledu mozna latwo znalezc plik ktory generuje blad
# przy prekompilacji zmienna przechowuje fragment kodu do wykonania w postaci binarnej przypisanej do kodu
# nastepnie uzywamy exec() lub eval() w zaleznosci jaki tryb umiescilismy w compile()


def lab14():
    import math
    import time

    formulas_list = ["abs(x**3 - x**0.5)",
                     "abs(math.sin(x) * x**2)"]

    argument_list = []
    for i in range(1000000):
        argument_list.append(i / 10)

    start = time.time()
    results_list = []
    for formula in formulas_list:
        print(f"Current formula: {formula}")
        for x in argument_list:
            # eval dziala tutaj lepiej niz exec poniewaz exec zwraca pusty obiekt
            # eval wykonuje tutaj polecenie w kodzie i zwraca wartosc
            result = eval(formula)
            results_list.append(result)

    stop = time.time()
    maks = max(results_list)
    mini = min(results_list)
    time_not_compiled = stop - start
    print(f"Time = {time_not_compiled}, MAX = {maks}, MIN = {mini}")

    print("\n")

    start = time.time()
    results_list = []
    for formula in formulas_list:
        print(f"Current formula: {formula}")
        # w ten sposob wykonalo sie praktycznie 20x szybciej niz pierwszym sposobem
        # formula jako wartosc zmiennej formula w petli
        # formula drugi raz to zmienna sama w sobie ktora jest zrodlem wyrazenia
        compiled = compile(formula, formula, "eval")
        for x in argument_list:
            result = eval(compiled)
            results_list.append(result)

    stop = time.time()
    maks = max(results_list)
    mini = min(results_list)
    time_compiled = stop - start
    print(f"Time = {time_compiled}, MAX = {maks}, MIN = {mini}")


# podczas definiowania funkcji nalezy pamietac o kolejnosci argumentow wprowadzanych do funkcji
# dlatego jak przypiszemy wartosc do pierwszego argumentu a do drugiego nie to wyskoczy nam blad
# argumenty domyslne najlepiej podawac jako ostatnie
# mozna je wtedy pominac przy wywolywaniu funkcji


def lab15():
    def show_progress(n, character="*"):
        print(character * n)

    show_progress(10)
    show_progress(15)
    show_progress(30)

    show_progress(10, '-')
    show_progress(15, '+')


# *args to krotka (lista) z wartosciami ktore mozna w dowolnej ilosci dodac do funkcji
# moze byc inna nazwa
# wazne by przed ta nazwa byla '*' co oznacza ze mamy doczynienia z wieksza iloscia wartosci w funkcji
# sa to argumenty bez nazwy

# **kwargs sa to argumenty w funkcji ktore maja nazwe
# mozemy je rowniez wpisywac w dowolnej ilosci lecz musza byc one nazwane
# tym przypadku mamy doczynienia ze slownikiem
# jezeli do funkcji wrzucamy liste lub slownik jako argument nalezy nzawy obu poprzedzic '*' lub '**'
# w ten sposob zostana one odczytane odpwiednio
# uzywajac *args oraz **kwargs mozemy tworzyc funkcje ktore sa bardziej elastyczne pod wzgledem przyjmowanych argumentow


def lab16():
    def calclate_paint(efficiency, *args):
        total = sum(args)
        result = efficiency * total
        return result

    print(f"Paint needed: {calclate_paint(5, 25, 4, 5, 12, 19)} ltr")
    rooms = [22, 12, 11, 10, 5, 2, 8]
    print(f"Paint needed: {calclate_paint(7, *rooms)} ltr")

    def log_it(*args):
        path = r"C:\Users\dziab\OneDrive\Dokumenty\temp\log_it.txt"
        # 'a' jest po to by dodawac do pliku
        with open(path, 'a') as f:
            for str in args:
                # w ten sposob kazdy element, nie wazne kiedy wywolany, bedzie od nowej lini
                f.write(str + "\n")
                # ta spacja jest po to by przy drugim wywolaniu miedzy elementami byla spacja
                f.write(" ")
            # to daje nam kolejna dodatkowa nowa linie po pierwszym wywolaniu
            f.write("\n")

    log_it('Starting processing forecasting')
    log_it('ERROR', 'Not enough data', 'invoices', '2020')


# fukncje mozna przypisac do zmiennej w nastepujacy sposob
# zmienna = nazwa_funkcji - pomijamy wtedy nawiasy i ewentualne argumenty wejsciowe
# W ten sposo tak jakby zmienia sie nazwa funkcji
# wtedy funkcje mozna wywolac tak - zmienna(argumenty)
# przypisac tak mozna cala liste funkcji
# potem mozna uzyc petli for
# instructions - lista z funkcjami
# for instr in instructions:
#   instr(argument)
# w ten sposob wykona sie cala lista funkcji naraz pokolei z podanym argumentem
# nie trzeba wtedy recznie tego wywolywac


def lab17():
    def double(x):
        return 2 * x

    def root(x):
        return x ** 2

    def negative(x):
        return -x

    def div2(x):
        return x / 2

    number = 8
    transformations = [double, root, negative, div2]
    print("Starting.....")
    tmp_return_value = number

    for t in transformations:
        # jezeli nie przypiszemy tego do zmiennej z numerem to za kazdym wartosc liczby sie nie zmieni
        # funkcje sie wykonaja ale wartosc liczby sie nie zmieni
        tmp_return_value = t(tmp_return_value)

    print(f"Final value is: {tmp_return_value}")


# funkcja moze stac sie argumentem w innej funkcji
# pozwala to na budowanie bardziej dynamicznego kodu
# nie rozdrabniamy sie w ten sposob zeby do kazdej mniejszej fukncji wywowalc wynik
# zamiast tego funkcja glowna sama wywoluje mniejsze funkcje i pobiera odpowiednio zdefiniowane argumenty do nich
# mniejsze babranie sie z drobiazgami takimi jak zapisywanie wynikow i dalsze ich przekazywanie
# w ten sposob wynik ktory chcemy uzyskac dostajemy od razu bez rozdrabniania sie na szczegoly


def lab18():
    def double(x):
        return 2 * x

    def root(x):
        return x ** 2

    def negative(x):
        return -x

    def div2(x):
        return x / 2

    def generate_values(func, l):
        return_values = []
        for i in l:
            x = func(i)
            return_values.append(x)
        return return_values

    x_table = list(range(11))

    print(generate_values(double, x_table))
    print(generate_values(root, x_table))
    print(generate_values(negative, x_table))
    print(generate_values(div2, x_table))


# funkcja moze wywolywac inna funkcje jako return
# funkcja w funkcji moze miec zadeklarowane argumenty ktore niekoniecznie sa zadeklarowane w glownej funkcji
# sa to tylko deklaracje co bedzie uzywane w danej funkcji nawet jesli znajduje sie ona w innej funkcji
# i ma zadeklarowane rozne argumenty

# def create_func(kind = '+'):
#     source = """
# def f(*args):
#   result = 0
#   for a in args:
#       result {}= a
#   return result
# """.format(kind)
#     exec(source, globals())
#     return f

# wywolujemy to w nastepujacy sposob:
# f_add = create_func('+')
# print(f_add(1,2,3,4,5))

# w ten sposob napisalismy funkcje ktora zwraca funkcje
# jest zapisane w "" poniewaz uzyjemy exec() do jej wykonania
# bez uzycia globals wyskoczy blad ze 'f' nie jest zdefiniowane
# dlatego jak uzyjemy globals() exec() bedzie pracowalo na kopi zmiennych globalnych w srodowisku
# i w trakcie wykonywania kodu zwroci 'f' czyli nie bedzie bledu
# bez tego zadna wartosc z globals() nie jest zwracana wiec generowany jest blad
# jest to tzw srodowisko pracy funkcji exec()
# przy wywolaniu glowniej funkcji podajemy wartosc kind ktora zamienia sie wedlug formatu string
# exec() wywoluje zapisany jako str fragment kodu
# wazne zeby niebylo wciec przy pisaniu fragmentu kodu bo moze byc blad


def lab19():
    from datetime import datetime

    def time_span_m(start, end):
        duration = end - start
        duration_in_s = duration.total_seconds()
        return divmod(duration_in_s, 60)[0]

    def time_span_h(start, end):
        duration = end - start
        duration_in_s = duration.total_seconds()
        return divmod(duration_in_s, 3600)[0]

    def time_span_d(start, end):
        duration = end - start
        duration_in_s = duration.total_seconds()
        return divmod(duration_in_s, 86400)[0]
# w nawiasie idzie po kolei - rok, miesiac, dzien, godziny, minuty, sekundy
    start = datetime(2019, 1, 1, 0, 0, 0)
    end = datetime.now()

    print(time_span_m(start, end))
    print(time_span_h(start, end))
    print(time_span_d(start, end))

    def create_function(span):

# tutaj jest ustawiana wartosc 'sec' na podstawie podanej wartosci
        if span == 'm':
            sec = 60
        elif span == 'h':
            sec = 3600
        elif span == 'd':
            sec = 86400

# trzeba w ten sposob napisac kod zrodlowy bo bedzie wyskakiwal blad ze jest za duze wciecie
        source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)
# globals() jest potrzebne by kod zadzialal bo inaczej nie bedzie mial zmiennych na ktorych moze pracowac
# jest to kopia zmiennych globalnych z aktualnej sesji
        exec(source, globals())
    # blad wyskakuje bo bedzie dopiero to sie wykonywac w trakcie pracy kodu
        return f

    f_minutes = create_function('m')
    f_hours = create_function('h')
    f_days = create_function('d')

    print(f_minutes(start, end))
    print(f_hours(start, end))
    print(f_days(start, end))


# wrapper jest to funkcja zewnetrzna ktora sluzy do obudowania innej funkcji
# wykonuje ona wtedy jakies dodatkowe zadanie niz fukcja wewnetrzna
# umieszczamy funkcje w innej funkcji i obuduwujemy ja dodatkowymi funkcjami
# przyklad:
# def wrapper(func)
#   def func_wrapper(*args, **kwargs):
#       'dodatkowe funkcje' -----> np.: print cos lub jakies zapisy do logu uruchomien
#       'funkcja do obudowania' -----> result = func(*args, **kwargs)
#       'return z funkcji wewnatrz' -----> zwracanie wartosci z funkcji wewnetrznej jesli jakies sa
#   return func_wrapper -----> zwracanie wrappera
# func.__name__ - jest to 'magiczna' funkcja ktora zwraca tylko nazwe danej fukcji
# obudowujac funkcje rezygnujemy tak jakby z wewnetrznej funkcji
# Wew_funkcja = wrapper(Wew_funkcja)
# w ten sposob funkcja wewnetrzna bedzie sie wykonywac wedlug instrukcji w wrapperze
# niestety robi sie to recznie i nie jest to koniecznie dobre rozwiazanie

# functools - modul zawierajacy funkcje do modyfikacji funkcji
# mamy wtedy mozliwosc do tzw dekoratorow
# przy takim rozwiazaniu najpierw definiujemy funkcje wrappera a potem kolejne funkcje
# przed nowa funkcja piszemy wtedy
# @wrapper_func
# jest to tzw dekorator
# w ten sposob nowa fukcja zostanie automatycznie obudowana przez wrapper
# nie bedzie wtedy konieczne by przypisywac jej do zmiennej
# PYTHON z automatu uruchomi wywolywana przez nas funkcje przez zdefiniowany wczesniej wrapper


def lab20():
    import time

    def wrapper(func):
        def wrapped_func(*args):
            time_start = time.time()
            v = func(*args)
            time_stop = time.time()
            print(f"Funkcja {func.__name__} wykonala obliczenia w czasie {time_stop - time_start}")
            return v
        return wrapped_func

# w ten sposob udekorowalismy funkcje dekoratorem ktorym jest wczesniejszy wrapper
# ten kod jest do wyjasnienia przez kogos innego
    @wrapper
    def get_sequence(n):

        if n <= 0:
            return 1
        else:
            v = 0
            for i in range(n):
                v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
            return v

    print(get_sequence(18))


# WRAPPER Z DODATKOWYMI ARGUMENTAMI
# mozna w takim przypadku uzyc sciezki do pliku gdzie maja byc zapisywane dodatkowe informacje
# ta sciezka nie jest jednak uzywana jako argument funkcji jeszcze na poziomie tworzenia funkcji wrapper
# dopiero jak wpiszemy wrapper w kolejna fukcje bedzie mozna uzyc sciezki dostepu do pliku
# def wrapper_log(path):
#   def wrapper(func):
#       def funkcja(*args, **kwargs):
#           ...
#           return result
#       return funkcja
#   return wrapper
# nastepnie przy dekorowaniu uzywamy sciezki dostepu do pliku
# @wrapper_log(sciezka do pliku)
# w ten sposob bedzie sie mniej dzialo w kompilatorze
# wszystkie dodatkowe dane beda zapisane w jednym pliku
# niestety to wszystko zapisuje dane tylko do jednego pliku
# zeby zapisywaly sie do innych plikow to przy odpowiednio udekorowanych funkcjach podajemy rozne sciezki
# w ten sposob mozna zapisywac wykonywane operacje funkcji w roznych plikach
# a dalej tworzymy tylko jeden wrapper


def lab21():
    import os
    import functools
    from datetime import datetime as dt

# to jest wrapper z argumentami i przyjmuje dwa argumenty
# pierwszy to nazwa wykonywanej operacji ktora bedzie wprowadzana recznie przy dekorowaniu odpowiedniej funkcji
    def wrapper_with_log_file(logged_action, log_path_file):
        # gdyby nie byly potrzebne argumenty to zaczynaloby sie od tego momentu
        def wrapper_with_log_to_known_file(func):
            # wrapper przyjmuje takie argumenty jakie ma przyjmowac funkcja do dekorowania
            # inaczej beda zle argumenty przy wywolaniu funkcji
            def real_wrapper(path):
                with open(log_path_file, "a") as f:
                    f.write(f"Akcja {logged_action}, zostala wykona na pliku {path}, o czasie {dt.now().strftime('%Y-%m-%d %H:%M:%S')} \n")
                return func(path)
            return real_wrapper
        return wrapper_with_log_to_known_file

# w taki sposob podajemy dodatkowe argumenty przy dekoratorze
    @wrapper_with_log_file("FILE CRATE", r"C:\Users\dziab\OneDrive\Dokumenty\temp\file_create.txt")
    def create_file(path):
        print('creating file {}'.format(path))
        open(path, "w+")

    @wrapper_with_log_file("FILE DELETE", r"C:\Users\dziab\OneDrive\Dokumenty\temp\file_delete.txt")
    def delete_file(path):
        print('deleting file {}'.format(path))
        os.remove(path)

# funkcja jest wywolywana z wlasnymi argumentami
# argumenty dekoratora zostaly podane w dekoratorze i sa inne niz te w funkcji
    create_file(r"C:\Users\dziab\OneDrive\Dokumenty\temp\dummy_file.txt")
    delete_file(r"C:\Users\dziab\OneDrive\Dokumenty\temp\dummy_file.txt")
    create_file(r"C:\Users\dziab\OneDrive\Dokumenty\temp\dummy_file.txt")
    delete_file(r"C:\Users\dziab\OneDrive\Dokumenty\temp\dummy_file.txt")


# WYSYLANIE MAILI Z PYTHON
# sluzy do tego modul smtplib
# niestety niektore poczty internetowe maja dodatkowe zabezpieczenia przed uzyskiwaniem do nich dostepu
# nalezy wtedy ustawic mozliwosc dostepu z mniej bezpiecznych aplikacji na koncie gmail lub podobnym

# do tego celu beda nam potrzebne nastepujace pyrzkladowe zmienne
# od_kogo -> czyli doslownie od kogo lub adres e-mail, czyli identyfikacja nadajacego
# do_kogo -> adres lub adresy do kogo beda wysylane maile
# temat -> temat wiadomosci
# tresc -> tresc wiadomosci e-mail
# funkcja message przyjmuje tylko od i do kogo oraz tresc
# funkcja send_mail wyciaga wszystko ze odpowiednio sformatowanej zmiennej 'message'
# wyglada ona nastepujaco:
# '''From: {od_kogo}
# Subject: {temat}
# {tresc}''' (tak z grubsza)
# dodatkowo potrzebujemy jeszcze dwie zmienne przechowujace nazwe uzytkownika i haslo
# laczac sie z poczta tworzymy jeszcze zmienna serwer
# pozniej wykorzystywana jest jak obiekt klasy
# serwer = smtplib.SMTP_SSL('smtp.gmail.com', 465) -> adres serwera oraz numer portu z ktorego wysylamy wiadomosci
# SMTP_SSL -> jest to rodzaj klienta obslugiwanego przez gmail
# w przypadku innych skrzynek mozliwe bedzie uzycie innych klientow z innym numerem portu
# serwer.ehlo() - przekazywanie danych kompuptera przez ktory nastepuje laczenie z serwerem
# serwer.login(user, password) - logowanie do serwera
# serwer.sendmail(user, do_kogo, message) - wysylanie maila przez python
# serwer.close() - zamykanie polaczenia z serwerem
# najlepiej cala ta procedue wpisac w blok 'try\except' w razie gdyby w trakcie wykonywania nastapil blad


def lab22_tylko_dla_przykladu():
    import smtplib

    mailFrom = "Your automation system"
    mailTo = ["mail1@gmail.com", "mail2@o2.pl"]
    mailSubject = "Message processed succesfully!"
    mailBody = '''Hello

This mail confirms that processing has finished without problems

Have a nice day!'''

    message = f"""From: {mailFrom}
Subject: {mailSubject}

{mailBody}"""

    user = "mail1@gmail.com"
    password = "123456789"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print("Mail sent")
    except:
        print("Error send")


# FUNKCJA DO WYSYLANIA E-MAIL
# do tego celu najlepiej uzyc funkcje partial
# zeby z niej skorzystac nalezy zaimportowac modul functools
# funkcja partial pozwala na zmniejszenie ilosci podawanych argumentow do glownej funkcji
# poprzez zapisanie stalych argumentow w funkcji partial
# partial_func = functools.partial(funcka glowna, argumenty stale)
# przy wywolywaniu uzywamy funkcji partial podajac tylko te argumenty ktore sie zmieniaja
# reszta argumentow w takim przypadku sa juz w domysle stale
# jezeli w partial podamy argumenty w zlej kolejnosci to przy wywolaniu powstanie blad
# dzieje sie to poniewaz funkcja chcac wywolac dany argument spodziewa sie czegos innego niz jest w partial
# a dokladniej to w partial predefiniowany jest argument ktory jest pomiedzy innymi argumentami
# dlatego przy wywolaniu nalezy wszystkie argumenty 'nazwac'


def lab23():
    # modul pozwalajacy na wysylanie polecen HTTP przez python
    import requests
    import os
    import functools

    def save_url_file(url, dir, file, msg):
        print(msg.format(file))

        r = requests.get(url, stream=True)
        file_path = os.path.join(dir, file)

        with open(file_path, "wb") as f:
            f.write(r.content)

    # jezeli nie zdefiniujemy wartosci atgumentow wczesniej nalezy to zrobic wewnatrz partial
    save_url_to_dir = functools.partial(save_url_file, dir=r'C:\Users\dziab\OneDrive\Dokumenty\temp', msg="Please wait: {}")

    url = 'http://mobilo24.eu/spis'
    file = 'spis.html'

    # argumenty sa przekazane w taki sposob bo nie sa one pokolei w funkcji
    # python domyslnie spodziewa sie czegos innego
    save_url_to_dir(url=url, file=file)

    url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
    file = 'logo.png'

    save_url_to_dir(url=url, file=file)


# OPTYMALIZACJA ZLE NAPISANEGO KODU PRZEZ CACHE
# @functools.lru_cache() - jest to dekoratow z modulu functools
# jego dzialanie polega na tym ze python zapamietuje wyniki juz wykonanych obliczen w pamieci
# dzieki temu raz wyliczone obliczenia z funckji zostana zwrocone z pamieci komputera
# funkcja ktora wykonuje te obliczenia nie zostanie w ten sposob wywolana kolejny raz
# w dekoratorze mozna zdefiniowac maksymalna ilosc elementow w pamiecu cache
# funkcja.cache_info() - zwraca informacje na temat tego ile znajduje sie elementow w pamieci
# niestety funkcje tak dekorowane musza byc deterministyczne
# czyli byc wywolywania z takimi samymi argumentami i zwracajaca zawsze ten sam wynik
# w takim przypadku czas, liczby losowe itp odpadaja


def lab24():
    import time
    import functools

    @functools.lru_cache(100)
    def fib(n):

        if n <= 2:
            result = n
        else:
            result = fib(n - 1) + fib(n - 2)

        return result

    start = time.time()
    for n in range(1, 41):
        print(f"{n} = {fib(n)}")
        partial = time.time()
        print(f"Partial time: {partial - start}")
    stop = time.time()
    print(f"Time overall: {stop - start}")
    print(fib.cache_info())


# WYRAZENIA LAMBDA
# f = lambda argument: cialo funkcji (jedno wyrazenie co dana funkcja ma robic)
# w ten sposob tworzy sie funkcje lambda
# lambda to funkcja anonimowa poniewaz nie definiujemy technicznie jej nazwy
# filter(fukncja, zmienne) - zwraca elementy ktore spelniaja warunki funkcji w argumentach
# w tym miejscu mozna takze umiescic funkcje lambda
# dlatego lambda to funkcja anonimowa poniewaz w takim przypadku nie nazwalismy jej w zaden sposob
# ten typ funkcji jest przydatny poniewaz proste wyrazenia mozna zapisac w calosci w jedej krotkiej linijce
# mozna tez jej uzyc w funkcji do wygenerowania kolejnej funkcji
# def func(n):
#   return lambda x: x * n
# new_func = func(3)
# print(new_func(2)) ----> w ten sposob wygenerowana zostala nowa funkcja ktora mnozy 3 razy x podawany pozniej
# funkcje lambda lepiej by nie byly zbyt skomplikowane


def lab25():
    text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

# funkcja do sprawdzania dlugosci elementu
    f = lambda lenght: len(lenght)

# map zwraca obiekt zawierajacy elementy powstale na podstawie podanej wewnatrz funkcji i iteratora (listy itp)
# map nie tworzy listy wiec trzeba ten obiekt manualnie zamienic na liste
    print(list(map(f, text_list)))

# to samo co wyzej tylko bez wczesniejszego okoreslania funkcji
    print(list(map(lambda s: len(s), text_list)))


def lab26():
    cake_01 = {'taste': 'vanilia', 'glaze': 'chocolade', 'text': 'Happy Brithday', 'weight': 0.7}

    cake_02 = {'taste': 'tee', 'glaze': 'lemon', 'text': 'Happy Python Coding', 'weight': 1.3}

    def show_cake_info(cake):
        print('{} cake with {} glaze with text "{}" of {} kg'.format(
            cake['taste'], cake['glaze'], cake['text'], cake['weight']))

    show_cake_info(cake_01)
    show_cake_info(cake_02)

    cakes = [cake_01, cake_02]

    for c in cakes:
        print(show_cake_info(c))


# KLASY PYTHON!!!!!!!!
# programowanie proceduralne - fukncje i zmienne zyja wlasnym osobnym zyciem
# posiadamy niezalezne dane i niezalezne funkcje i tworzymy z nich jeden algorytm
# to jest to co bylo do tej pory

# klasa laczy w sobie jednoczesnie funkcje i dane potrzebne do wykonania
# klasa jest jakby formularzem do ktorego wprowadza sie odpowiednie wartosci
# obiekt (instancja) klasy pozwala na odwolywanie sie do wszystkich wlasciwosci jakie posiada klasa
# self w klasie to obiekt ktory ma powstac z tej klasy
# self nie trzeba pozniej przekazywac bo jest on inicjowany atumatycznie
# self.zmienna - to jest definiowana wlasciwosc danego obiektu a po prawej stronie znajduje sie przekazany argument
# wczesniej zapisane argumenty przez __init__ trzeba potem przy tworzeniu obiektu przekazac do klasy
# __init__ ma za zadanie zainicjowac obiekt wartosciamy przkazanymi podczas tworzenia klasy


def lab27():
    class Cake:
        def __init__(self, name, kind, taste, addictions, filling):
            self.name = name
            self.kind = kind
            self.taste = taste
            self.addictions = addictions
            self.filling = filling

# obiekty z wczesniej utworzonej klasy
# mozna tez wewnatrz umiescic liste jako jeden z argumentow
    cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
    cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
    cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

    bakery_list = [cake01, cake02, cake03]

    print("Today in our offer!:")
    for c in bakery_list:
        print(f"{c.name}, kind: {c.kind}, taste: {c.taste}, with: {c.addictions} and {c.filling} filling\n")


# parametr 'self' w klasie odnoszaczy sie do danego obiektu pobierany jest automatycznie przez python
# self.atrybut - odnoszenie sie do atrybutow podczas tworzenia klasy


def lab28():
    class Cake:
        def __init__(self, name, kind, taste, addictions, filling):
            self.name = name
            self.kind = kind
            self.taste = taste
            self.addictions = addictions
            self.filling = filling

        def show_info(self):
            print(f"Name: {self.name.upper()}")
            print(f"Kind: {self.kind}")
            print(f"Taste: {self.taste}")
            if self.addictions:
                print(f"Addictions: {self.addictions}")
            if self.filling:
                print(f"Filling: {self.filling}")
            print("-"*20)

# zamiana nadzienia poprzez podane nadzienia przy wywolaniu metody klasy
# jezeli podajemy dodatkowe argumenty ktore wpisujemy tutaj nalezy potem je wpisac przy wywolaniu
        def set_filling(self, filling):
            self.filling = filling

# wprowadzanie nowego nadzienia poprzez user input
        def new_filling(self):
            filling = input("New filling: ")
            self.filling = filling

# reczne dodanie dodatkow poprzez wpisanie reczne dodatkow przy wywolaniu metody klasy
        def add_additives(self, additives):
            self.addictions.extend(additives)

# to samo co wyzej tylko ze automatyczne
# jezeli nie chcemy podawac argumentow przy funkcji podajemy je wewnatrz funkcji kiedy chcemy cos zrobic z nimi
        def set_additives(self):
            additives = []
            how_many = int(input("How many additives: "))
            for f in range(how_many):
                add = input("Type of additive: ")
                additives.append(add)
            return self.addictions.extend(additives)

    cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
    cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
    cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

    cake01.show_info()
    cake01.new_filling()
    cake01.show_info()

    print("\n")

    cake01.set_filling("cream")
    cake02.set_filling("cream")
    cake03.add_additives(["coconut", "choco sprinkles"])

    print("Today in our offer:")
    cake01.show_info()
    cake02.show_info()
    cake03.show_info()

    print("\n\n")

    bakery_offer = [cake01, cake02, cake03]

    cake01.set_filling("vanilla cream")

    print("Today in our offer:")
    for c in bakery_offer:
        c.show_info()


# klasy i obiekty klasy to nie to samo
# isistance(obiekt, klasa) - sprawdza czy dany obiekt nalezy do wskazanej klasy
# type(obiekt) is klasa - kolejna metoda sprawdzenia czy obiekt nalezy do wskazanej klasy
# w obu przypadkach zwracana jest wartosc True lub False

# obiekt.__class__ -  kolejna metoda na to samo co wyzej - zawiera info jak dany obiekt powstal i do ktorej klasy nalezy
# tutaj zwracane sa informacje dotyczace obiektu
# vars(obiekt) - zwracane sa informacje o atrybutach danego obiektu klasy
# vars(klasa) - zwracane sa informacje o atrybutach i funkcjach danej klasy lecz nie dotyczy to obiektu

# mozna zatem definiowac atrybuty na poziomie klasy
# robi sie to na poczatku tworzenia klasy przed funkcja __init__
# definiujemy wtedy potrzebne argumenty
# wtedy przy wywolaniu vars zmieniaja sie tylko i wylacznie informacje dotyczace klasy a informacje obiektu sa bez zmian
# mozna z nich skorzystac w funkcji __init__ np.:
# Klasa.zmienna += 1 ---> przy kazdym utworzniu obiektu liczba zwiekszy sie o jeden
# Klasa.zmienna.append(self) ----> kazdy stworzony obiekt zostanie dodany do listy
# self to inczej nowo stworzony obiekt ktory w __init__ przyjmuje nazwe self
# jest to przykladowe wykorzystanie zmiennych tylko i wylacznie w klasie ktore sie aktywuja po stworzenu obiektu
# poza klasa mozna je wywolac w ten sam sposob co tworzylismy
# Klasa.zmienna1 / Klasa.zmienna2
# zmiana tych argumentow wplywa dalej na wynik funkcji vars()
# zmienne te mozna wywolywac takze za pomaca obiektow klasy
# obiekt.zmienna_klasy1 / obiekt.zmienna_klasy2
# wywolany wynik jest taki sam w obu przypadkach

# dir(obiekt) - zwraca wszystkie funkcje nawet te ukryte oraz argumenty danego obiektu oraz te zdefiniowane w klasie
# dir(klasa) - robi to samo co wyzej lecz zwraca tylko te argumenty ktore zostaly zdefiniowane w klasie

# wada klas w python jest taka ze nie chronia one w zaden sposob swoich danych
# oznacza to ze w danym momencie pisania kodu mozna zmienic wartosci argumentow w klasie
# w momencie usuwania obiektow, ktore liczyla zmienna w klasie, licznik sie nie zmniejszy


def lab29():
    class Cake:
        known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
        bakery_offer = []

        def __init__(self, name, kind, taste, addictions, filling):
            self.name = name
            self.kind = kind
            self.taste = taste
            self.addictions = addictions
            self.filling = filling
            if self.kind in Cake.known_types:
                self.kind = kind
            else:
                Cake.known_types.append('other')
            Cake.bakery_offer.append(self)

        def show_info(self):
            print(f"Name: {self.name.upper()}")
            print(f"Kind: {self.kind}")
            print(f"Taste: {self.taste}")
            if self.addictions:
                print(f"Addictions: {self.addictions}")
            if self.filling:
                print(f"Filling: {self.filling}")
            print("-" * 20)

        def set_filling(self, filling):
            self.filling = filling

        def new_filling(self):
            filling = input("New filling: ")
            self.filling = filling

        def add_additives(self, additives):
            self.addictions.extend(additives)

        def set_additives(self):
            additives = []
            how_many = int(input("How many additives: "))
            for f in range(how_many):
                add = input("Type of additive: ")
                additives.append(add)
            return self.addictions.extend(additives)

    cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
    cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')
    print(cake04.known_types)

    print("Is istance: ", isinstance(cake01, Cake))
    print("Type: ", type(cake01) is Cake)

    print("Vars object: ", vars(cake01))
    print("Vars class: ", vars(Cake))

    print("Dir object: ", dir(cake01))
    print("Dir class: ", dir(Cake))


# UKRYWANIE i DODAWANIE ATRYBUTOW W KLASIE
# self.__zmienna - '__' sluzy do tworzenia wewnetrznych, czyli ukrytych, atrybutow
# w ten sposob ta zmienna przy probie pozniejszej zmiany poza klasa nie pojawi sie w liscie mozliwych zmiennych
# a proba jej zmiany spowoduje stworzenie nowej zmiennej
# a przy uruchomieniu vars() zmienna ta bedzie miala nazwe _Klasa__zmienna
# w ten sposob ukrywana jest ta wartosc ktora nie chcemy by inni zobaczyli lub zmienili
# niestety jesli zmienimy wartosc uzywajac tej zmienionej nazwy dalej jest mozliwosc jej zmienienia
# klasy w python nie bronia sie dobrze przed zewnetrzymi zmianami wartosci
# raz zdefiniowana klasa mozna byc zmieniana nawet po stworzeniu obiektu poprzez dodawanie nowych zmiennych

# del obiekt.zmienna - usuwanie danego atrybutu obiektu klasy
# setattr(obiekt, 'nazwa, wartosc) - tworzenie nowego atrybutu
# hasattr(obiekt, 'nazwa') - sprawdza czy dany obiekt klasy posiada dany atrybut
# delattr(obiekt, 'nazwa') - usuwanie danego atrybutu obiektu klasy
# takie mozliwosci modyfikowania w locie daje duze mozliwosci do tworzenia dynamicznego kodu

# przed tworzeniem klasy mozna zdefiniowac zmienne do ktorych bedziemy sie odwolywac wewnatrz klasy

# nie znajac dokladnej nazwy ukrytego argumentu mozna go zmienic tworzac odpowiednia funkcje do tego w klasie
# jest to jedna z metod do zmiany wartosci ukrytego argumentu
# najpierw pobieramy ukryty argument i zwracamy go czyli funkcja bedzie sie skladala tylko z:
# return self.__ukrytazmienna
# ustawianie nowej wartosci atrybutu mozna zrobic w kolejnej funkcji klasy
# def new_value(self, new_value)
#   self.__ukryta = new_value ----> przykladowa metoda zmiany wartosci
# w ten sposob przy wywolaniu trzeba kazdej metody uzyc osobno

# w ten sposob mozna uzyc mniej ilosci komend do wywolania funckji
# tworzy sie to wewnatrz klasy jako zmienna(argument) poza funkcjami(metodami)
# jest to tak jakby funkcja bez 'def'
# Wlasciwosc = property(metoda do pobrania wartosci zmiennej, metoda do zmiany tej wartosci,
#                       funkcja ktora moze usunac ten atrybut, opcjonalna dokumentacja dla tej wlasciwosci)
# dokumentacja czyli wiadomosc jaka bedzie sie wyswietlala
# uzywajac wlasciwosci klasy mozna latwo zmieniac wartosci ukrytych argumentow
# obiekt.Wlasciwosc = nowa_wartosc
# w ten sposob zmienia sie wartosc argmentu przy uzyciu odpowiednich funckji

# trzecia mozliwosc zmiany wartosci argumentu ukrytego to uzycie ukrytej nazwy ukrytego argumentu
# o trzeciej metodzie lepiej zapomniec

# metody tak jak argumenty moga byc ukryte
# nie mozna ich wtedy normalnie wywolac lecz mozna ich wtedy uzyc w 'property'
# ukrywanie atrybutow ktore nie powinny byc bezmyslnie zmieniane to dobra praktyka
# powinny one byc zmieniane wtedy wedlug odpowiedniej logiki

# METODY OPERUJACE NA POZIOMIE KLASY
# dzieki temu mozna stworzyc obiekt wywolujac funkcje z klasy
# nastepnie dzieki zapisanemu odpowiednio tekstowi mozna przekazac argumenty do klasy
# nie trzeba wtedy tworzyc obiektu normalna droga
# metoda dzialajaca na poziomie klasy powinna byc oznaczona dekoratorem @classmethod
# nastepnie w metodzie zamiast 'self' bedzie sie pojawialo 'cls' co znaczy ze jest to klasa a nie obiekt
# nowy_obiekt = cls(*text.split('separator'))
# w ten sposob zmieniamy tekst na argumenty do obiektu
# '*' sprawia ze argumenty z tektu sa traktowane osobno a nie jako jedna lista
# tworzac nowy obiekt robimy ---> obiekt = Klasa.funkcja(text)

# METODY STATYCZNE
# nie musza miec one zadnego zwiazku z klasa
# jedyny zwiazek wspolny to taki ze znajduja sie w klasie
# musi posiadac one dekorator @staticmethod
# nie posiada ona pierwszego argumentu 'self' lub 'cls'
# przy wywolaniu uzywamy klasa.nazwa_funkcji(argumenty)
# uzywane sa one dla utrzymania porzadku

# metody statyczne oraz klasy mozna uzywac takze na przy uzyciu obiektu
# metody w klasie to: metody obiektu, klasy oraz statyczne
# metody klasy nie moga operowac na podstawie argumentow zdefiniowanych w obiekcie

# modul pickle oraz glob w dokumencie tekstowym


def lab30_31_32():
    # zapisywanie plikow w formacie binarnym
    # pobiera obiekt i zamienia go na tekst
    import pickle
    # modul do listowania zawartosci danego katalogu
    import glob

    class Cake:
        known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
        bakery_offer = []

        def __init__(self, name, kind, taste, addictions, filling, gluten_free, text):
            self.name = name
            self.kind = kind
            self.taste = taste
            self.addictions = addictions
            self.filling = filling
            if self.kind in Cake.known_types:
                self.kind = kind
            else:
                Cake.known_types.append('other')
            Cake.bakery_offer.append(self)
# tworzenie ukrytych atrybutow w klasie
            self.__gluten_free = gluten_free
            if self.kind == "cake" or text == " ":
                self.__text = text
            else:
                # w ten sposob zmienna text staje sie pusta jesli jest cos innego niz 'cake'
                # wartosc none sprawia ze w show_info() jest false i ta informacja sie nie pojawia
                self.__text = None

        def show_info(self):
            print(f"Name: {self.name.upper()}")
            print(f"Kind: {self.kind}")
            print(f"Taste: {self.taste}")
            if self.addictions:
                print(f"Addictions: {self.addictions}")
            if self.filling:
                print(f"Filling: {self.filling}")
            print(f"Gluten free: {self.__gluten_free}")
            if self.__text:
                print(f"Text: {self.__text}")
            print("-" * 20)

        def set_filling(self, filling):
            self.filling = filling

        def new_filling(self):
            filling = input("New filling: ")
            self.filling = filling

        def add_additives(self, additives):
            self.addictions.extend(additives)

        def set_additives(self):
            additives = []
            how_many = int(input("How many additives: "))
            for f in range(how_many):
                add = input("Type of additive: ")
                additives.append(add)
            return self.addictions.extend(additives)

# ukryte metody klasy tworzone sa tak samo jak ukryte atrybuty
        def __get_text(self):
            return self.__text

        def __set_text(self, new_text):
            if self.kind == "cake":
                print(f"Changing Cake text from {self.__text} to {new_text}")
                self.__text = new_text
            else:
                print("Cannot change text!")

        Text = property(__get_text, __set_text, None, "If kind is Cake change text")

        def save_to_path(self, path):
            # 'wb' znaczy zapis w formacie binarnym
            # plik bedzie zapisany w 'path'
            with open(path, 'wb') as f:
                # 'self' to obiekt czyli to co bedzie zapisane w pliku
                # 'f' to zapisywany plik w formacie binarnym gdzie jest zapisany 'self'
                pickle.dump(self, f)

        @classmethod
        def read_from_file(cls, path):
            # odczytywanie pliku w formacie binarnym
            with open(path, 'rb') as f:
                new_cake = pickle.load(f)
            # dodawanie nowego obiektu do listy obiektow w klasie
            cls.bakery_offer.append(new_cake)
            return new_cake

        @staticmethod
        def get_bakery_files(path):
            # tworzenie listy plikow z podanym rozszerzeniem
            return glob.glob(path+'/*.bakery')

    cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, "Whazaap")
    cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, "")
    cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, "")
    cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, "")

    # cake01.show_info()
    # cake02.show_info()
    # cake03.show_info()

    # print("\n")

    # cake03.__gluten_free = False
    # cake03.show_info()
    # print(dir(cake03))

    # print("\n")

# to jest poprawna nazwa ukrytego atrybutu po utworzeniu go w klasie
    # cake03._Cake__gluten_free = False
    # cake03.show_info()

    # for c in Cake.bakery_offer:
        # c.show_info()


# uzywanie wlasciwosci klasy z uzyciem ukrytych metod oraz funkcji 'property' wewnatrz klasy
    # cake01.Text = 'Happy birthday!'
    # cake02.Text = '18'

    # for c in Cake.bakery_offer:
        # c.show_info()

# dziala to w pliku temp
# najwyrazniej funkcja pickle.dump nie dziala jako funkcja w innych fukcjach
# dziala w osobno stworzinym pliku
# tworzenie nowych plikow binarnych
    cake01.save_to_path('D:/temp/cake01.bakery')
    cake02.save_to_path('D:/temp/cake02.bakery')

# odczytywanie z pliku binarnego i tworzenie nowego obiektu
    cake05 = Cake.read_from_file('D:/temp/cake01.bakery')
    cake05.show_info()

# wyswietalnie listy plikow
    print(Cake.get_bakery_files('D:/temp/'))


# TWORZENIE WLASCIWOSCI ZA POMOCA DEKORATOROW
# @property - jest to dekorator do tworzenia wlasciwosci
# nie trzeba wtedy uzywac funckji 'property' tak jak to bylo opisane wczesniej
# odwolujemy sie wtedy do tej funkcji normalnie tak jak z innymi funkcjami tylko ze nie uzywamy nawiasow na koncu
# uzywamy tylko nazwy funkcji
# niestety jakakolwiek zmiana wartosci tej wlasciwosci sie nie uda
# mozna temu zaradzic w nastepujacy sposob
# metoda ktora zmienia wartosc nalezy oznaczyc specjalnym dekoratorem
# @Wlasciwosc.setter
# dodatkowo taka metoda musi miec ta sama nazwer co metoda do zwracania wartosci
# dodatkowo musi byc takze on po metodzie do zwracania wartosci
# tworzac metody w ten sposob zabezpieczamy je przed usunieciem
# czyli nie mozna usunac metody do zmiany ukrytej zmiennej
# mozna tylko zmieniac wartosci ukrytego atrybutu przy uzyciu tych metod
# zeby moc je usunac nalezy stworzyc nowa metoda i odpowiednio ja udekorowac
# @Wlasciwosc.deleter
# tez musi ona posiadac taka sama nazwe jak metoda zwracajaca wartosc
# wewnatrz nalezy wyzerowac wartosci argumentu

# tworzenie wlasciwosci za pomoca dekoratorow jest bardziej intuicyjne i prostsze


def lab33():
    class Cake:
        known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
        bakery_offer = []

        def __init__(self, name, kind, taste, addictions, filling, gluten_free, text):
            self.name = name
            self.kind = kind
            self.taste = taste
            self.addictions = addictions
            self.filling = filling
            if self.kind in Cake.known_types:
                self.kind = kind
            else:
                Cake.known_types.append('other')
            Cake.bakery_offer.append(self)
            self.__gluten_free = gluten_free
            if self.kind == "cake" or text == " ":
                self.__text = text
            else:
                self.__text = None

        def show_info(self):
            print(f"Name: {self.name.upper()}")
            print(f"Kind: {self.kind}")
            print(f"Taste: {self.taste}")
            if self.addictions:
                print(f"Addictions: {self.addictions}")
            if self.filling:
                print(f"Filling: {self.filling}")
            print(f"Gluten free: {self.__gluten_free}")
            if self.__text:
                print(f"Text: {self.__text}")
            print("-" * 20)

        @property
        def Text(self):
            return self.__text

        @Text.setter
        def Text(self, new_text):
            if self.kind == "cake":
                print(f"Changing Cake text from {self.__text} to {new_text}")
                self.__text = new_text
            else:
                print("Cannot change text!")

    cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
    cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
    cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
    cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

    print("Today in our offer:")
    for c in Cake.bakery_offer:
        c.show_info()

    cake01.Text = 'Happy birthday!'
    cake02.Text = '18'

    for c in Cake.bakery_offer:
        c.show_info()


# DYNAMICZNE DODAWANIE METOD DO KLASY

# statyczne definiowanie wlasciwosci to definiowanie w czasie definiowania klasy
# modul 'csv' - importowanie danych do pliku csv czyli comma separated values
# writer = csv.writer(file, czym oddzielone, w czym maja byc umieszczone, sposob cytowania)
# writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# QUOTE_MINIMAL - tylko te fragmenty z przecinkiem beda w cudzyslowie reszta bez
# writer.writerow(naglowek) - definiowanie co bedzie w naglownku
# writer.writerow(co ma byc w pliku) - definiowanie co bedzie w pliku

# zeby dodac funkcje do klasy po za klasa nalezy zrobic:
# Klasa.nowa_nazwa_funckji = wczesniej_utworzona_funkcja
# w ten sposob dodajemy funkcje statyczne poniewaz dalej musimy recznie dodawac argumenty do funkcji
#


lab3()
