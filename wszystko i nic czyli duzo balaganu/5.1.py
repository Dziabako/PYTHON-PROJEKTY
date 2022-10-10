print("Zamieniator!\n")

import random
words = ["kolo", 'bolo', 'olo', 'ulu', 'mulu', 'ulumulu']

#shuffle zmienia kolejnosc listy lecz nie tworzy nic nowego z istniejacych elementow
random.shuffle(words)
print(words, end=" ")