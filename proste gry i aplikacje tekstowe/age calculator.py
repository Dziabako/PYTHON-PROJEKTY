from datetime import datetime
import time

def get_user_birthday():
    date_str = input("Podaj date urodzin w formacie DD/MM/YYYY: ")
    try:
        birthday = datetime.strptime(date_str, "%d/%m/%Y")
    except TypeError:
        birthday = datetime(*(time.strptime(date_str, "%d/%m/%Y")[0 : 6]))
    return birthday

def age(birthday):
    today = datetime.today()                                                        #aktualna date
    days = (today - birthday).days                                                  #liczba dni miedzy dzisiaj i data urodzin
    age = days // 365                                                               #wiek
    return age

birthday = get_user_birthday()
age = age(birthday)
print("Twoj wiek to: ", age)