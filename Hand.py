import Deck
class Hand:
    def __init__(self, inputDeck):
        self.deck=inputDeck
    def drawHand(self):
        self.hand =[]
        self.hand.append(self.deck.drawCard())
        self.hand.append(self.deck.drawCard())
        self.hand.append(self.deck.drawCard())
        self.hand.append(self.deck.drawCard())
        self.hand.append(self.deck.drawCard())
    def setHand(self, cardOne,cardTwo,cardThree,cardFour,cardFive):
        self.hand =[]
        self.append(cardOne)
        self.append(cardTwo)
        self.append(cardThree)
        self.append(cardFour)
        self.append(cardFive)
    def getPokerHand()
    '''
    This method will return the poker hand rank.
    1 - No Pair
    2 - One Pair
    3 - Two Pair
    4 - Three of a Kind
    5 - Straight
    6 - Flush
    7 - Full House
    8 - Four of a Kind
    9 - Straight Flush
    10 - Royal Flush
    '''
    return 1
        