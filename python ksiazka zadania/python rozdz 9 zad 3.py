import karty, gra

class BJ_Card(karty.Cards):
    ACE_VALUE = 1

    def value(self):
        # self.is_face_up jest zaimportowany z karty.Cards
        if self.is_face_up:
            # pierwsza czesc odposni sie do listy RANKS
            # potem jest index kazdej rangi z RANKS i dodawany jest 1 zeby byla poprawna wartosc
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(karty.Deck):
    # ta metoda jest przeslonieta poniewaz chcemy by to TA klasa otrzymala talie a nie klasa bazowa
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(karty.Hand):
    def __init__(self, name):
        # super() sluzy do uzywania metody bazowej razem z metoda z nowej klasy
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + super(BJ_Hand, self).__str__()
        if self.total():
            rep += f'({str(self.total())})'
        return rep

    def total(self):
        for card in self.cards:
            # .value to metoda z klasy wyzej
            # card jest tak jakby obiektem klasy wyzej
            if not card.value():
                return None

            # sumowanie wartosci kart, as = 1
            t = 0
            for card in self.cards:
                t += card.value()

            # czy reka zawiera asa
            contain_ace = False
            for card in self.cards:
                if card.value() == BJ_Card.ACE_VALUE:
                    contain_ace = True

            # jezeli zawiera asa
            if contain_ace:
                # tylko 10 bo AS ma juz wartosc 1
                t += 10
            
            return t

    def is_busted(self):
        return self.total() > 21


# przy towrzeniu obiektu tej klasy trzeba podac imie poniewaz
# w BJ_Hand jest argument name
class BJ_Player(BJ_Hand):
    def __init__(self, name, acc=500):
        super(BJ_Player, self).__init__(name)
        self.name = name
        self.acc = acc

    def __str__(self):
        if self.acc:
            rep = super(BJ_Player, self).__str__() + f"\tStan konta: {str(self.acc)}"
        return rep

    def is_hitting(self):
        response = gra.ask_yes_no("\n" + self.name + ", chcesz dobrać kartę? (T/N): ")
        return response == 't'

    def bid(self):
        if self.acc > 0:
            bid = int(input(f'{self.name} ile chcesz postawic?: '))
            self.acc -= bid
        return bid

    def bust(self):
        print(f'{self.name} ma fure!')
        self.lose()

    def lose(self):
        print(f'{self.name} przegrywa!')

    def win(self):
        print(f'{self.name} wygrywa i zgarnia cala pule!')

    def push(self):
        print(f'{self.name} remnisuje!')

    def out_of_money(self):
        if self.acc <= 0:
            print(f'{self.name} nie ma juz pieniedzy')
            self.lose()


# tak samo z name jest tutaj
class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total() < 17

    def bust(self):
        print(f'{self.name} ma fure!')

    def flip_first_card(self):
        # odwraca pierwsza karte dlatego przy uruchomieniu pokazuje XX
        first_card = self.cards[0]
        first_card.flip()



class BJ_Game:
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        # to jest nowy obiekt w metodzie klasy
        self.dealer = BJ_Dealer("Rozdajacy")

        self.deck = BJ_Deck()
        # w teori jak self.deck zwraca True lub False to zawsze bedzie towrzyc nowa talie do gry
        if self.deck:
            self.deck.populate()
            self.deck.shuffle()
        else:
            self.deck.populate()
            self.deck.shuffle()

    def still_playing(self):
        sp = []
        for player in self.players:
            # metoda wywolywana na kazdym graczu z listy
            if not player.is_busted() or not player.out_of_money():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() or not player.out_of_money() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
            
    def play(self):
        # rozdawani kazdemu po dwie karty
        # dealer jest w [] poniewaz jest dodawany do listy players
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        # ukrywanie pierwszej karty rozdajacego
        self.dealer.flip_first_card()
        for player in self.players:
            # wartosci punktow sa pobierane z metody BJ_Player
            print(player)
        print(self.dealer)

        m = 0

        # rozdawanie dodatkowych kart
        for player in self.players:
            self.__additional_cards(player)
            m += player.bid()

        # odslon pierwsza karte rozdajacego
        self.dealer.flip_first_card()

        if not self.still_playing():
            # tylko rozdajacy zostal
            print(self.dealer)
        else:
            # daj dodatkowe karty rozdajacemu
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # kto zostal wygrywa
                for player in self.still_playing():
                    player.win()
            else:
                # porownanie wszystkich punktow
                for player in self.still_playing():
                    if player.total() > self.dealer.total():
                        player.win()
                        print(f'Wygrana {m}')
                    elif player.total() < self.dealer.total():
                        player.lose()
                    else:
                        player.push()

        #usuwanie wszytkich kart
        for player in self.players:
            player.clear()
        self.dealer.clear()
        m = 0


def main():
    print('\t\tWitaj w grze Blackjack!\n')

    names = []
    number =  gra.ask_number("Podaj liczbę graczy (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input('Podaj imie gracza: ')
        names.append(name)

    game = BJ_Game(names)

    again = None
    while again != 'n':
        game.play()
        again = gra.ask_yes_no("Chcesz zagrac jeszcze raz? (t/n): ")


main()
input("Aby zakonczyc nacisnij klawisz ENTER")
