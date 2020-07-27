from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for value in range(0,13):
                self.cards.append(Card(value, suit))
    
    def __str__(self):
        cards = ""
        for card in self.cards:
            cards += '{0} '.format(card)
        return cards
    
    def cards_as_array(self):
        card_arr = []
        for card in self.cards:
            card_arr.append('{}'.format(card))
        random.shuffle(card_arr)
        return card_arr
