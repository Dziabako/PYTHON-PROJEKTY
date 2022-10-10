def zad1():
    a = int(input("Podaj liczbe: "))
    b = float(input("Podaj liczbe przecinkowa: "))
    total = a * b
    print(total)

def zad2():
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj potege: "))
    result = a ** b
    print(result)

    print("\nDruga Metoda!\n")

    c = int(input("Podaj liczbe: "))
    d = int(input("Podaj potege: "))
    total = pow(c, d)
    print(total)

def zad3():
    import random
    rand = random.randint(0, 10)
    rand2 = random.randrange(11)
    print(rand)
    print(rand2)

def zad4():
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    import math
    total1 = a // b
    print(total1)
    print("\nDruga Metoda!\n")
    total2 = math.floor(a / b)
    print(total2)

def zad5():
    a = 5
    b = 4
    print("a = ", a)
    print("b = ", b)
    print("\nPierwsza metoda\n")
    temp = a
    a = b
    b = temp
    print("a = ", a)
    print("b = ", b)
    print("\nDruga metoda\n")
    a, b = b, a
    print("a = ", a, "b = ", b)

def zad6():
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    if a > b:
        print(a, "jest wieksze")
    else:
        print(b, "jest wieksze")
    print("\nDruga metoda\n")
    total = max(a, b)
    print("Wieksza liczba to: ", total)

def zad7():
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    c = int(input("Podaj liczbe: "))
    largest = a
    if b >= a and b >= c:
        largest = b
        print("Najwieksza liczba to: ", largest)
    elif c >= a and c >= b:
        largest = c
        print("Najwieksza liczba to: ", largest)
    else:
        print("Najwieksza liczba to: ", largest)

    print("\nDruga metoda!\n")

    big = max(a, b, c)
    print("Najwieksza liczba to: ", big)


def zad8():
    lenght = int(input("Ile liczb: "))
    suma = []
    for i in range(lenght):
        i = int(input("Podaj liczbe: "))
        suma.append(i)

    for i in suma:
        print(i, end=" ")

    total = (sum(suma)/lenght)
    print("\nSrednia z liczb to: ", total)

    print("\nDruga Metoda\n")
    tot = 0
    for i in range(lenght):
        i = int(input("Podaj liczbe:"))
        tot += i
    avg = tot/lenght
    print("Srednia z liczb to: ", avg)

def zad9():
    lenght = int(input("Podaj liczbe: "))
    divide = []
    for i in range(1, lenght):
        if i % 3 == 0 and i % 5 == 0:
            divide.append(i)
    print("Liczby podzielne przez 3 i 5 z podanego zakresu to: ")
    for i in divide:
        print(i, end=" ")

    print("\nKolejna metoda\n")

    lenght2 = int(input("Podaj liczbe: "))
    while lenght2 > 0:
        if lenght2 % 3 == 0 and lenght2 % 5 == 0:
            print(lenght2, end=" ")
        lenght2 -= 1

    print("\nKolejna metoda\n")
    lenght3 = int(input("Podaj liczbe: "))
    count = 1
    div = []
    while lenght3 > count:
        if count % 3 == 0 and count % 5 == 0:
            div.append(count)
        count += 1
    print(div)

def zad10():
    def sum_of_digits(num):
        sum = []
        while num > 0:
            last = num % 10
            sum.append(last)
            num = num // 10
        return sum
    num = int(input("Podaj liczbe: "))
    suma = sum(sum_of_digits(num))
    print("Suma liczb w liczbie to: ", suma)

    print("\nKolejna metoda\n")

    def get_sum(numb):
        sum = 0
        while numb > 0:
            last = numb % 10
            sum += last
            numb = numb // 10
        return sum
    numb = int(input("Podaj liczbe: "))
    suma2 = get_sum(numb)
    print("Suma liczb w liczbie to: ", suma2)

    print("\nKolejna metoda\n")

    numbe = input("Podaj liczbe: ")
    sume = 0
    for i in numbe:
        sume += int(i)
    print("Suma liczb w liczbie to: ", sume)

    print("\nKolejna metoda\n")
    digits = list(input("Podaj liczbe: "))
    sumi = 0
    for i in digits:
        sumi += int(i)
    print("Suma liczb w liczbie to: ", sumi)

def zad11():
    nums = [15, 12, 1, 4, 5, 12, 11]
    suma = 0
    for i in nums:
        suma += i
    print("Suma: ", suma)

    print("\nKolejna metoda\n")

    total = sum(nums)
    print("Suma: ", total)

def zad12():
    nums = [15, 17, 1, 4, 5, 12, 11]
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    print("Najwieksza liczba to: ", largest)

    print("\nKolejna metoda\n")

    large = max(nums)
    print("Najwieksza liczba to: ", large)

def zad13():
    num = int(input("Podaj liczbe: "))
    sum = 0
    for i in range(num + 1):
        i = pow(i, 2)
        sum += i
    print("Suma poteg w podanym zakresie wynosi: ", sum)

    print("\nKolejna metoda nieprawidlowa\n")

    number = input("Podaj liczbe: ")
    suma = 0
    for i in number:
        i = int(i)
        suma = suma + pow(i, 2)
    print("Suma poteg liczb wynosi: ", suma)

    print("\nKolejna metoda z uzyciem wzoru\n")

    nums = int(input("Podaj zakres: "))
    sums = nums * (nums + 1) * (2 * nums + 1) / 6
    print("Suma poteg wynosi: ", sums)

def zad14():
    nums = [15, 12, 18, 4, 5, 17, 11]
    first = nums[0]
    second = nums[0]
    for i in nums:
        if i > first:
            first = i
        if i < first and i > second:
            second = i

    print("Pierwsza: ", first)
    print("Druga", second)

    print("\nKolejna metoda\n")

    for i in range(1, len(nums)):
        if nums[i] > first:
            first = nums[i]
        elif nums[i] < first and nums[i] > second:
            second = nums[i]
    print("Pierwsza: ", first)
    print("Druga", second)

    print("\nKolejna Metoda\n")

    nums.remove(max(nums))
    max2 = max(nums)
    print("Druga: ", max2)

    print("\nKolejna Metoda\n")

    nums = sorted(nums)                                 #18 z listy jest tutaj usuniete w poprzedniej metodzie
    maxi2 = nums[-2]
    print("Druga: ", maxi2)

def zad15():
    nums = [15, 12, 18, 4, 5, 17, 11]
    first = nums[0]
    second = nums[0]
    for i in nums:
        if i < first:
            first = i
        elif i > first and i < second:
            second = i
    print("Pierwsza: ", first)
    print("Druga: ", second)

    print("\nKolejna metoda\n")

    for i in range(1, len(nums)):
        if nums[i] < first:
            first = nums[i]
        elif nums[i] > first and nums[i] < second:
            second = nums[i]
    print("Pierwsza: ", first)
    print("Druga", second)

    print("\nKolejna Metoda\n")

    nums.remove(min(nums))
    min2 = min(nums)
    print("Druga: ", min2)

    print("\nKolejna Metoda\n")

    nums = sorted(nums)                                 #5 jest usuniete w poprzedniej metodzie
    mini2 = nums[1]
    print("Druga: ", mini2)

def zad16():
    def remove(string):
        stri = " "
        for i in string:
            if i not in stri:
                stri += i
        return stri
    string = input("Napisz cos: ")
    stri = remove(string)
    print("Bez powtorzen: ", stri)

def zad17():
    mile = float(input("Ile mil: "))
    km = mile * 1.609344
    print("Mile na kilometry to: ", km)

def zad18():
    celsius = int(input("Podaj ilosc stopni: "))        #funkcja "round" umozliwia ustaelenie ile liczb po przecinku bedzie = round(wynik, ilosc liczb po przecinku)
    fahr = ((celsius * 9) / 5) + 32
    print("fahrenheit: ", fahr)

def zad19():
    num = int(input("Podaj liczbe: "))
    bin_list = []
    binary = " "
    while num > 0:
        last = num % 2
        bin_list.append(last)
        num //= 2
    for i in bin_list:
        binary += str(i)
    print(binary)
    binary = binary[::-1]                               #mozna tez wczesniej odwrocic liste za pomoca "bin_list.reverse()"
    print("Podana liczba w formacie binarnym to: ", binary)

    print("\nKolejna metoda - rekursywna(skrocona)\n")

    def dec_to_bin(n):
        if n > 1:
            dec_to_bin(n // 2)
        print(n % 2, end=" ")                           #tym sposobem kazda reszta z dzielenia jest wstawiana na poczatek dlatego nie trzeba jej odwracac
    numb = int(input("Podaj liczbe: "))
    dec_to_bin(numb)

    print("\nKolejna metoda\n")
    bn = int(input("Podaj liczba: "))
    bn = bin(bn)
    print(bn)

def zad19_2():
    bin_num = list(input("Podaj liczbe binarna: "))     #zamiana liczby binarnej na dziesietna
    bin_num.reverse()
    dec = 0
    pot = 0
    for i in bin_num:
        i = int(i) * pow(2, pot)
        pot += 1
        dec += i
    print("W systemie dziesietnym to: ", dec)

    bin_number = input("Podaj liczbe binarna: ")
    dec_num = int(bin_number, 2)                        #funkcja int zamienia liczby z roznych systemow na dziesietne
    print(dec_num)                                      #2 to podstawa na podstawie ktorej jest zamieniana liczba (binarna(2), osemkowa(8), itd)

def zad20():
    proc = 0.02
    czas = 2
    kwota = 50000
    total = proc * czas * kwota
    print("Odsetki: ", total)

def zad21():
    proc = 10
    czas = 12
    kwota = 5000
    a = kwota * ((1 + proc / 100) ** czas)
    print("Rzeczywista kwota splaty porzyczki: ", round(a, 2))

def zad22():
    a = int(input("Podaj ilosc pkt: "))
    b = int(input("Podaj ilosc pkt: "))
    c = int(input("Podaj ilosc pkt: "))
    d = int(input("Podaj ilosc pkt: "))
    e = int(input("Podaj ilosc pkt: "))
    avg = (a + b + c + d +e) / 5
    if avg < 20:
        print("Ocena: 1")
    elif avg >= 20 and avg < 40:
        print("Ocena: 2")
    elif avg >= 40 and avg < 70:
        print("Ocena: 3")
    elif avg >= 70 and avg < 90:
        print("Ocena: 4")
    elif avg >= 90 and avg < 100:
        print("Ocena: 5")
    elif avg == 100:
        print("Ocena: 6")

def zad23():
    G = 6.673 * (10 ** (-11))
    m1 = int(input("m1: "))
    m2 = int(input("m2: "))
    r = int(input("r: "))
    F = (G * m1 * m2) / r ** 2
    print("F = ", round(F, 4))

def zad24():
    a = int(input("Podaj liczbe: "))
    #obliczanie pola trojkata

def zad25():
    def check_prime(numb):
        for i in range(2, numb):                                    #tutaj jest zwracany wynik tylko raz poniewaz znajduje sie to w funkcji
            if numb % i == 0:
                return print("Nie jest to liczba pierwsza")
            else:
                return print("Jest to liczba pierwsza")

    numb = int(input("Podaj liczbe: "))
    check_prime(numb)

    print("\nDruga metoda nieprawidlowa\n")

    num = int(input("Podaj liczbe: "))
    for i in range(2, num):                                         #tutaj sie bedzie powtarzac poniewaz jest to poza utworzona fukncja
        if num % i == 0:                                            #dlatego kazde powtorzenie linijki kodu sie powtarza
            print("Nie jest to liczba pierwsza")
        else:
            print("Jest to liczba pierwsza")

    print("\nKolejna metoda z 'Programming Hero'\n")

    def prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False                                        #jezeli liczba dzieli sie przez i to zwracane jest FALSE
        return True                                                 #jezeli nie dzieli sie przez i to zwracane jest TRUE
    n = int(input("Podaj liczbe: "))
    p = prime(n)
    if p:
        print("Jest to liczba pierwsza")
    else:
        print("Nie jest to liczba pierwsza")

def zad26():
    def prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def all_prime(n):                                               #przy podaniu liczby ktora nie jest liczba pierwsza zwraca pusta liste
        primes = []
        for i in range(2, n + 1):
            if prime(n) is True:
                primes.append(i)
        return primes

    n = int(input("Podaj liczbe: "))
    primes = all_prime(n)
    print(primes)

    print("\nKolejna metoda - wlasna\n")
    num = int(input("Podaj liczbe: "))
    prime = []
    for i in range(2, num):
        if num % i == 0:
            continue
        else:
            prime.append(i)
    print(prime)

def zad27():
    num = int(input("Podaj liczbe: "))
    start = 2
    factors = []
    while num > 2:
        if num % start == 0:
            factors.append(start)
            num /= start
            start += 1
        else:
            start += 1
    print(factors)

    print("\nKolejna Metoda\n")

    def prime_factors(num):
        factors = []
        divider = 2
        while num > 2:
            if num % divider == 0:
                factors.append(divider)
                num /= divider
            else:
                divider += 1
        return factors
    n = int(input("Podaj liczbe: "))
    p = prime_factors(n)
    print(p)


def zad28():
    string = "Hello World!"
    print(string)
    string = string[::-1]
    print(string)

    print("\nKolejna metoda\n")

    strip = "Hello World!"
    print(strip)
    reverse = " "
    for char in strip:
        reverse = char + reverse                            #w ten sposob kazda kolejna litera z lancucha wskakuje na poczatek
    print(reverse)                                          #mozna to umiescic tez w funkcji

def zad29():
    string = list(input("Napisz cos: "))                    #odwracania za pomoca stackowania
    reverse = " "                                           #string zamienianiy jest na liste po czy zabierany jest osotatni element przez .pop()
    while len(string) > 0:                                  #na koniec kazdy koncowy element dodawany jest do nowego lancucha
        rev = string.pop()
        reverse += rev
    print(reverse)

def zad30():
    def reverse_recur(string):                              #metoda rekursywna (DO OGARNIECIA)
        if len(string) == 0:
            return string
        else:
            return reverse_recur(string[1:]) + string[0]
    string = input("Napisz cos: ")
    rev_str = reverse_recur(string)
    print(rev_str)

def zad31():
    num = int(input("Podaj liczbe: "))
    rev = 0
    while num > 0:
        last = num % 10
        rev += last                                         #blad polega tutaj na tym, ze ostatnia licz jest najpierw dodawana a potem mnozona przez 10 co daje 0 na koncu
        rev = rev * 10
        num //= 10
    print(rev)

    print("\nDruga Metoda\n")

    num = int(input("Podaj liczbe: "))
    rev = 0
    while num > 0:
        last = num % 10
        rev = rev * 10 + last                               #tutaj liczba odwrocona najpierw jest mnozona przez 10 a potem dodawany jest ostatni element do odwroconej liczby
        num //= 10
    print(rev)

def zad31_2():
    sent = input("Napisz zdanie: ")
    words = sent.split()                                    #.split() dzieli lancuch w domysle jest spacja i tworzy liste
    print(words)
    rev = reversed(words)                                   #reversed odwraca kolejnosc listy, dziala tak samo jak .reverse
    print(" ".join(rev))                                    #.join laczy liste w jeden lancuch uzywajac elementu podanego przed

    print("\nKolejna metoda\n")

    s = input("Napisz zdanie: ")
    rever = reversed(s)                                     #nie dziala jesli to jest lancuch
    print(rever)

#SPRAWDZIC ROZNICE MIEDZY reversed() ORAZ .reverse()

def roznice_miedzy_metodami():
    lista = ["Hello", "World"]
    rev = lista.reverse()                                   #ta metoda nie mozna wrzucic w petle, zwraca obiekt z ktorym nie mozna nic praktycznie zrobic
    print(rev)                                              #mozna uzyc potem tej listy w petli ale nie mozna jej wyswietlic

    reve = reversed(lista)                                  #tutaj mozna wrzucic w petle zeby ja wyswietlic
    for i in reve:                                          #jest wiekszy dostep do listy po odwroceniu
        print(i, end=" ")

def zad32():
    def check_palidrome(string):                            #mozna to zrobic bez uzywania fukncji
        if string.lower() == string[::-1].lower():
            return True
        else:
            return False
    string = input("Napisz cos: ")
    if check_palidrome(string):
        print("Jest to palidroma")
    else:
        print("Nie jest to palidroma")

def zad33():
    num = int(input("Podaj liczbe: "))
    sum = 0
    for i in range(1, num + 1):
        i = i ** 3
        sum += i
    print("Suma szescianow: ", sum)

    print("\nKolejna Metoda - wzor\n")
    n = int(input("Podaj liczbe: "))
    c = (n * (n + 1) / 2) ** 2
    print("Suma szescianow: ", c)

def zad34():
    def check_arm(num):
        n = list(num)
        p = len(n)
        sum = 0
        for i in n:
            i = int(i) ** p
            sum += i
        if sum == int(num):
            return True
        else:
            return False
    num = input("Podaj liczbe: ")
    if check_arm(num):
        print("Jest to Armstrong number!")
    else:
        print("Nope!")

    print("\nMetoda z PROGRAMMING HERO\n")

    def armstrong(n):
        order = len(str(num))
        sum = 0
        temp = n
        while temp > 0:                                     #temp jest uzywane to wydzielenia jazdej liczby i podniesienia jej do potegi
            digit = temp % 10
            sum += digit ** order
            temp //= 10                                     #to skraca liczba o ostatnia cyfre z temp
        return sum == n

    n = int(input("Podaj liczbe: "))
    if armstrong(n):
        print("Jest to Armstrong number!")
    else:
        print("Nope!")

def zad35():
    def gcd(num1, num2):
        lowest = num1
        gcd = 0
        if num1 > num2:                                     #zamiast tego mozna bylo po prostu uzyc min(x, y)
            lowest = num2
        for i in range(1, lowest + 1):
            if num1 % i == 0 and num2 % i == 0:
                gcd = i
        return gcd

    num1 = int(input("Podaj liczbe: "))
    num2 = int(input("Podaj liczbe: "))
    g = gcd(num1, num2)
    print("GCD = ", g)

    print("\nKolejna metoda rekursywna\n")
    def GCD(a, b):
        if b == 0:
            return a
        else:
            return GCD(b, a % b)
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    gc = GCD(a, b)
    print("GCD = ", gc)

    print("\nKolejna metoda - wbudowany modul\n")
    import math
    x = int(input("Podaj liczbe: "))
    y = int(input("Podaj liczbe: "))
    z = math.gcd(x, y)
    print("GCD = ", z)
        
def zad35_2():
    def lcm(num1, num2):                                                #najmniejsza wspolna wielokrotnosc
        largest = max(num1, num2)                                       #ta metoda zuzywa duzo pamieci komputera
        while True:                                                     #LCM nie moze byc mniejszy niz wieksza liczba z dwoch
            if largest % num1 == 0 and largest % num2 == 0:             #w tej petli za kazdym razem sprawdzay czy wieksza liczba jest podzielna przez podane liczby
                lcm = largest                                           #w momencie kiedy jest podzielne jest petla jest przerywana i ta liczba jest przypisywana do lcm
                break
            else:
                largest += 1
        return lcm
    num1 = int(input("Podaj liczbe: "))
    num2 = int(input("Podaj liczbe: "))
    l = lcm(num1, num2)
    print("LCM = ", l)

    print("\nKolejna metoda\n")

    import math
    x = int(input("Podaj liczbe: "))                                    #uzyty wzor X * Y = LCM * GCD
    y = int(input("Podaj liczbe: "))                                    #wynik mnozenia dwoch liczb jest rowny wynikowi mnozenia lcm i gcd tych liczb
    gcd = math.gcd(x, y)
    lcm1 = (x * y) // gcd                                               #tak wyglada wzor po przeksztalceniu
    print("LCM = ", lcm1)

def zad36():
    import random                                                       #gra w zgadywanie
    number = random.randint(1, 10)
    points = 0
    tries = 0
    guess = int(input("Zgadnij liczbe od 0 do 10: "))
    while guess != number:                                              #dziala tak dlugo az liczba nie zostanie zgadnieta
        guess = int(input("To nie to, zgaduj dalej: "))
        tries += 1
    else:
        points += 10
        print("Gratulacje zgadles! Ta liczba to ", number, "Uzyskales: ", points, "punktow!")

    print("\nKolejna metoda z jedna proba\n")

    n = random.randint(0, 10)
    p = 0
    print("Zeby przerwac wcisnij 'q'")
    g = input("Zgaduj: ")
    while True:
        if g == "q":
            print("Koniec")
            break
        elif int(g) == n:
            print("Zgadles!")
            p += 10
            print("Twoj wynik to: ", p)
            break
        else:
            print("ZLE, ta liczba to: ", n)
            break

def zad37():
    print("Kamien / papier / nozyczki = r / p / s")
    p1 = input("Co rzucasz?: ")
    p2 = input("Co rzucasz?: ")
    if p1 == p2:
        print("Remis!")
    elif p1 == "r":
        if p2 == "s":
            print("Wygrywa gracz 1")
        else:
            print("Wygrywa gracz 2")
    elif p1 == "p":
        if p2 == "r":
            print("Wygrywa gracz 1")
        else:
            print("Wygrywa gracz 2")
    elif p1 == "s":
        if p2 == "p":
            print("Wygrywa gracz 1")
        else:
            print("Wygrywa gracz 2")

def zad38():                                                            #zaden z tych kodow nie dziala poprawnie
    def cow_bulls_2(num, rand):
        cows = 0
        bulls = 0
        if num[0] == rand[0]:
            bulls += 1
        elif num[1] == rand[1]:
            bulls += 1
        for i in range(0, 10):
            if str(i) in list(rand):
                cows += 1
        return cows, bulls
    import random
    rand = str(random.randint(10, 99))
    print(rand)
    num = input("Podaj liczbe dwucyfrowa: ")
    cows, bulls = cow_bulls_2(num, rand)
    print("Twoj wynik to COWS: ", cows, "BULLS: ", bulls)

    print("\nKolejna metoda - porzednio zrobiona\n")

    def cow_bulls(rand, numb):
        cow = 0
        bulls = 0
        if rand[0] == numb[0]:
            bulls += 1
        elif rand[1] == numb[1]:
            bulls += 1

        for i in range(len(numb)):
            if numb[i] in rand:
                cow += 1
        return print("Cow = ", cow, "\nBulls = ", bulls)
    import random
    ran = str(random.randint(10, 99))
    print(ran)
    num = input("Podaj liczbe dwu cyfrowa: ")
    print("Twoj wynik to: ")
    cow_bulls(ran, num)

    print("\nKolejna metoda\n")

    r = str(random.randint(10, 99))
    print(r)
    n = input("Podaj liczbe dwu cyfrowa: ")
    c = 0
    b = 0
    if n == r:
        print("Wygrales, ta liczba to, ", r, "\nBULLS = ", b, "\nCOWS = ", c)
    elif n[0] == r[0]:
        b += 1
    elif n[1] == r[1]:
        b += 1
    elif n[0] == r[1]:
        c += 1
    elif n[1] == r[0]:
        c += 1
    print("Cow = ", c, "\nBulls = ", b)

def zad39():
    import random                                                               #ciulowy pomysl DO POPRAWY
    bulls = 0                                                                   #lub nie bo nie warto zachodu - ZA DLUGI KOD
    cows = 0
    rand = str(random.randint(1000, 9999))
    print(rand)
    tries = 7
    while tries >= 1:
        num = input("Podaj liczbe 4 cyfrowa: ")
        print(rand)
        if num == rand:
            print("Wygrales!")
            break
        elif num[0] == rand[0]:
            bulls += 1
        elif num[1] == rand[1]:
            bulls += 1
        elif num[2] == rand[2]:
            bulls += 1
        elif num[3] == rand[3]:
            bulls += 1
        elif num[0] == rand[1] or num[0] == rand[2] or num[0] == rand[3]:
            cows += 1
        elif num[1] == rand[0] or num[1] == rand[2] or num[1] == rand[3]:
            cows += 1
        elif num[2] == rand[1] or num[2] == rand[0] or num[2] == rand[3]:
            cows += 1
        elif num[3] == rand[1] or num[3] == rand[2] or num[3] == rand[0]:
            cows += 1
        tries -= 1
        print("Cow = ", cows, "\nBulls = ", bulls)

    print("\nKolejna metoda - nie wlasna\n")

    def cow_bulls(n, r):                                                        #to dziala tak jak powinno
        cow = 0
        bull = 0
        for i in range(len(n)):
            if n[i] == r[i]:
                bull += 1
            elif n[i] in r:
                cow += 1
        return print("BULLS = ", bull, "\nCOWS = ", cow)
    t = 7
    r = str(random.randint(1000, 9999))
    print(r)
    while t >= 1:
        n = input("Podaj liczbe: ")
        if n == r:
            print("Wygrales!")
            break
        else:
            cow_bulls(n, r)
        t -= 1

def word_guessing():
    import random
    WORDS = ["python", "cola", "elemele", "ulumulu", 'laminator']
    tries = 10
    slowo = random.choice(WORDS)
    litery = len(slowo)
    print("Jesli chcesz podpowiedz wcisnij 'H'")
    while tries > 0:
        print("Tajemnicze slowo sklada sie z ", litery, "liter")
        guess = input("Zgadnij słowo: ")
        if guess == slowo:
            print("Wygrałeś to jest to!")
            break
        elif guess != slowo:
            hint = input("Czy chcesz podpowiedz? H/N")
            if hint == "H":
                if slowo == "python":
                    print("Pierwsza litera to 'p' a ostatnia to 'n'")
                elif slowo == "cola":
                    print("Pierwsza litera to 'c' a ostatnia to 'a'")
                elif slowo == "elemele":
                    print("Pierwsza litera to 'e' a ostatnia to 'e'")
                elif slowo == "ulumulu":
                    print("Pierwsza litera to 'u' a ostatnia to 'u'")
                elif slowo == "laminator":
                    print("Pierwsza litera to 'l' a ostatnia to 'r'")
            elif hint == "N":
                print("To nie to, graj dalej!")
                print("Pozostalo ci prob: ", tries)
        tries -= 1

def zad40():
    def dodawanie(a, b):
        sum = a + b
        return sum
    def odejmowanie(a, b):
        sum = a - b
        return sum
    def mnozenie(a, b):
        sum = a * b
        return sum
    def dzielenie(a, b):
        sum = a / b
        return sum
    def reszta(a, b):
        sum = a % b
        return sum
    choice = " "

    while choice != 6:
        print("""KALKULATOR
            1 - dodawanie
            2 - odejmowanie
            3 - mnozenie
            4 - dzielenie
            5 - reszta z dzielenia
            6 - koniec""")
        choice = int(input("Co wybierasz?: "))
        if choice == 1:
            a = int(input("Podaj liczbe: "))
            b = int(input("Podaj liczbe: "))
            sum = dodawanie(a ,b)
            print(sum)
        elif choice == 2:
            a = int(input("Podaj liczbe: "))
            b = int(input("Podaj liczbe: "))
            sum = odejmowanie(a, b)
            print(sum)
        elif choice == 3:
            a = int(input("Podaj liczbe: "))
            b = int(input("Podaj liczbe: "))
            sum = mnozenie(a, b)
            print(sum)
        elif choice == 4:
            a = int(input("Podaj liczbe: "))
            b = int(input("Podaj liczbe: "))
            sum = dzielenie(a, b)
            print(sum)
        elif choice == 5:
            a = int(input("Podaj liczbe: "))
            b = int(input("Podaj liczbe: "))
            sum = reszta(a, b)
            print(sum)
        elif choice == 6:
            print("Koniec")
            break

def zad41():
    import string
    import random
    all_letters = string.ascii_letters
    all_num = string.digits
    all_punc = string.punctuation
    lenght = int(input("Podaj dlugosc hasla: "))
    haslo = " "
    for i in range(lenght):
        rand_mark = random.choice(all_letters + all_num + all_punc)
        haslo += rand_mark
    print("Twoje haslo to: ", haslo)

def zad42():
    #permutacje i kombinacje
    from itertools import permutations, combinations, combinations_with_replacement
    lista = [1, 2, 3]
    lista2 = [2, 1, 3]
    perm = permutations(lista)                                                  #tworzy wszystkie mozliwe permutacje(mieszaniny) elementow z listy w postaci osobnych krotek w liscie (tuple)
    print("Permutacje zwykle")                                                  #dokladniej to w licie z 3 elementami tworzy 3! permutacji itd
    print(perm, "to sie tworzy po zwyklym wywolaniu bez petli")                 #PERMUTACJE SIE NIE POWTARZAJA
    for i in perm:                                                              #nie mozna tego wyswietlic od razu po przypisaniu do zmiennej wiec nalezy ja wrzucic w petle by ja wyswietlic
        print(i, end=" ")
    print("\nPermutacje, ale o okreslonej ilosci elementow z listy\n")
    perm2 = permutations(lista, 4)                                              #2 to liczba elementow w jednej kombinacji, przy podaniu wiekszej liczby niz liczba elementow listy permutacja nie wykonuje sie
    for i in perm2:
        print(i, end=" ")

    print("\nKombinacje\n")

    comb = combinations(lista, 2)                                               #podaje mozliwe kombinacje liczb o podanej dlugosci w formie listy krotek
    for i in comb:                                                              #bez podania dlugosci wyskakuje blad
        print(i, end=" ")
    print("\n")
    comb2 = combinations(lista2, 2)                                             #kombinacje tworzone sa na podstanie pozycji w liscie a nie wartosci poszczegolnych elementow
    for i in comb2:                                                             #nie tworzy kombinacji z tymi samymi elementami(ta sama pozycja w liscie)
        print(i, end=" ")

    print("\nKombinacje w powstorzeniami\n")
    powt = combinations_with_replacement(lista, 2)                              #zasady ogolne takie same jak wczesniej
    for i in powt:                                                              #tworzy kombinacje z elementow na tej samej pozycji czyli je powtarza
        print(i, end=" ")
    print("\n")
    powt2 = combinations_with_replacement(lista2, 2)
    for i in powt2:
        print(i, end=" ")

def zad43():
    import time
    h = int(input("Podaj godziny: "))
    m = int(input("Podaj minuty: "))
    s = int(input("podaj sekundy: "))
    while True:
        time.sleep(1)
        print(h, ":", m, ":", s)
        s += 1
        if s == 60:
            m += 1
            s = 0
        elif m == 60:
            h += 1
            m = 0
        elif h == 24:
            h = 0









def main():
    zad43()

main()