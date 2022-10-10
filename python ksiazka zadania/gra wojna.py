import karty
import gra

class W_Card(karty.Cards):
    def __init__(self, rank, suit):
        super(W_Card, self).__init__()
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

    def value(self):
        if W_Card.RANKS.index(self.rank) == 0:
            v = 15
        else:
            v = W_Card.RANKS.index(self.rank) + 1
        return v


class W_Deck(karty.Deck):
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))


class W_Hand(karty.Hand):
    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + super(W_Hand, self).__str__()
        if self.total():
            rep += f'({str(self.total())})'
        return rep

    def total(self):
        t = 0
        for card in self.cards:
            t += card.value()
        return t


class W_Player(W_Hand):
    def lose(self):
        print(f'{self.name} przegrywa!')

    def win(self):
        print(f'{self.name} wygrywa!')

    def push(self):
        print(f'{self.name} remnisuje!')


class W_Game:
    def __init__(self, names):
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)

        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def biggest_value(self):
        big = []
        for player in self.players:
            big.append(player.total())
        return big

    def play(self):
        self.deck.deal(self.players)

        for player in self.players:
            print(player)
            if player.total() == max(self.biggest_value()):
                player.win()
                if player.total() == player.total():
                    player.push()
            else:
                player.lose()


def main():
    print("Gra w wojne")

    names = []
    number =  gra.ask_number("Podaj liczbę graczy (2 - 7): ", low = 2, high = 8)
    for i in range(number):
        name = input('Podaj imie gracza: ')
        names.append(name)

    game = W_Game(names)

    response = None
    while response != 'n':
        game.play()
        response = gra.ask_yes_no('Chcesz grac dalej?: ')


main()
input("Aby zakonczyc nacisnij klawisz ENTER")
