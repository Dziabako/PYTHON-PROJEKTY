def ex8():
    color_list = ["Red", "Green", "White", "Black"]
    print("First word from list:", color_list[0], " Last word from list:", color_list[3])

def ex9():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : %i / %i / %i" % exam_st_date)                  # %i / % exam_st_date - pierwsze znaczy ze chcemy podzielic liste, nastepnie jest czym ma byc podzielona na po % z ktorej listy

def ex10():
    integer = int(input("Give number: "))
    n1 = int("%s" % integer)                                # %s - sluzy do wklejania str z podanego ciagu po %
    n2 = int("%s%s" % (integer, integer))                   # kazdy %s dodaje pojedynczy str z ciagu
    n3 = int("%s%s%s" % (integer, integer, integer))        # kilka str w ciagu to kazdy potrzbuje %s
    print(n1+n2+n3)

def ex11():
    print(abs.__doc__)              # sprawdzic!!!!!!!!!!!!!!!!!!!!!!!!

def ex12():
    import calendar                                 # importuje modul kalendarza w formie str
    y = int(input("Input the year : "))             # podanie roku z kalendarza
    m = int(input("Input the month : "))            # miesiac z kalendarza
    print(calendar.month(y, m))                     # drukuje kalendarz w dormacie str dla argumentow y oraz m

def ex13():
    print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
    """)

def ex14():
    from datetime import date               # importowanie modulu date (standardowy kalendarz gregorianski) z datetime
    f_date = date(2014, 7, 2)               # date - konwertuje liste na date
    l_date = date(2014, 7, 11)
    d = l_date - f_date                     # standardowa roznica miedzy datami
    print(d.days)                           # .days = daje nam roznice dni między datami

def ex15():
    from math import pi
    radius = int(input("Radius of sphere: "))
    volume = 4/3*pi*radius**3
    print("Volume of sphere is equal to: ", volume)

def ex16():
    n = int(input("Number: "))
    if n <= 17:
        n = n - 17
        print("Difference: ", n)
    else:
        n = (n - 17)*2
        print("Difference: ", n)

def ex17():
    n = int(input("Number: "))
    if n < 100:
        print(n, "is less than 100")
    elif n >= 100 and n < 1000:
        print(n, "is between 100 and 1000")
    elif n >= 1000 and n < 2000:
        print(n, "is between 1000 and 2000")
    else:
        print(n, "is bigger than 2000")

def ex17_2():
    def near_thousand(n):
        return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))       # abs zwraca liczbe calkowita
    print(near_thousand(1000))                                          # jezeli abs jest mniejeszy lub rowny 100 to return = True
    print(near_thousand(900))                                           # w innym przypadku return = False
    print(near_thousand(800))
    print(near_thousand(2100))

def ex18():
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    n3 = int(input("Number 3: "))
    if n1 == n2 == n3:
        print((n1+n2+n3)*3)
    else:
        print(n1+n2+n3)

def ex19():
    str = input("Give word: ")
    if len(str) >= 2 and str[:2] != "Is":               # str[:2] oznacza drugi znak w ciagu podanego lancucha (pozycja 2 nie jest uwzgledniana)
        new_str = "Is" + str
        print(new_str)
    else:
        print(str)

def ex20():
    string = input("Give string: ")
    n = int(input("How many copies?: "))
    for i in range(n):
        print(string, end=" ")                          # end= - podaje ktory znak ma byc konczacy i rozpoczynac nowy ciag

def ex21():
    num = int(input("Enter a number: "))
    mod = num % 2                                       # % - wynikiem jest tylko i wylacznie reszta z dzielenia danych liczb
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")

def ex22():
    insert = input("Number: ")
    lista = insert.split(",")                           # tworzy liste str z podanych elementow oddzielonych ","
    count = 0
    for i in lista:
        if i == "4":
            count += 1
    print("There is ", count, " 4's")

def ex23():
    string = input("Give string: ")
    n = int(input("Number of copies: "))
    if len(string) < 2:
        print(string*n)
    else:
        print(string[:2]*n)

def ex24():
    VOwELS = "aeiouy"
    letter = input("Give letter: ")
    if letter in VOwELS:
        print("Given letter is a vowel")
    else:
        print("Given letter is not a vowel")

def ex25():
    GROUP = [1, 5, 8, 3]
    print(GROUP)
    n = int(input("Give number: "))
    if n in GROUP:
        print("True")
    else:
        print("False")

def ex26():
    numberList = []
    n = int(input("Enter the list size : "))            # tworzenie listy z liczbami naturalnymi zaczynajac od pustej listy
    print("Give numbers: ")
    for i in range(0, n):
        item = int(input())
        numberList.append(item)
    print("User List is ", numberList)
    def histogram(numberList):
        for n in numberList:                            # pierwszy element list
            output = ''                                 # zamiana na pusty element listy
            times = n                                   # ilość n taka sama jak wartość liczby w liście
            while (times > 0):                          # wykonuje się dopoki times jest wieksze od 0
                output += '*'                           # przy każdym wykonaniu puste pole zamieniane jest przez "*"
                times = times - 1                       # odejmowana jest wartość times az bedzie 0
            print(output)                               # zwracane są "*" w ilosci zaleznej od liczby w liście i pętla zaczyna sie wykonywać od nowa
    print("Histogram: ")
    histogram(numberList)

def ex27():
    insert = input("Give numbers: ")
    lista = insert.split(",")
    print("Your list: ", lista)
    print("Your list after concatenation:")              # concatenate - połączyc w jedna liste
    separator = ""                                      # separator w nowej liscie czyli brak spacji i przcinka
    for i in lista:                                     # przechodzenie po  kazdym elemencie listy
        separator += str(i)                             # dodawanie do separatora kazdego elementu listy przez co jest ona łączona w jedno
    print(separator)

def ex28():
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]
    for i in numbers:
        if i % 2 == 0:
            print(i)
        elif i == 237:
            print(i)
            break

def ex29():
    color_list_1 = ["White", "Black", "Red"]
    color_list_2 = ["Red", "Green"]
    for i in color_list_1:
        if i not in color_list_2:
            print(i, end=" ")

def ex29_2():
    color_list_1 = set(["White", "Black", "Red"])               # set - tworzy zbior niemutowalnych obiektow ktore auomatycznie sa iterowane
    color_list_2 = set(["Red", "Green"])

    print(color_list_1.difference(color_list_2))                # automatycznie iteruje przez color_list_1 tylko ze sprawdza roznice miedzy druga lista i drukuje tylko roznice

def ex30():
    a = int(input("Base: "))
    h = int(input("Height: "))
    area = 0.5*a*h
    print("Triangle area is equal to: ", area)

def ex31():
    gcd = 1
    x = int(input("First number: "))
    y = int(input("Second number: "))
    

def exercises():
    ex30()

exercises()