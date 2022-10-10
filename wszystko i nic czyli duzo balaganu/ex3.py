import datetime                                     # importowanie modulu z data i godzina
now = datetime.datetime.now()                       # datetime. - podobnie jak random.  / /   datetime - użycie daty i czasu, now() - zwraca aktualna date i czas
print("Current date and time:")
print(now.strftime("%Y - %m - %d %H : %M : %S"))    # strftime - zwraca lancych reprezentujacy date i czas