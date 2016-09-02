#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""game.py

Control logic for the Gomoku game and main class for the program.
"""

from gomoku_board import GomokuBoard
from itertools import cycle
from random import randint


def player_input(board, player):

    print(board)
    while True:
        try:
            raw = input("Place {} on which x,y? ".format(board.stones[player]))
            pos = tuple(int(i) for i in raw.split(","))
            valid_pos = all(type(i) is int and (0 <= i <= 14) for i in pos)
            if len(pos) != 2 or not valid_pos or not board.is_empty_space(pos):
                raise ValueError
            break
        except ValueError:
            print("Invalid input.", end=' ')

    return pos


def random_input(board):

    pos = [randint(0, 14) for _ in range(2)]
    while not board.is_empty_space(pos):
        pos = [randint(0, 14) for _ in range(2)]

    return pos


def game_loop(board, mode=None):

    if mode == 'exit':
        raise SystemExit

    turn = cycle([1, -1])
    while not board.victory():
        player = next(turn)
        if player == -1 and mode == 'random':
            pos = random_input(board)
        else:
            pos = player_input(board, player)
        board.place_stone(player, pos)

    message = "\nDraw!" if board.draw() else "\nWinner: {}".format(
        board.stones[player])

    print(board, message)
    board.clear()


def main():

    choices = {
        "0": dict(desc="quit", mode='exit'),
        "1": dict(desc="human x human", mode='two_player'),
        "2": dict(desc="human x computer (random)", mode='random'),
    }

    while True:
        for key in sorted(choices.keys()):
            print("[{}] {}".format(key, choices[key]["desc"]))
        option = input("Choice: ")
        if option not in choices.keys():
            print("Invalid input.")
        else:
            game_loop(GomokuBoard(15), choices[option]['mode'])


if __name__ == '__main__':
    main()
