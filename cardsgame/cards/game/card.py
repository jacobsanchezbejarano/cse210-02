import random




# Class declaration.
"""A set of cards from 1 to 13.

    The responsibility of Card is to keep track of the number of the current 
    card.
   
    Attributes:
        suits (list): A list of card suits.
        value (int): The number of the card.
        last_card (int): The number of the last card.
        suit (string): The suit of the current card.
        last_suit (string): The suit of the last card.
        points  (int): The number of points.
        decision (string): The player's choice.
        
    
    """

class Card:
       
# 2) Creating the class constructor.
    """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """

    def __init__(self):
        
        self.suits = ["clubs","diamonds","hearts","spades"]

        self.last_card = 0
        self.last_suit = ""

        self.value = 0
        self.suit = ""

        self.points = 0
        self.decision = ""

# 3) Create the next_card(self) method.
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
    def next_card(self):
        if self.last_card == 0:
            self.last_card = random.randint(1,13)
            self.last_suit = self.suits[random.randint(0,3)]
            self.value = random.randint(1,13)
            self.suit = self.suits[random.randint(0,3)]
        else:
            self.value = random.randint(1,13)
            self.suit = self.suits[random.randint(0,3)]

# 4) Create the evaluate(self) method.
        """Calculates the points acording to the player's decision and the 
        comparison of last card and current card value.
        Also, it updates the card's suit.
        
        Args:
            self (Card): An instance of Card.
        """
    def evaluate(self):


        while self.value == self.last_card:
                self.value = random.randint(1,13)
                self.suit = self.suits[random.randint(0,3)]

        if self.decision == "h":
            
            if self.value > self.last_card:
                self.points = 100
            elif self.value < self.last_card:
                self.points = -75
            else:
                self.points = 0

        elif self.decision == "l":
            
            if self.value < self.last_card:
                self.points = 100
            elif self.value > self.last_card:
                self.points = -75
            else:
                self.points = 0
            
        self.last_card = self.value
        self.last_suit = self.suit

        


    
