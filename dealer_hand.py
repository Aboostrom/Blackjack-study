from deck import Deck

class Dealer:
    def __init__(self, card):
        self.deck = Deck().cards_as_array()
        self.deck.remove(card)
        self.hand = [card, self.deck.pop()]
