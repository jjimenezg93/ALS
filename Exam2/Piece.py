__author__ = 'Julián'

import os
import pickle

class Piece:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return "id: {0}, name: {1}".format(self.__id, self.__name)

piece1 = Piece(1, "p1")
piece2 = Piece(2, "p2")
piece3 = Piece(3, "p3")

dictPieces = {piece1.id:piece1, piece2.id:piece2, piece3.id:piece3}

def save(file, data):
    f = open(file, "wb")
    for i in dictPieces.items():
        pickle.dump(dictPieces, f)

def load(file):
    with open(file, "rb") as f:
        pieces = pickle.load(f)
        for i in pieces:
            print(pieces[i].name)

save("data.txt", dictPieces)
load("data.txt")