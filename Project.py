# I have designed a new game, which is based on Card Game 28's point system. This game can be played between minimum 2 players and maximum of 4 players.
# Each player is dealt 5 cards, some of the cards have been alloted points irrespective of the suit, i.e. King and Queen 5 points, Jack 3, 9 2 points and Ace 10 , 1 each.
# Based on the total point scored by the players, the winner is decided.

class Card:
    suit_list = ["Clubs","Diamonds","Hearts","Spades"]
    rank_list = ["None", "Ace", "2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
    def __init__(self,suit = 0, rank=2, point=0):
        self.suit=suit
        self.rank=rank
        #Assigning points to card irrespective of the suit
        if (self.rank_list[self.rank]=="Ace" or self.rank_list[self.rank]=="10"):
            self.point=1   
        elif self.rank_list[self.rank]=="9":
            self.point=2
        elif self.rank_list[self.rank]=="Jack":
            self.point=3
        elif (self.rank_list[self.rank]=="Queen" or self.rank_list[self.rank]=="King"):
            self.point=5
        else:
            self.point=0      
    
    def __str__(self):
        return (self.rank_list[self.rank] + " of " + self.suit_list[self.suit] + " with point " + str(self.point))

import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        s=""
        t=""
        total=0
        for i in range(len(self.cards)):           
            s =str(self.cards[i]) + "\n"
            # splitting the printed statement to get the Points in a new variable e.g. 2 of Diamonds with point 0, 0 will be stored in variable p
            p=s.split(" ")
            # simillarly for all hand for a player will be totaled and stored 
            total = total + int(p[5])
            t = t+s
        t+="\nTotal score = " + str(total)+ "\n"    #total= total+split
        return t
        
    def shuffle(self):
        n_cards=len(self.cards)
        for i in range(n_cards):
            j=random.randrange(0,n_cards)
            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]
    
    def pop_card(self):
        return self.cards.pop()
    
    def is_empty(self):
        return len(self.cards) == 0
    
    def deal(self,hands, n_cards=52):
        n_players=len(hands)
        for i in range(n_cards):
            if self.is_empty():
                break
            card = self.pop_card()
            current_player = i % n_players
            hands[current_player].add_card(card)

class Scores(Deck):
    def __init__(self,pnumber=[]):
        self.pnumber = pnumber
    
    def __str__(self):
        s=""
        k=""
        
        win=[]
        t=0
        score=[]
        for i in range (len(self.pnumber)):
            s=str(self.pnumber[i]).split("\n") #getting info of each player
            k=s[len(s)-2:] # storing the last statement of the player e.g. Total Score = 12
            k=k[0].split(" ") # splitting to get the value of the total score e.g. 12
            z=k[len(k)-1:] # storing the total score in z
            score+= z #storing each players total point in a list score[]. e.g. score[0] contains total point of player1 
        flag=0 
        temp=-1     
        for j in range (len(score)):
            
            if (int(score[j])>temp and int(score[j])!=temp) : # comparing each players score to get the player with highest score.
                t=j
                flag=0
                temp=int(score[j])
            elif(int(score[j])==temp):
                t=j
                flag=1
         #flag indicates whether there is tie or not   
        if(flag!=1):
            win =str(self.pnumber[t]).split(" ")
            return(str(win[1]) + " wins the game" + "\n" + "\n" + "------------GAME OVER------------" + "\n")
        else:
            return(" It is a TIE " + "\n" + "\n" + "------------GAME OVER------------" + "\n")

class Hand(Deck):
    def __init__(self, name = ""):
        self.cards = []
        self.name = name
        
    def add_card(self, card):
        self.cards.append(card)
        
    def __str__(self):
        s="\nHand " + self.name
        if self.is_empty():
            return s + " is empty "
        s += " contains \n" + Deck.__str__(self)
        return s
d = Deck()
d.shuffle()
#Error validation for string input
def int_input(prompt): 
    while True:
        try:
            nosp = int(input(prompt))
            return nosp
        except ValueError as e:
            print("Aah ! Not a integer! Try again")
            
while True:
    nosp = int_input("Enter Number of Players to Start the Game or Press 0 to Quit: ")
    nosp=int(nosp)
    
    if nosp == 4:
        hand1 = Hand(input("Player 1: "))
        hand2 = Hand(input("Player 2: ")) 
        hand3 = Hand(input("Player 3: "))
        hand4 = Hand(input("Player 4: "))
        players = [hand1, hand2, hand3, hand4] 
        d.deal(players, 20) # no of total card 
        print(hand1,hand2,hand3,hand4) #print new player
        print(Scores(players)) # print scores
    elif nosp==3:
        hand1 = Hand(input("Player 1: "))
        hand2 = Hand(input("Player 2: ")) 
        hand3 = Hand(input("Player 3: "))
        players = [hand1, hand2, hand3] 
        d.deal(players, 15) 
        print(hand1,hand2,hand3) 
        print(Scores(players))
    elif nosp==2:
        hand1 = Hand(input("Player 1: "))
        hand2 = Hand(input("Player 2: ")) 
        players = [hand1, hand2] 
        d.deal(players, 10) 
        print(hand1,hand2) 
        print(Scores(players))
    elif nosp==1:
        print("Come on! You cannot play it alone. Min 2 players required \n")
        
    elif nosp==0:
        print("You Chose to quit the game")
        break
    else :
        print("Ok ! it's overcrowded now. Max 4 players allowed \n")
