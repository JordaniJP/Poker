import Card
ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["Spade","Heart","Club","Diamond"]
class Deck:
    def __init__(self):
        self.deck =[]
        for x in range(len(Card.suits)):
            for y in range(len(Card.ranks)):
                temp = Card.Card(y,x)
                print(temp)
                self.deck.append(temp)