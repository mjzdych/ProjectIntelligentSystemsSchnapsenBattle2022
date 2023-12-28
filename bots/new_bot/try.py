
# Import the API objects
from api import State, util
import random


class Bot:
    # How many samples to take per move
    __num_samples = -1
    # How deep to sample
    __depth = -1

    def __init__(self, num_samples=4, depth=8):
        self.__num_samples = num_samples
        self.__depth = depth

    def get_move(self, state):

        # See if we're player 1 or 2
        player = state.whose_turn()

        # Get a list of all legal moves
        moves = state.moves()

        # Sometimes many moves have the same, highest score, and we'd like the bot to pick a random one.
        # Shuffling the list of moves ensures that.
        random.shuffle(moves)

        best_score = float("-inf")
        best_move = None

        scores = [0.0] * len(moves)

        for move in moves:
            for s in range(self.__num_samples):

                # If we are in an imperfect information state, make an assumption.

                sample_state = state.make_assumption() if state.get_phase() == 1 else state

                score = self.evaluate(sample_state.next(move), player)

                if score > best_score:
                    best_score = score
                    best_move = move

        return best_move  # Return the best scoring move
