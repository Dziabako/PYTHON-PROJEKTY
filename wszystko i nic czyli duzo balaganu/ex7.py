filename = input("Input the Filename: ")
f_extns = filename.split(".")                                       # .split dzieli str na poszczegolne slowa / mozna ustalic separator (separator, maxsplit) lub zostawic puste wtedy bedzie spacja
print ("The extension of the file is : " + repr(f_extns[-1]))       # repr zwraca str ktory moze zostac wysietlony na podstawie podanego parametru
                                                                    # [-1] pozycja po podzieleniu ???????
                                                                    # maxsplit ustala na ile zostanie podzielony str