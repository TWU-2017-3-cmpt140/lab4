#****************************************************************
# CMPT 140 Lab #4
#
# Coin flip experiment
#
# Coin class definition
#****************************************************************
import random
class Coin:
    """
    fields:
        state - integer; let 0=head and 1=tail
        p - the probablity of getting a head on a coin flip
    """

    #************************************************************
    # Class initializer
    # this function creates a coin object
    #
    # input: initial state
    def __init__(self, state):
       self.state = state
       p = 0.5 # if the coin is weighted, p will not be 0.5

    #************************************************************
    # return a string representation of this Coin instance
    #
    # return: str
    def __str__(self):
       return "head" if self.state==0 else "tail"

    #************************************************************
    # flip the coin
    #
    def flip(self):
       if random.randrange(0,2)==1:
          self.state = abs(self.state-1)
