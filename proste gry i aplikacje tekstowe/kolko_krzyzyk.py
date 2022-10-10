print("Kolko i Krzyzyk!")

# Wyświetl instrukcje do gry
# Wybierz tryb gry
    # single - rozgrywka z komputerem    (dopisac pozniej)
    # multi - rozgrywka z druga osoba
# gra sie rozpoczyna
    # losowanie kto pierwszy
    # wyswietlenie planszy z pustymi polami
    # podanie pola na ktore postawic znak
    # zmiana gracza
        # podawanie pozycji i zmiana az do momentu az ktoras ze stron nie wygra lub remis
    # ustal kto wygral
        # single - komputer czy gracz
        # multi - O czy X
        # remis
# wyswietlenie komunikatu o skonczonej grze i wyniku


# zmienne globalne
player = "X"
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
ongoing = True
winner = None
import random

def game():
    instructions()
    print("""
    Wybierz tryb gry:
    1 - Single
    2 - Multi
    """)
    gamemode = int(input(""))
    if gamemode == 1:
        print("Wybrałeś tryb dla pojedynczego gracza")
        print("To be implemented")
    elif gamemode == 2:
        print("Wybrałeś tryb dla dwoch graczy")
        who_first()
        while ongoing:
            humans_move()
            check_win()
            check_tie()
            switch_player()



def instructions():
    print("""
    Zasady są takie same jak w tradycyjnej grze kolko i krzyzyk.
    Do postawienia swojego znaku nalezy wybrac numer od 1 do 9.
    Plansza do gry wyglada nastepujaco:
    
                1 | 2 | 3
                4 | 5 | 6
                7 | 8 | 9   
    """)


def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])


def humans_move():
    position = input("Podaj pozycje od 1 do 9: ")
    position = int(position) - 1
    board[position] = player
    display_board()

def switch_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return

def who_first():
    global player
    gracze = ["X", "O"]
    roll = random.choice(gracze)
    player = roll
    print("Zaczyna gracz: ", player)

def check_win():
    global winner
    global ongoing
    if board[0] == board[1] == board[2] != " ":
        winner = player
        ongoing = False
    elif board[3] == board[4] == board[5] != " ":
        winner = player
        ongoing = False
    elif board[6] == board[7] == board[8] != " ":
        winner = player
        ongoing = False
    elif board[0] == board[3] == board[6] != " ":
        winner = player
        ongoing = False
    elif board[1] == board[4] == board[7] != " ":
        winner = player
        ongoing = False
    elif board[2] == board[5] == board[8] != " ":
        winner = player
        ongoing = False
    elif board[0] == board[4] == board[8] != " ":
        winner = player
        ongoing = False
    elif board[2] == board[4] == board[6] != " ":
        winner = player
        ongoing = False
    while winner:
        print("Wygrywa gracz: ", winner)
        break
    return

def check_tie():
    global ongoing
    if " " not in board:
        ongoing = False
        print("Gra zakonczona remisem!")
    return

def computer_move():
    newboard = board[:]
    


game()