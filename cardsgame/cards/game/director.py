from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.is_playing = True
        self.total_score = 300
        self.current_card = ""

        card = Card()
        self.current_card = card

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to continue playing.

        Args:
            self (Director): An instance of Director.
        """
        self.current_card.next_card()
        print(f"The card is: {self.current_card.last_card} {self.current_card.last_suit}")
        guess_card = input("Higher or lower? [h/l] ")
        self.is_playing = (guess_card == "h" or guess_card == "l")
        
        self.current_card.decision = guess_card

       
    def do_updates(self):
        """Evaluates the player's decision and updates his score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        self.current_card.evaluate()
        self.current_card.next_card()

        self.total_score += self.current_card.points

    def do_outputs(self):
        """Displays the next card's value and the score. 
        Also asks the player if he want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        

        print(f"Next card was: {self.current_card.last_card} {self.current_card.last_suit}")
        print(f"Your score is: {self.total_score}")
        self.is_playing = (self.total_score > 0)
        playagain = input("Play again? [y/n] ")
        self.is_playing = (playagain == "y")
        print()


        if not self.is_playing:
            print("Game Over!")
        