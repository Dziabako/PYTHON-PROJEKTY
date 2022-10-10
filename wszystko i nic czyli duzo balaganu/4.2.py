print("Odwracaczoinator!")
print("Podaj komunikat a program odwroci jego kolejnosc.\n")

message = input("Podaj swoj komunikat: ")
new_message = message[ : : -1]
#[start : koniec : step] jezeli nie podamy dwoch pierwszych program przyjmnie wartosc 0 dla start
#koniec w dimysle przyjmuje ostatni element str
#dlatego dlugosc str bedzie w domysle dlugoscia dowolnego str
#step -1 oznacza ze rozpoczynac bedziemy od konca tak jak to jest przy petli for

print("\nTwoj odwrocony komunikat to: ", end=" ")
print(new_message)