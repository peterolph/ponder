import random
from insects.tuples import Move, Token

class AI(object):
    def choose_move(self, m, p):
        places = [(Token(p,token),None,destination) for token in m.colour_hand(p) for destination in m.colour_places(p)]
        moves = [(None, source, destination) for source,destinations in m.colour_moves(p).items() for destination in destinations]
        everything = places + moves
        return Move(*random.choice(everything))