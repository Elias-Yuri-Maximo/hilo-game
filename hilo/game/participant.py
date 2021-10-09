import random


class Participant:
    """
    The participant is a class that will be responsible for shuffling,
    calculating the points of each round and checking if the player can play.

    attributes:
        dice_rolls[] is a list of the points earned in one throw.
    """

    def __init__(self):
        """
        Participant class initialization.

        Parameters
            self: The current instance of Participant

        Class attributes
            card_value (int),
            card_new_value (int): Randints between 1 and 13 inclusive. Actual randint
                                  will be generated during the shuffle() method below.
            can_play_result (boolean): See can_play() method below. Here, default value is assigned.
                                       True by default, sets to False if participant's score
                                       becomes negative. When True, game is allowed to continue.
                                       When False, game ends.
        """
        self.card_value = 1 # arbitrary initialization value
        self.card_new_value = 0 # arbitrary initialization value
        self.can_play_result = True

    def shuffle(self):
        """ Generates two random numbers

        Paremeters
            self (Participant): the current Participant instance

        """

        # These are the "cards"
        # card_value will be shown to player, card_new_value will not until they guess
        self.card_value = random.randint(1, 13)
        self.card_new_value = random.randint(1, 13)


    def calculate_points(self, guess):
        """ Determines, based on user's guess, whether to add 100 points or subtract 75 from score

        Parameters
            self (Participant): The current Participant instance
            guess (string): The user's guess. Either "h" for higher or "l" for lower.

        Returns
            points: The number of points to add to participant's running total.
                    This number may be negative, effectively subtracting from score.

        """

        points = 0 # default value assigned to avoid 'referenced before assignment' errors

        if guess == "h":
            if self.card_new_value >= self.card_value:
                points = 100
            else:
                points = -75

        elif guess == "l":
            if self.card_new_value < self.card_value:
                points = 100
            else:
                points = -75


        return points

    def can_play(self, score):
        if score <= 0:
            self.can_play_result = False

        return self.can_play_result
