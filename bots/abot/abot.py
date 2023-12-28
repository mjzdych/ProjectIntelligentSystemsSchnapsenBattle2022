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

    def kb_consistent(self, state, move):
        # type: (State, move) -> bool

        kb = KB()

        load.general_information(kb)

        load.jack_strategy(kb)

        index = move[0]

        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

    def kb_consistent3(self, state, move):
        # type: (State, move) -> bool

        kb = KB()

        load.general_information(kb)

        load.queen_strategy(kb)

        index = move[0]

        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()