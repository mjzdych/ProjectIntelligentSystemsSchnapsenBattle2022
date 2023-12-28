#!/usr/bin/env python
"""
This is a bot that applies propositional logic reasoning to determine its strategy.
The strategy it uses is determined by what is defined in load.py. Here it is to always
pick a Jack to play whenever this is a legal move.

It loads general information about the game, as well as the definition of a strategy,
from load.py.
"""

from api import State, util
import random
from bots.new_bot import load
from bots.queen_strategy.kb import KB, Boolean
from api import Deck


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()
        random.shuffle(moves)

        for move in moves:
            if not self.kb_consistent(state, move):  # jack strategy
                return move
            elif not self.kb_consistent3(state, move):  # queen strategy
                return move
            else:
                return random.choice(moves)

                # elif not self.kb_consistent2(state, move):
                #     return move
                # elif not self.kb_consistent3(state, move):
                #     return move
                # elif not self.kb_consistent4(state, move):
                #     return move

        # If no move that is entailed by the kb is found, play random move

    # Note: In this example, the state object is not used,
    # but you might want to do it for your own strategy.
    def kb_consistent(self, state, move):
        # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        kb = KB()

        # Add general information about the game
        load.general_information(kb)

        # Add the necessary knowledge about the strategy
        load.jack_strategy(kb)

        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        kb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
        return kb.satisfiable()

    def kb_consistent1(self, state, move):
        # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        kb = KB()

        # Add general information about the game
        load.general_information(kb)

        # Add the necessary knowledge about the strategy

        load.ace_strategy(kb)
        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        kb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
        return kb.satisfiable()

    def kb_consistent2(self, state, move):
        # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        kb = KB()

        # Add general information about the game
        load.general_information(kb)

        # Add the necessary knowledge about the strategy

        load.ten_strategy(kb)
        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        kb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
        return kb.satisfiable()

    def kb_consistent3(self, state, move):
        # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        kb = KB()

        # Add general information about the game
        load.general_information(kb)

        # Add the necessary knowledge about the strategy

        load.queen_strategy(kb)
        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        kb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
        return kb.satisfiable()

    def kb_consistent4(self, state, move):
        # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        kb = KB()

        # Add general information about the game
        load.general_information(kb)

        # Add the necessary knowledge about the strategy

        load.king_strategy(kb)
        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        kb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
        return kb.satisfiable()


def empty(n):
    """
    :param n: Size of the matrix to return
    :return: n by n matrix (2D array) filled with 0s
    """
    return [[0 for i in range(n)] for j in range(n)]


def best_non_trump_card(state):
    """
    :param state: A state object
    :return: A move tuple representing the highest rank non-trump move available
    """

    # All legal moves
    moves = state.moves()
    chosen_move = moves[0]

    lowest_suit_moves = []

    # Get all moves which are not trump suit or matching the suit of the enemy's card
    for move in moves:

        if move[0] is not None and util.get_suit(move[0]) != state.get_trump_suit():
            lowest_suit_moves.append(move)

    if len(lowest_suit_moves) == 0:
        lowest_suit_moves = moves

    # Get move with highest rank available, of the subset that we've narrowed down so far
    for move in lowest_suit_moves:
        if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
            chosen_move = move

    return chosen_move
