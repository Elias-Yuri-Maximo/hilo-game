
from game.participant import Participant

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """
    def __init__(self):

         """The class constructor.
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.participant = Participant()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        pass
        while self.keep_playing:
            pass

    def update_points(self):
        '''
        Receives the calculated points from participant 
        and keeps track of the points
        Args:
            self(Director): an instance of Director.
        '''
        pass
    def do_outputs(self):
        '''
        print card 
        input is the next card higher or lower?
        player.calculate_points()
        pritn next card
        print points 
        print a message 
        input ask the player play again (Y;n)(if they have more than 0 points)

        Args:
            self(Director): an instance of Director.
        '''
        pass

    