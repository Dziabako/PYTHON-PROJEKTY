
import string
import random
print("GENERATOR HASEL")
lenght = int(input("Podaj dlugosc hasla: "))
haslo = " "
print("Na pytania odpowiadaj: y/n")
choice = input("Chcesz haslo ze wszystkimi znakami? ")
if choice == "y":
    for i in range(lenght):
        rand_mark = random.choice(string.ascii_letters + string.digits + string.punctuation)
        haslo += rand_mark
elif choice == "n":
    print("Haslo z literami = l")
    print("Haslo z znakami = z")
    print("Haslo z numerami = n")
    choice = input("Co wybierasz?: ")
    if choice == "l":
        print("Chcesz haslo tylko z literami czy +liczbami lub +znakami? = l / n / z")
        choice = input("Co wybierasz? ")
        if choice == "l":
            print("Litrey duze, male czy obojetne? = d / m / o")
            choice = input("Co wybierasz? ")
            if choice == "d":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_uppercase)
                    haslo += rand_mark
            elif choice == "m":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_lowercase)
                    haslo += rand_mark
            elif choice == "o":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_letters)
                    haslo += rand_mark
        elif choice == "n":
            print("Litrey duze, male czy obojetne? = d / m / o")
            choice = input("Co wybierasz? ")
            if choice == "d":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_uppercase + string.digits)
                    haslo += rand_mark
            elif choice == "m":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_lowercase + string.digits)
                    haslo += rand_mark
            elif choice == "o":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_letters + string.digits)
                    haslo += rand_mark
        elif choice == "z":
            print("Litrey duze, male czy obojetne? = d / m / o")
            choice = input("Co wybierasz? ")
            if choice == "d":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_uppercase + string.punctuation)
                    haslo += rand_mark
            elif choice == "m":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_lowercase + string.punctuation)
                    haslo += rand_mark
            elif choice == "o":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_letters + string.punctuation)
                    haslo += rand_mark
    elif choice == "z":
        print("Chcesz miec tez liczby? lub litery? czy same znaki? y/l/n")
        choice = input("Co wybierasz?: ")
        if choice == "y":
            for i in range(lenght):
                rand_mark = random.choice(string.punctuation + string.digits)
                haslo += rand_mark
        elif choice == "l":
            print("Litrey duze, male czy obojetne? = d / m / o")
            choice = input("Co wybierasz? ")
            if choice == "d":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_uppercase + string.punctuation)
                    haslo += rand_mark
            elif choice == "m":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_lowercase + string.punctuation)
                    haslo += rand_mark
            elif choice == "o":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_letters + string.punctuation)
                    haslo += rand_mark
        elif choice == "n":
            for i in range(lenght):
                rand_mark = random.choice(string.punctuation)
                haslo += rand_mark
    elif choice == "n":
        print("Chcesz miec tez znaki? lub litery? czy same liczby? y/l/n")
        choice = input("Co wybierasz?: ")
        if choice == "y":
            for i in range(lenght):
                rand_mark = random.choice(string.punctuation + string.digits)
                haslo += rand_mark
        elif choice == "l":
            print("Litrey duze, male czy obojetne? = d / m / o")
            choice = input("Co wybierasz? ")
            if choice == "d":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_uppercase + string.digits)
                    haslo += rand_mark
            elif choice == "m":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_lowercase + string.digits)
                    haslo += rand_mark
            elif choice == "o":
                for i in range(lenght):
                    rand_mark = random.choice(string.ascii_letters + string.digits)
                    haslo += rand_mark
        elif choice == "n":
            for i in range(lenght):
                rand_mark = random.choice(string.digits)
                haslo += rand_mark

print("\nTwoje haslo to: ", haslo)