def zad1():
    class Pojazdy:
        kolor = " "
        rodzaj = " "
        wartosc = 100.00
        nazwa = " "

        def opis(self):
            opis = "%s to %s %s warty %.2f zl" % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)                    # w ten sposob formatujemy str na obecnosc zmiennych
            return opis                                                                                                 # %.2f znaczy ze liczba bedzie miala tylko 2 liczby po przeciku

    auto1 = Pojazdy()
    auto1.kolor = "czerwony"
    auto1.rodzaj = "kabriolet"
    auto1.wartosc = 60000
    auto1.nazwa = "Ferrari"

    auto2 = Pojazdy()
    auto2.kolor = "niebieski"
    auto2.rodzaj = "autobus"
    auto2.wartosc = 10000
    auto2.nazwa = "Ikarus"

    print(auto1.opis())
    print(auto2.opis())


def zad2():
    class Int_To_Roman:
        def int_to_roman(self, num):
            nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                    (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

            roman = " "
            while num > 0:                                                                                              #poki num jest wiekszy od 0
                for i, r in nums:                                                                                       #iterowanie przez liczbe i liczbe rzymska jednoczesnie
                    while num >= i:                                                                                     #zaczyna sie wykonywac kiedy i (z nums) jest mniejsze lub rowne num
                        roman += r                                                                                      #dodaje odpowiednia litere kiedy jest spelniony warunek
                        num -= i                                                                                        #odejmuje i i zaczyna od nowa
            return roman

    print(Int_To_Roman().int_to_roman(1))
    rom2 = Int_To_Roman()
    print(rom2.int_to_roman(4000))

    class py_solution:                                                                                                  #druga metoda nie rozumiem dokladnie
        def int_to_Roman(self, num):
            val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
            ]
            syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
            ]
            roman_num = ''
            i = 0
            while num > 0:
                for _ in range(num // val[i]):
                    roman_num += syb[i]
                    num -= val[i]
                i += 1
            return roman_num

    print(py_solution().int_to_Roman(1))
    print(py_solution().int_to_Roman(4000))


def zad3():
    class Roman:
        def rom_to_int(self, str1):
            roman = {"M": 1000, "D": 500, "C": 100, "L": 50,
                     "X": 10, "V": 5, "I": 1}
            numb = 0
            for i in range(len(str1)):
                if i > 0 and roman[str1[i]] > roman[str1[i - 1]]:                           # jezeli nie damy ze i > 0 to ta linia kodu wykona sie jako pierwsza przez co nie bedzie dzialac odpowiednio
                    numb += roman[str1[i]] - 2 * roman[str1[i - 1]]
                else:
                    numb += roman[str1[i]]

            return numb

    print(Roman().rom_to_int("MMXL"))



def zad4():
    class Exercise4:
        def nawiasy(self, stri):
            stack = []
            par = {"(": ")", "{": "}", "[": "]"}
            for p in stri:
                if p in par:
                    stack.append(p)
                elif par[stack.pop()] != p:                              # usuwany jest ostani element z listy i wchpdzi jako klucz o danej wartosci ktory jest rowny z innym
                    return False                                         # jezeli wartosci nie sa rowne zwracany jest FALSE
            return len(stack) == 0

    print(Exercise4().nawiasy("()(){}[]"))
    print(Exercise4().nawiasy("()(){)}[]"))


def zad5():
    # NIE ROZUMIEM TEGO!!!!!!!
    class Exercise:
        def sums(self, nums, target):
            lookout = {}
            for i, num in enumerate(nums):                              #wbudowana funkcja ktora zwraca numer iteracji oraz wartosc jednoczesnie
                if target - num in nums:
                    return lookout[target - num], i
                lookout[num] = i

    print("index1=%d, index2=%d" % Exercise().sums((10, 20, 10, 40, 50, 60, 70), 50))


def zad6():
    # KOLEJNE KTOREGO NIE ROZUMIEM
    class Exercise:
        def threeSum(self, nums):
            nums, result, i = sorted(nums), [], 0
            while i < len(nums) - 2:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                i += 1
                while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                    i += 1
            return result

    print(Exercise().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


def zad7():
    class Potegowanie:
        def power(self, x, n):
            if x == 1 or x == 0 or n == 1:
                return x
            elif x == -1:
                if n % 2 == 0:
                    return 1
                else:
                    return -1
            elif n == 0:
                return 1
            elif n < 0:
                return 1 / x ** abs(n)
            elif n > 0:
                return x ** n

    print(Potegowanie().power(2, -3))
    print(Potegowanie().power(3, 5))
    print(Potegowanie().power(100, 0))

def zad8():
    class Reversed:
        def rev(self, str):
            r = str.split()
            rev = reversed(r)
            return print(" ".join(rev))

    Reversed().rev("Hello World!")

    class py_solution:
        def reverse_words(self, s):
            # typowa rekursja dziala tak samo co wyzej ale krotszy kod
            return ' '.join(reversed(s.split()))

    print(py_solution().reverse_words('hello .py'))


def zad9():
    class String:
        # nie deklarujemy zmiennej w nawiasie wiec pozostale funkcje maja racje bytu
        # definiujemy tylko pusty string do wykorzystania w funkcjach w klasie
        # tak jaby podobne do definiowania pustej zmiennej w funkcjach
        def __init__(self):
            self.str = ""

        def get_str(self):
            self.str = input()

        def print_str(self):
            print(self.str.upper())

    string = String()
    string.get_str()
    string.print_str()



zad9()
