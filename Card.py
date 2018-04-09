ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["Spade","Heart","Club","Diamond"]

class Card:
    def __init__(self,rank,suit):
        self.rank=ranks[rank]
        self.suit=suits[suit]
    def __str__(self):
        if self.rank ==11:
           return "Jack" +" of " + self.suit +"s"
        elif self.rank ==12:
           return "Queen" +" of " + self.suit +"s"
        elif self.rank ==13:
           return "King" +" of " + self.suit +"s"   
        elif self.rank ==14:
           return "Ace" +" of " + self.suit +"s" 
        else:
            return str(self.rank) +" of " + self.suit +"s"
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def isSuitEqual(self,b):
        '''
        This method will tell if two cards have the same 
        suit.  It will return true if they have the same
        suit and return false otherwise.
        '''
        if self.getSuit()==b.getSuit():
            return True
        else:
            return False
    def isRankEqual(self,b):
        '''
        This method will tell if two cards have the same 
        rank.  It will return true if they have the same
        rank and return false otherwise.
        '''
        if self.getRank()==b.getRank():
            return True
        else:
            return False
    def compareRank(self, b):
        '''
        This method will compare two cards.  It will return true
        if Card b has a higher rank then the card and return false
        otherwise
        '''
        if b.getRank() > self.getRank():
            return True
        else:
            return False