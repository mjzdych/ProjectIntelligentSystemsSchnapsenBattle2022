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
from . import load
from .kb import KB, Boolean, Integer
from api import Deck


class Bot:
    def __init__(self):
        pass


    def highest_trump_suit_card(self, state):
        moves = state.moves()
        chosen_move = moves[0]
        moves_same_suit = []

        # Get all moves of the same suit as the opponent's played cardk
        for index, move in enumerate(moves):
            if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
                moves_same_suit.append(move)
        moves_same_suit.sort(key=lambda a: a[0])  # we are sorting the list in the ascending order
        if len(moves_same_suit) > 0:
            chosen_move = moves_same_suit[0]
            return chosen_move


    def highest_rank_available(self, state):
        moves = state.moves()
        chosen_move = moves[0]
        for index, move in enumerate(moves):
            if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                chosen_move = move
        return chosen_move

    def knowledge_base_non_trump(self, state):

        # All legal moves
        moves = state.moves()
        moves_not_trump_suit = []

        # Get all non-trump suit moves available
        for index, move in enumerate(moves):

            if move[0] is not None and Deck.get_suit(move[0]) != state.get_trump_suit():
                moves_not_trump_suit.append(move)

        list_of_non_trump_moves = moves_not_trump_suit

        moves = state.moves()

        random.shuffle(moves)

        for move in moves:
            if move in list_of_non_trump_moves:
                if not self.kb_consistent(state, move):
                    return move
                elif not self.kb_consistent3(state, move):
                    return move
                elif not self.kb_consistent4(state, move):
                    return move
                elif not self.kb_consistent2(state, move):
                    return move
                elif not self.kb_consistent1(state, move):
                    return move
            else:
                return self.highest_trump_suit_card(state)


    def get_move(self, state):

        opponents_card = state.get_opponents_played_card()
        moves = state.moves()

        random.shuffle(moves)

        if opponents_card is None:  # when our bot is playing

            return self.knowledge_base_non_trump(state)

        else:   # when opponent is playing

            return self.highest_rank_available(state)

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

    def kb_consistent1(self, state, move):
        # type: (State, move) -> bool


        kb = KB()

        load.general_information(kb)

        load.ace_strategy(kb)

        index = move[0]


        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

    def kb_consistent2(self, state, move):
        # type: (State, move) -> bool

        kb = KB()

        load.general_information(kb)


        load.ten_strategy(kb)

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

    def kb_consistent4(self, state, move):
        # type: (State, move) -> bool

        kb = KB()

        load.general_information(kb)

        load.king_strategy(kb)

        index = move[0]

        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)


        return kb.satisfiable()

