def zad1():
    jeden = int(input("Podaj numer: "))
    dwa = float(input("Podaj numer przecinkowy: "))
    total = jeden * dwa
    print("Wynik mnożenia to: ", total)

def zad2():
    numer = int(input("Podaj numer: "))
    potega = int(input("Do jakiej potegi: "))
    total = numer ** potega
    print(total)

def zad2_2():
    numer = int(input("Podaj numer: "))
    potega = int(input("Do jakiej potegi: "))
    total = pow(numer, potega)                      #tak jak w nawiasie jest to wbudowana funkcja potegowania
    print(total)

def zad3():
    import random
    rand = random.randint(0, 10)
    print(rand)

def zad4():
    jeden = int(input("Podaj numer: "))
    dwa = int(input("Podaj numer: "))
    total = jeden / dwa
    total2 = jeden // dwa                           #jeden z sposobow uzyskania liczby calkowitej z dzielenia
    print(total, "\n", total2)

def zad4_2():
    import math                                     #modul do dzialan matematycznych
    jeden = int(input("Podaj numer: "))
    dwa = int(input("Podaj numer: "))
    total = jeden / dwa
    total2 = math.floor(total)                      #podaje liczbe calkowita z dzielenia
    print(total, "\n", total2)

def zad5():
    a = 5                                           #sposoby zamiany wartosci zmiennych
    b = 7
    print("a = ", a, "b = ", b)
    temp = a
    a = b
    b = temp
    print("a = ", a, "b = ", b)
    a, b = b, a
    print("a = ", a, "b = ", b)

def zad6():
    a = int(input("Podaj liczbe: "))                #najwieksza liczba z dwoch
    b = int(input("Podaj liczbe: "))
    if a > b:
        print(a, "jest wieksze od ", b)
    else:
        print(b, "jest wieksze od ", a)
    #shortcut
    c = int(input("Podaj liczbe: "))
    d = int(input("Podaj liczbe: "))
    largest = max(c, d)
    print("Najwieksza liczba to: ", largest)

def zad7():
    a = int(input("Podaj liczbe: "))                #najwieksza liczba z trzech
    b = int(input("Podaj liczbe: "))
    c = int(input("Podaj liczbe: "))
    if b >= a and b >= c:
        print("Najwieksza liczba to: ", b)
    elif c >= a and c >= b:
        print("Najwieksza liczba to: ", c)
    else:
        print("Najwieksza liczba to: ", a)
    #shorcut
    d = int(input("Podaj liczbe: "))
    e = int(input("Podaj liczbe: "))
    f = int(input("Podaj liczbe: "))
    largest = max(d, e, f)
    print("Najwieksza liczba to: ", largest)

def zad8():
    numb = int(input("Ilosc liczb: "))              #dodawania liczb do listy, sumowanie oraz podawanie sredniej wartosci
    avg = []
    for i in range(0, numb):
        element = int(input("Podaj liczbe: "))
        avg.append(element)
    total = (sum(avg)) / numb
    print(total)

def zad9():
    numb = int(input("Ilosc liczb: "))              #dodawanie liczb do listy ktore sa podzielne przez 3 oraz 5
    divide = []
    a = 1
    while numb >= a:
        if a % 3 == 0 and a % 5 == 0:
            divide.append(a)
        a += 1

    for i in divide:
        print(i, end=" ")
    print("\n")

    numb2 = int(input("Ilosc liczb: "))             # druga metoda na to samo
    while numb2 > 0:
        if numb2 % 3 == 0 and numb2 % 5 == 0:
            print(numb2, end=" ")
        numb2 -= 1
    print("\n")

    def divisible(numb3):                            # trzecia metoda na to samo
        result = []
        for i in range(numb3):
            if i % 3 == 0 and i % 5 == 0:
                result.append(i)
        return result

    numb3 = int(input("Ilosc liczb: "))
    result = divisible(numb3)
    for i in result:
        print(i, end=" ")

def zad10():
    numb = int(input("Podaj liczbe dwucyfrowa: "))  #tylko suma liczb dwucyfrowych
    if numb > 0:
        a = numb // 10
        b = numb % 10
        total = a + b
        print("Suma tych dwoch licz w liczbie to: ", total, "\n")

    numb2 = int(input("Podaj dowolna liczbe: "))    #suma liczb w liczbie o dowolnej dlugosci
    sum = 0
    while numb2 > 0:
        last = numb2 % 10
        sum += last
        numb2 = numb2 // 10
    print("Suma liczb w liczbie to: ", sum, "\n")

    numb3 = input("Podaj dowolna liczbe: ")         #trzecia metoda na to samo
    sum2 = 0                                        #input to domyslnie str
    for char in numb3:                              #dlatego dziala tutaj petla for ktora przy liczbach w takiej postaci nie dziala
        sum2 += int(char)                           #"liczba" z numb3 jest zamieniana na liczbe i dodawana do sumy
    print("Suma liczb w liczbie to: ", sum2, "\n")

    numb4 = list(input("Podaj dowolna liczbe: "))   #czwarta metoda
    sum3 = 0                                        #funkcja list zamienia str automatycznie w liste oddzielajac kazdy str od siebie
    for i in numb4:                                 #to samo co wczesniej
        sum3 += int(i)
    print("Suma liczb w liczbie to: ", sum3, "\n")

def zad11():
    numb = list(input("Podaj liczby bez spacji: ")) #pierwsza metoda dodawania liczb w liscie (tylko liczby pojedyncze)
    sum = 0
    for i in numb:
        sum += int(i)
    print("Suma licz: ", sum)

    def sum(nums):                                  #druga metoda z recznym tworzeniem listy
        sum = 0
        for i in nums:
            sum += i
        return sum
    nums = [12,13,1,15,5,20,25]
    for i in nums:
        print(i, end=" ")
    total = sum(nums)
    print("\n", "Suma licz: ", total)

    nums2 = [12,13,1,15,5,20,25]                    #trzecia, najkrotsza metoda
    for i in nums:
        print(i, end=" ")
    total2 = sum(nums2)
    print("\n", "Suma licz: ", total2)

def zad12():
    nums = [12, 13, 1, 15, 5, 20, 25, 55]               #najwieksza liczba z listy
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    print("Najwieksza liczba to: ", largest)

    largest2 = max(nums)                             #druga metoda najkrotsza
    print("Najwieksza liczba to: ", largest2)

def zad13():
    numb = list(input("Podaj duza liczbe: "))       #pierwsza metoda nie do konca prawidlowa
    sum = 0                                         #podaje sume poteg poszczegolnych liczb
    for i in numb:
        sum += pow(int(i), 2)
    print("Suma poteg w liczbie to: ", sum)

    nums = int(input("Podaj liczbe: "))             #druga metoda prawidlowa podaje sume poteg od 0 do podanego zakresu
    sums = 0
    for i in range(nums + 1):
        sums = pow(i, 2)
    print("Suma potegowania z zaskresu 0 - ", nums, "wynosi: ", sums)

    def sum_of_square(n):                           #wzor na sume poteg w liczbie (nie wiem czy dobry)
        sums = n * (n + 1) * (2 * n + 1) / 6
        return sums
    number = int(input("Podaj liczbe: "))
    suma = sum_of_square(number)
    print("Suma potegowania z zaskresu 0 - ", number, "wynosi: ", suma)

def zad14():
    n = [41, 20, 11, 12, 5, 40, 9, 30, 22, 45]      #sposob na znalezienie drugiej najwiekszej liczby w liscie
    first = n[0]
    second = n[0]
    for i in range(1, len(n)):
        if n[i] > first:
            second = first
            first = n[i]
        elif n[i] > second:
            second = n[i]
    print("Druga najwieksza liczba w liscie to: ", second)

    n2 = [1, 20, 11, 12, 5, 42, 9, 30, 22, 45]      #druga, latwiejsza metoda
    n2.remove(max(n2))
    largest = max(n2)
    print("Druga najwieksza liczba w liscie to: ", largest)

    nums = [1, 20, 11, 12, 5, 42, 9, 30, 22, 45]    #trzecia metoda przy uzyciu funkcji sorted
    sorted_nums = sorted(nums)                      #liczby sa posortowane od najwiekszej do najmniejszej
    print(sorted_nums)                              #druga najwieksza liczba bedzie druga od konca
    print(sorted_nums[-2])                          #czyli na pozycji [-2] // odwrotne indeksowanie

def zad15():
    n = [1, 20, 11, 12, 5, 42, 9, 30, 22, 45]       #druga njamniejsza liczba w liscie
    n.remove(min(n))
    sec_min = min(n)
    print("Druga najmniejsza liczba w liscie to: ", sec_min)

    n2 = [15, 20, 11, 2, 5, 40, 9, 30, 22, 45]      #dluzsza metoda
    first = n2[0]                                   #nie dziala kiedy pierwszy element jest najmniejszy
    second = n2[0]
    for i in range(1, len(n2)):
        if n2[i] < first:
            second = first
            first = n2[i]
        elif n2[i] < second:
            second = n2[i]
    print("Druga najmniejsza liczba w liscie to: ", second)

    nums = [1, 20, 11, 12, 5, 42, 9, 30, 22, 45]    #druga najmniejsze jest na pozycji [1] w liscie
    sorted_nums = sorted(nums)
    print(sorted_nums)
    print(sorted_nums[1])

def zad16():
    def remove_duplicate(nums):                     #to na co nazwa wskazuje usuwanie duplikatow z podanego str
        rem = []
        for i in nums:
            if i not in rem:
                rem.append(i)
        return rem
    a = input("Napisz cos: ")
    no_duplicate = remove_duplicate(a)
    print(no_duplicate)

def zad17():
    lm = int(input("Podaj odleglosc w milach: "))
    km = lm * 1.609344
    print(lm, "mil to: ", km, "kilometrow")

def zad18():
    c = int(input("Podaj temperature w *C: "))
    f = int(c * 9 / 5 + 32)
    print(c, "*C to: ", f, "F")

def zad19():
    dec = int(input("Podaj liczbe: "))              #zamiana licz dziesietnych na binarne
    bin_list = []
    while dec > 0:
        dec_rem = dec % 2
        bin_list.append(dec_rem)
        dec //= 2
    bin_list.reverse()
    binary = " "
    for i in bin_list:
        binary += str(i)
    print(binary)

    def dec_to_binary(n):                           #druga metoda na to samo (metoda rekursywna)
        if n > 1:
            dec_to_binary(n // 2)
        print(n % 2, end=" ")
    num = int(input("Podaj liczbe: "))
    dec_to_binary(num)
    print(" ")

def zad20():
    loan = int(input("Podaj kwote pozyczki: "))
    per = int(input("Podaj oprocentowanie: "))
    time = int(input("Podaj na ile lat: "))
    odst = loan * (per / 100) * time
    print("Odsetki będa wynosic: ", odst)
    total = loan + odst
    print("Calkowita kwota do splacenia wynosi: ", total)

def zad21():
    loan = int(input("Podaj kwote pozyczki: "))
    per = int(input("Podaj oprocentowanie: "))
    time = int(input("Podaj na ile lat: "))
    A = loan *((1 + per / 100) ** time)             #wzor na calkowita kwote splaty pozyczki
    print(A)

def zad22():
    a = int(input("Podaj ilosc punktow: "))
    b = int(input("Podaj ilosc punktow: "))
    c = int(input("Podaj ilosc punktow: "))
    d = int(input("Podaj ilosc punktow: "))
    e = int(input("Podaj ilosc punktow: "))

    avg = (a + b + c + d + e) / 5

    if avg >= 90:
        print("Twoja ocena to 5!")
    elif avg >= 70:
        print("Twoja ocena to 4!")
    elif avg >= 50:
        print("Twoja ocena to 3!")
    elif avg >= 30:
        print("Twoja ocena to 2!")
    else:
        print("Twoja ocena to 1!")

def zad23():        #FUNKCJA ROUND DO SPRAWDZENIA W GOOGLE
    G = 6.673 * pow(10.0, -11.0)
    m1 = float(input("Masa pierwszego obiektu: "))
    m2 = float(input("Masa drugiegio obiektu: "))
    r = float(input("Dystans miedzy nimi: "))
    gravitional_force = G * m1 * m2 / pow(r, 2.0)                                                  #round to funkcja ktora sluzy do skrocenia duzych liczb przecinkowych
    print("Siła przyciagania miedzy dwoma obiektami wynosi: ", round(gravitional_force, 5), "N")   #liczba po przecinku oznacza ile liczb po przecinku chcemyu zobaczyc

def zad24():        #SPRAWDZIC WZOR NA POLE TROJKATA
    import math
    a = int(input("Dlugosc boku trojkata: "))
    b = int(input("Dlugosc boku trojkata: "))
    c = int(input("Dlugosc boku trojkata: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))               #math.sqrt - to modul odpowiadajacy za pierwiastkowanie
    print("Pole trojkata wynosi: ", round(area, 2))

def zad25():
    a = int(input("Podaj dowolna liczbe: "))                        #moja metoda nie do konca poprawna
    for i in range(2, a):
        if a % i == 0:
            print("Nie jest to liczba pierwsza!")
        else:
            print("Jest to liczba pierwsza!")

    print("\n Druga metoda!!!")

    def check_prime(numb):                                          #poprawna metoda
        for i in range(2, numb):
            if numb % i == 0:
                return False
        return True
    numb = int(input("Podaj dowolna liczbe: "))
    if check_prime(numb):
        print("Jest to liczba pierwsza!")
    else:
        print("Nie jest to liczba pierwsza!")

def zad26():
    def check_prime(numb):
        for i in range(2, numb):
            if numb % i == 0:
                return False
        return True

    def all_primes(numb):
        primes = []
        for i in range(2, numb + 1):
            if check_prime(i) is True:
                primes.append(i)
        return primes

    numb = int(input("Podaj dowolna liczbe: "))
    primes = all_primes(numb)
    print(primes)

    print("\nDruga metoda!! \n")

    a = int(input("Podaj dowolna liczbe: "))
    pierwsze = []
    for i in range(2, a + 1):
        if a % i == 0:
            continue
        else:
            pierwsze.append(i)
    print(pierwsze)

def zad27():
    factors = []                                                #szukanie liczb pierwszych ktore moga podzielic liczbe
    start = 2                                                   #poprawiona i lepiej dzialajace
    a = int(input("Podaj dowolna liczbe: "))                    #DO SPRAWDZENIA PRZEZ KOGOS KOMPETENTNEGO!!!
    while a > start:
        if a % start == 0:
            factors.append(start)
            a /= start
            start += 1
        else:
            start += 1
    print(factors)

    print("\nDruga metoda!! \n")

    def prime_factors(n):                                       #druga metoda
        factor = []                                             #posiada blad, przez ktory liczba 2 pojawia sie w liscie podwojnie
        divisor = 2
        while n > 2:
            if n % divisor == 0:
                factor.append(divisor)
                n /= divisor
            else:
                divisor += 1
        return factor

    num = int(input("Podaj dowolna liczbe: "))
    factor = prime_factors(num)
    print(factor)

def zad28():
    factors = []                                                #szukanie najmniejszej liczby pierwszej ktora moze podzielic liczbe
    start = 2
    a = int(input("Podaj dowolna liczbe: "))
    while a > start:
        if a % start == 0:
            factors.append(start)
            a /= start
            start += 1
        else:
            start += 1
    print(min(factors))

def zad29():
    string = "Hello World"                                      #odwrocenie kolejnosci str
    new_string = ""
    for i in string:
        new_string = i + new_string                             #kazdy element str jest dodawany przed poprzednim elementem
    print(new_string)

def zad30():
    def reverse_stack(str):                                     #odwracanie str za pomoca stackowania
        stack =[]
        for char in str:
            stack.append(char)
        rev = ''
        while len(stack) > 0:
            last = stack.pop()                                  #pop() - usuwa i zwraca ostatni element listy
            rev += last
        return rev

    string = input("Napisz cos: ")
    reverse = reverse_stack(string)
    print(reverse)

def zad31():
    user_str = input("Napisz cos: ")                        #slicing najlatwiejsza metoda
    reverse = user_str[::-1]
    print(reverse)

    def recursive(str):                                    #METODA REKURSYWNA DO POCZYTANIA W NECIE
        if len(str) == 0:
            return str
        else:
            return reverse(str[1:]) + str[0]
    string = input("Napisz cos: ")
    rev = recursive(string)
    print(rev)

def zad32():
    numb = input("Podaj liczbe: ")                          #odwrocenie liczby
    reverse = numb[::-1]
    print(int(reverse))

    print("\nDruga Metoda!!!\n")

    n = int(input("Podaj liczbe: "))
    rev = 0
    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    print(rev)

def zad33():
    user_str = input("Napisz cos: ")
    reverse = user_str[::-1]
    if user_str == reverse:
        print("Te slowo czyta sie tak samo w obu kierunkach")
    else:
        print("Te slowo nie czyta sie tak samo w obu kierunkach")

def zad34():
    def cube_pow(n):                                        #podnoszenie liczb do potegi 3 z podanego zakresu
        sums = 0
        for i in range(n + 1):
            sums = pow(i, 3)
        return sums
    n = int(input("Podaj liczbe: "))
    cube = cube_pow(n)
    print(cube)

def zad35():
    def armstrong(numb):                                    #sprawdzania czy suma poteg danej liczby do potegi dlugosci tej liczby jest taka sama co liczba
        sum = 0
        for i in numb:
            sum += pow(int(i), len(numb))
        return sum
    numb = input("Podaj liczbe: ")
    arm = armstrong(numb)
    if int(numb) == arm:
        print("Jest to armstrong number!")
    else:
        print("Nie jest to armstrong number!")

    print("\nDruga Metoda!\n")

    def check_armstrong(num):                               #druga metoda na to samo
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        return num == sum
    num = int(input("Podaj liczbe: "))
    if check_armstrong(num):
        print(num, "Jest to armstrong number!")
    else:
        print(num, "Nie jest to armstrong number!")

def zad36():                                                #najwiekszy wspolny dzielnik
    def gcd(x, y):
        smaller = min(x, y)                                 #nie moze on byc wiekszy od najmniejszej liczby dlatego mamy zmienna smaller
        gcd = 1
        for i in range(1, smaller + 1):                     #dzielimy obie liczby w zakresie od 1 do najmniejszej z dwoch liczb
            if x % i == 0 and y % i == 0:
                gcd = i                                     #jesli warunek jest spelniony zmienia sie gcd
        return gcd
    num1 = int(input("Podaj liczbe: "))
    num2 = int(input("Podaj liczbe: "))
    gcd = gcd(num1, num2)
    print("GCD ", num1, num2, " to ", gcd)

    print("\nDruga Metoda!\n")

    def gcd2(a, b):                                         #metoda rekursywna
        if b == 0:
            return a
        else:
            return gcd2(b, a % b)
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    GCD = gcd2(a, b)
    print(GCD)

    print("\nKolejna Metoda!\n")

    import math                                             #metoda z wykorzystaniem wbudowanej funkcji z modulu math
    c = int(input("Podaj liczbe: "))
    d = int(input("Podaj liczbe: "))
    gcd3 = math.gcd(c, d)
    print(gcd3)

#POCZYTAC O FUKCJI SET W NECIE!!!!!

def zad37():
    import random                                           #prosta gra w zgadywanie liczb
    print("Zgadnij liczbe od 1 do 10!")
    the_number = random.randint(1, 10)
    score = 0
    guess = " "
    while the_number != guess:
        guess = int(input("Podaj liczbe: "))
        print("Probuj dalej...")
        cont = input("Czy grasz dalej? y/n: ")
        if guess == the_number:
            score += 10
            print("Zgadles! Ta liczba to", the_number, "Koniec gry! Uzyskales ", score, "pkt")
        elif cont == "n":
            print("No to koniec")
            break

def zad38():
    player1 = input("Podaj r/p/s: ")                        #kamien, papier, nozyczki
    player2 = input("Podaj r/p/s: ")
    if player1 == player2:
        print("Remis!")
    elif player1 == "r":
        if player2 == "p":
            print("Wygrywa drugi gracz!")
        else:
            print("Wygrywa pierwszy gracz!")
    elif player1 == "p":
        if player2 == "s":
            print("Wygrywa drugi gracz!")
        else:
            print("Wygrywa pierwszy gracz!")
    elif player1 == "s":
        if player2 == "r":
            print("Wygrywa drugi gracz!")
        else:
            print("Wygrywa pierwszy gracz!")


def zad39():
    def cow_bulls(rand, numb):                                      #zgadywanie liczby z jedna proba i podanie wyniku
        cow = 0
        bulls = 0
        if rand[0] == numb[0]:
            bulls += 1
        elif rand[1] == numb[1]:
            bulls += 1
        elif rand[2] == numb[2]:
            bulls += 1
        elif rand[3] == numb[3]:
            bulls += 1

        for i in range(len(numb)):
            if numb[i] in rand:
                cow += 1
        return print("Cow = ", cow, "\nBulls = ", bulls)
    import random
    rand = str(random.randint(1000, 9999))
    numb = input("Podaj liczbe cztero cyfrowa: ")
    print(rand)
    print("Twoj wynik to: ")
    cow_bulls(rand, numb)


def zad40():
    def cow_bulls(rand, numb):                                  #zgadywanie liczby 4 cyfrowej z ograniczona iloscia prob
        cow = 0                                                 #nie wiem czy poprawne
        bulls = 0                                               #do sprawdzenia
        if rand[0] == numb[0]:
            bulls += 1
        elif rand[1] == numb[1]:
            bulls += 1
        elif rand[2] == numb[2]:
            bulls += 1
        elif rand[3] == numb[3]:
            bulls += 1

        for i in range(len(numb)):
            if numb[i] in rand:
                cow += 1
        return print("Cow = ", cow, "\nBulls = ", bulls)
    import random
    rand = str(random.randint(1000, 9999))
    tries = 7

    while tries >= 1:
        numb = input("Podaj liczbe cztero cyfrowa: ")
        if numb == rand:
            print("Wygrales!")
            print("Ta liczba to: ", rand)
        else:
            print("To jeszcze nie to! Probuj dalej!")
            cow_bulls(rand, numb)
            tries -= 1
    print("Koniec gry!")
    print("Ta liczba to: ", rand)


def zad41():
    def dodawanie(a, b):
        sum = a + b
        return sum
    def odejmowanie(a, b):
        wynik = a - b
        return wynik
    def mnozenie(a, b):
        subs = a * b
        return subs
    def dzielenie(a, b):
        divide = a / b
        return divide
    def modulo(a, b):
        mod = a % b
        return mod

    print("Kalkulator!")
    print("""Opcje do wyboru:
    1 - dodwanie
    2 - odejmowanie
    3 - mnozenie
    4 - dzielenie
    5 - modulo (reszta z dzielenia)""")

    a = int(input("Podaj pierwsza liczbe: "))
    b = int(input("Podaj druga liczbe: "))
    choice = int(input("Wybierz jedna z opcji: "))

    if choice == 1:
        sum = dodawanie(a, b)
        print("Wynik to: ", sum)
    elif choice == 2:
        wynik = odejmowanie(a, b)
        print("Wynik to: ", wynik)
    elif choice == 3:
        subs = mnozenie(a, b)
        print("Wynik to: ", subs)
    elif choice == 4:
        divide = dzielenie(a, b)
        print("Wynik to: ", divide)
    elif choice == 5:
        mod = modulo(a, b)
        print("Wynik to: ", mod)
    else:
        print("Blad!")

def zad42():
    import string                                                   #prosty generator hasel
    import random
    def password_gen(size):
        all_char = string.ascii_letters + string.digits + string.punctuation
        password = " "
        for char in range(size):
            rand_char = random.choice(all_char)
            password += rand_char
        return password
    size = int(input("Podaj dlugosc hasla: "))
    password = password_gen(size)
    print("Twoje nowe haslo to: ", password)

def zad43():
    import string                                                   #generator hasel z wymaganiami
    import random                                                   #sprawdzic inne mozliwosci w necie
    print("""Generator hasel:
    1 - litery, liczby i znaki specjalne
    2 - litery
    3 - liczby
    4 - znaki specjalne
    5 - litery i liczby
    6 - litery i znaki specjalne
    7 - liczby i znaki specjalne""")
    def password_gen(user, size):
        letters = string.ascii_letters
        digits = string.digits
        punc = string.punctuation
        password = " "
        for char in range(size):
            if user == 1:
                rand_char = random.choice(letters + digits + punc)
                password += rand_char
            elif user == 2:
                rand_char = random.choice(letters)
                password += rand_char
            elif user == 3:
                rand_char = random.choice(digits)
                password += rand_char
            elif user == 4:
                rand_char = random.choice(punc)
                password += rand_char
            elif user == 5:
                rand_char = random.choice(letters + digits)
                password += rand_char
            elif user == 6:
                rand_char = random.choice(letters + punc)
                password += rand_char
            elif user == 7:
                rand_char = random.choice(digits + punc)
                password += rand_char
            else:
                print("Blad!")
                return False
        return print("Twoje haslo to: ", password)
    user = int(input("Wybierz jedna z opcji: "))
    size = int(input("Dlugosc hasla: "))
    password_gen(user, size)

def zad44():
    import time                                         #prosty zegarek cyfrowy
    hour = int(input("Podaj godzine: "))
    minute = int(input("Podaj minuty: "))
    second = int(input("Podaj sekundy: "))

    def display():
        print(hour, ":", minute, ":", second)

    while True:
        time.sleep(1)
        second = second + 1
        if second == 60:
            minute += 1
            second = 0
        elif minute == 60:
            hour += 1
            minute = 0
        elif hour == 24:
            hour = 0
        display()

def zad45():
    from datetime import datetime
    import time
    def get_user_birthday():
        date_str = input("Twoja data urodzenia DD/MM/YYYY: ")
        try:
            birthday = datetime.strptime(date_str, "%d/%m/%Y")
        except TypeError:
            birthday = datetime.datetime(*(time.strptime(date_str, "%d/%m/%Y")[0 : 6]))
        return birthday

    def days_remaining(birth_date):
        now = datetime.now()
        current_year = datetime(now.year, birth_date.month, birth_date.day)
        days = (current_year - now).days
        if days < 0:
            next_year = datetime(now.year + 1, birth_date.month, birth.date.day)
            days = (next_year - now).days
        return days

    birthday = get_user_birthday()
    next_birthday = days_remaining(birthday)
    print("Twoje urodziny beda za ", next_birthday, "dni!")


def main():
    zad45()


main()