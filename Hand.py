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
        sorted(self.hand, reverse=False)
    def setHand(self, cardOne,cardTwo,cardThree,cardFour,cardFive):
        self.hand =[]
        self.append(cardOne)
        self.append(cardTwo)
        self.append(cardThree)
        self.append(cardFour)
        self.append(cardFive)
        def getPokerHand():
            if 14 and 13 and 12 and 11 and 10 in self.hand:
                return 10
            elif self.hand[1] == self.hand[0]+1 and self.hand[2] == self.hand[1]+1 and self.hand[3]==self.hand[2]+1 and self.hand[4]==self.hand[3]+1:
                return 5
            elif self.hand[2] == self.hand[1]+1 and self.hand[3]==self.hand[2]+1 and self.hand[4]==self.hand[3]+1:
                return 5
            elif self.hand[0] == self.hand[1] and self.hand[1] == self.hand[2] and self.hand[2] == self.hand[3]:
                return 8
            elif self.hand[1] == self.hand[2] and self.hand[2] == self.hand[3] and self.hand[3] == self.hand[4]:
                return 8   
            elif self.hand[0] == self.hand[1] and self.hand[1] == self.hand[2]:
                return 4
            elif self.hand[1] == self.hand[2] and self.hand[2] == self.hand[3]:
                return 4
            elif self.hand[2] == self.hand[3] and self.hand[3] == self.hand[4]:  
                return 4
            elif self.hand[0] == self.hand[1] or self.hand[1] == self.hand[2] or self.hand[2] == self.hand[3] or self.hand[3] == self.hand[4]:
                return 2   
            
        
        