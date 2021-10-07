import random


# TODO: Define the Thrower class here.
class Participant: 
     '''
    The participant is a class that will be responsible for shuffling, 
    calculating the points of each round and checking if the player can play. 

    attributes:
        dice_rolls[] is a list of the points earned in one throw.
    '''
    def __init__(self):

        '''
        The constructor 
        Args: Self
        '''
        cards = []
    def shuffle(self):
        '''
        When called will generate a a random list of numbers between 1-13 
        the list was already declared, so it should only append to it (list.append(item))

        '''
        pass

    def calculate_points(self):
        '''
        Gets the results and calculates the total points 
        then returns the sum of the results 
        Args: self
        '''
        pass
    
    def can_play(self):
        '''
        Checks if the player can play (if the result is different then 0)
        and returns a boolean value (true or false), 
        Args: self
        '''
        pass