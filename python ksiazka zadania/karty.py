# Karty do gry

class Cards:
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K"]

    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = 'XX'
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ' '
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            print('<pusta>')
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    # Faktyczna talia do gry
    def populate(self):
        for suit in Cards.SUITS:
            for rank in Cards.RANKS:
                # self to bedzie nowo storzony obiekt ktory bedzie odpowiadal za talie do gry
                # jako argument jest podana karta do gry z obiektu z poprzedniej klasy
                self.add(Cards(suit, rank))
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie moge dalej rozdawac! Zabraklo kart")


if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
