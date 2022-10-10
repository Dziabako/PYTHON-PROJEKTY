print("Liczydlo\n")
print("Podaj liczbe poczatkowa, koncowa oraz odstepy miedzy liczbami:")

begin = int(input("Początek: "))
end = int(input("Koniec: "))
space = int(input("Odstep: "))

print("\nZacznijmy liczyc!")
for i in range(begin, end, space):
    print(i, end=" ")
#end=" " sprawia ze liczby pojawiaja sie jedna po drugiej w jednym wierszu a nie kazda w osobnym wierszu