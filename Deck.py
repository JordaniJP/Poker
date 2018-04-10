import Card
class Deck:
    def __init__(self):
        self.deck =[]
        for x in range(len(Card.suits)):
            for y in range(len(Card.ranks)):
                temp = Card.Card(y,x)
                print(temp)
                self.deck.append(temp)