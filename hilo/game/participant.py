import random


class Participant:
    '''
    The participant is a class that will be responsible for shuffling,
    calculating the points of each round and checking if the player can play.

    attributes:
        dice_rolls[] is a list of the points earned in one throw.
    '''

    def __init__(self):
        self.card_value = 1
        self.card_new_value = 0
        self.can_play_result = True

    def shuffle(self):
        self.card_new_value = random.randint(1, 13)
        self.card_value = random.randint(1, 13)

    def calculate_points(self, guess):
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
