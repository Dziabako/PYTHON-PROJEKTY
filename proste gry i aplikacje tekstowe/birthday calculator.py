from datetime import datetime
import time

def get_user_birthday():
    date_str = input("Podaj date urodzin w formacie DD/MM/YYYY: ")
    try:
        birthday = datetime.strptime(date_str, "%d/%m/%Y")                                          #zamiana podanej wczesniej daty na format PYTHON
    except TypeError:                                                                               #musi byc ona w postaci str dlatego nie uzywamy INT
        birthday = datetime(*(time.strptime(date_str, "%d/%m/%Y")[0 : 6]))                          #FORMAT TRY I EXCEPT DO POCZYTANIA
    return birthday

def days_remaining(birth_date):
    now = datetime.now()                                                                            #uzyskanie aktualnej daty za pomoca modulu z python
    current_year = datetime(now.year, birth_date.month, birth_date.day)                             #Data urodzin w danym roku - kolejno jest rok, miesiac, dzien
    days = (current_year - now).days                                                                #obliczanie czasu do urodzin / po kropce jest formatowane odpowiednio w dni (lub miesiace, lata)
    if days < 0:                                                                                    #wykonywane jesli urodziny juz byly
        next_year = datetime(now.year + 1, birth_date.month, birth_date.day)                        #do aktualnego roku dodawany jest jeden zeby uzyskac nastepny rok
        days = (next_year - now).days
    return days

birthday = get_user_birthday()
next_birthday = days_remaining(birthday)
print("Twoje urodziny sa za: ", next_birthday)