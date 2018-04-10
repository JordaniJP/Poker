import Card
import random
class Deck:
    def __init__(self):
        self.deck =[]
        for x in range(len(Card.suits)):
            for y in range(len(Card.ranks)):
                temp = Card.Card(y,x)
                self.deck.append(temp)
    def __str__(self):
        ans = ""
        for i in self.deck:
            ans += str(i)+"\n"
        return ans
    def dealCard(self):
        '''
        This method will return a random card from the deck.
        This card will be removed from the deck and can not 
        be drawn again.  If the deck is empty it will shuffle
        up a new deck and draw from that
        '''
        #check to see if the deck is empty
        if(len(self.deck)<=0):
            #if empty create a new deck
            self.deck =[]
            for x in range(len(Card.suits)):
                for y in range(len(Card.ranks)):
                    temp = Card.Card(y,x)
                    self.deck.append(temp)
        rand = random.randint(0,len(self.deck)-1)
        # this will get the random card
        card = self.deck[rand]
        #this will remove the card
        del self.deck[rand]
        #this will return the random card
        return card
        
        