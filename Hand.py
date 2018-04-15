from Deck import Deck
from Card import Card
class Hand:
    def __init__(self, inputDeck):
        self.deck=inputDeck
    def drawHand(self):
        self.hand =[]
        self.hand.append(self.deck.dealCard())
        self.hand.append(self.deck.dealCard())
        self.hand.append(self.deck.dealCard())
        self.hand.append(self.deck.dealCard())
        self.hand.append(self.deck.dealCard())
        self.hand.sort()
    def setHand(self, cardOne,cardTwo,cardThree,cardFour,cardFive):
        self.hand =[]
        self.append(cardOne)
        self.append(cardTwo)
        self.append(cardThree)
        self.append(cardFour)
        self.append(cardFive)
    def getPokerHand(self):
        rankings = list(map(Card.getRank, self.hand))
        suits = list(map(Card.getSuit, self.hand))
        if 14 and 13 and 12 and 11 and 10 in rankings:
            return 10
        elif rankings[0] == rankings[1]-1 and rankings[1] == rankings[2]-1 and rankings[2] == rankings[3]-1 and rankings[3] == rankings[4]-1 and suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
            return 9
        elif rankings[0] == rankings[1] and rankings[1] == rankings[2] and rankings[2] == rankings[3] and rankings[3] == rankings[4]:
            return 8
        elif rankings[0] == rankings[1] and rankings[2] == rankings[1] and rankings[3] == rankings[4] or rankings[4] == rankings[3] and rankings[3] == rankings[2] and rankings[0] == rankings[1]:
            return 7 
        elif suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
            return 6
        elif rankings[0] == rankings[1]-1 and rankings[1] == rankings[2]-1 and rankings[2] == rankings[3]-1 and rankings[3] == rankings[4]-1:
            return 5
        elif rankings[0] == rankings[1] and rankings[1] == rankings[2] or rankings[1] == rankings[2] and rankings[2] == rankings[3] or rankings[2] == rankings[3] and rankings[3] == rankings[4]:
            return 4
        elif rankings[0] == rankings[1] and rankings[2] == rankings[3] or rankings[0] == rankings[1] and rankings[3] == rankings[4] or rankings[1] == rankings[2] and rankings[3] == rankings[4]:
            return 3
        elif rankings[0] == rankings[1] or rankings[1] == rankings[2] or rankings[2] == rankings[3] or rankings[3] == rankings[4]:
            return 2
        elif rankings[1] != rankings[2]:
            return 1