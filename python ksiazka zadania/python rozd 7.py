import pickle
import sys


def open_file(file_name, mode):
    # otwarcie pliku
    try:
        the_file = open(file_name, mode)
    except IOError:
        print(f"Nie mozna otworzyc pliku {file_name}! Program zostanie zakonczony!\n")
        input("\n\nAby zakonczyc nacisnij klawisz ENTER")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    # zwraca kolejny wiersz pliku po sformatowniu go
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    # zwraca kolejny blok danych z pliku
    category = next_line(the_file)
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    scores = next_line(the_file)

    return category, question, answers, correct, explanation, scores


# zapisywanie wynikow przy uzyciu marynowania
def best_score(title, score, path):
    with open(path, 'wb') as f:
        best = {title: score}
        pickle.dump(best, f)


# wyswietalnie zamarynowanych plikow
def show_score_board(path):
    with open(path, 'rb') as f:
        score_board = pickle.load(f)
    return print(score_board, '\n')


# wyniki zapisywane w pliku tekstowym jako string
def best_score_txt(title, score, path):
    with open(path, 'w') as f:
        b = f"{title} : {score}\n"
        f.write(b)


# odczytywanie danych z pliku tekstowego
def show_score_board_txt(path):
    with open(path, 'r') as f:
        return print(f.read())


def welcome(title):
    # wita gracza i pobiera jego nazwe
    print("\t\tWitaj w turnieju wiedzy\n")
    print(f"\t\t{title}!\n")


def main():
    path = r"D:\PYTHON PROJEKTY\proste gry i aplikacje tekstowe\kwiz rozd 7 python dla kazdego ksiazka\kwiz.txt"
    path2 = r"D:\PYTHON PROJEKTY\proste gry i aplikacje tekstowe\kwiz rozd 7 python dla kazdego ksiazka\best_scores.dat"
    
    trivia_file = open_file(path, 'r')
    title = input("Podaj swoje imie: ")
    welcome(title)
    score = 0

    # pobranie pierwszego bloku
    category = next_line(trivia_file)
    question = next_line(trivia_file)
    answers = next_line(trivia_file)
    correct = next_line(trivia_file)
    explanation = next_line(trivia_file)
    scores = next_line(trivia_file)
    while category:
        # zadawanie pytan
        print(category)
        print(question)
        for i in range(4):
            print(f"\t {i + 1} - {answers[i]}")

        # odpowiedz gracza
        answer = input("Jaka jest Twoja odpowiedz: ")

        #sprawdzanie odpowiedzi
        if answer == correct:
            print("\nPrawidlowa odpowiedz", end=" ")
            score += scores
        else:
            print("\nNieprawidlowa odpowiedz", end=" ")
        print(explanation)
        print(f"Wynik: {score} \n\n")

        # pobranie kolejnego bloku
        category = next_line(trivia_file)
        question = next_line(trivia_file)
        answers = next_line(trivia_file)
        correct = next_line(trivia_file)
        explanation = next_line(trivia_file)
        scores = next_line(trivia_file)

    trivia_file.close()

    print("To bylo ostanie pytanie")
    print(f"Twoj koncowy wynik wynosi {score}")

    best_score(title, score, path2)
    print("Tabela wynbikow wyglada nastepujaco: ")
    show_score_board(path2)


main()
input("\n\nAby zakonczyc nacisnij klawisz ENTER.")
