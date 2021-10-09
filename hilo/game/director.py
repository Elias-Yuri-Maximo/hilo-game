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
        self.cards_list = []
        self.current_round_index = 0
        self.guess = "#"

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director.
        """
        #self.cards_list = shuffle()
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()

    # def shuffle(self):
    #    '''
    #    When called will generate a a random, non repeated,  list of numbers between 1-13
    #    the list was already declared, so it should only append to it (list.append(item))'''
    #    random_list = random.sample(range(1, 14), 13)
    #    return random_list

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        self.participant.shuffle()

    def update_points(self):
        '''
        Shows the card, asks the player and updates points.
        Receives the calculated points from participant
        and keeps track of the points
        Args:
            self(Director): an instance of Director.
        '''
        #print(f'This card is:{self.cards_list[self.current_round_index]}')
        # dealer prints current card
        #guess = input("is the next card higher or lower?(h/l)")
        # asks the player if they  think it is lower or higher
        #print(f'Next card was:{self.cards_list[self.current_round_index + 1]}')
        # prints the next card.

        # makes this the current card.
        self.score = self.score + \
            (self.participant.calculate_points(
                self.guess))
        self.current_round_index += 1
        # calculate_points() in participant should return the points FOR THE TURN
        # the participant calculates the score and it is added to current score,
        # which is then atributerd to current score.

    def do_outputs(self):
        '''
        Prints the total score, calls the can_play function to to change the
        keep_playing value to False, if the player cannot play anymore.
        Args:
            self(Director): an instance of Director.
        '''
        if self.participant.can_play(self.score):
            print(f'This card is:{self.participant.card_value}')

            # prints the score.
            self.guess = input("is the next card higher or lower?(h/l)")
            print(f'Next card was:{self.participant.card_new_value}')
            # attributes the players answer to choice.
            #self.keep_playing = self.participant.can_play(choice)
            # should can play should return a true boolean if the player
            # still wants to play, and if they have the points for it
            # if they don't have the points, return False.
            self.update_points()
            print(f'Your score is:{self.score}')
            if self.score > 0:
                choice = input('Would you like to play again (y,n)')
                if (choice == "n"):
                    self.keep_playing = False
