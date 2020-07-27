class Card:
    SUIT = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    VALUE = ['A', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, value=0, suit=0):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return '{0} of {1}'.format(Card.VALUE[self.value], Card.SUIT[self.suit])

    def test_arr(self):
        card_arr = []
        for card in Card.VALUE:
            card_arr.append("{} of Clubs".format(card))
        return card_arr