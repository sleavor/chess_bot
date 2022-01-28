#Import libraries
import chess.pgn
import os

#Open data file Carlsen.pgn
cur_path = os.path.dirname(__file__)
# EDIT PATH TO YOUR DATA #
data_path = '../Data/Carlsen.pgn'
path=os.path.join(cur_path, data_path)
path=os.path.abspath(path)
data = open(path)

while True:
    try:
        game = chess.pgn.read_game(data)
        print(game.headers["Event"])
    except AttributeError:
        break