__author__ = 'Rene'

from piece import piece
from PIL import Image

PIECE_WIDTH = 280
PIECE_HEIGHT = 930

class Collection:

    def __init__(self):
        self.num = 0
        self.pieces = []

    # add resized pieces in a list into collection
    def add(self, list):
        for piece in list:
            self.pieces.append(piece)
            self.num = self.num + 1

    # get pieces
    def get(self):
        return self.pieces

    def getNum(self):
        return self.num
    # merge pieces side by side in collection, return an image
    def getMergePieces(self):
        collect_width = self.num * PIECE_WIDTH
        collect_height = PIECE_HEIGHT
        collect = Image.new('RGB', (collect_width, collect_height))
        i = 0
        for piece in self.pieces:
            image = piece.getImage()
            collect.paste(image, box = (PIECE_WIDTH * i, 0))
            i = i + 1
        return collect

    # merge avg_pieces in collection
    def getMergeAvgPieces(self):
        collect_width = self.num * PIECE_WIDTH
        collect_height = PIECE_HEIGHT
        collect = Image.new('RGB', (collect_width, collect_height))
        i = 0
        for piece in self.pieces:
            image = piece.drawImage(piece.avgColor())
            collect.paste(image, box = (PIECE_WIDTH * i, 0))
            i = i + 1
        return collect

    # merge most_frequent_pieces in collection
    def getMergeFrequentPieces(self):
        collect_width = self.num * PIECE_WIDTH
        collect_height = PIECE_HEIGHT
        collect = Image.new('RGB', (collect_width, collect_height))
        i = 0
        for piece in self.pieces:
            image = piece.drawImage(piece.mostFrequentColor())
            collect.paste(image, box = (PIECE_WIDTH * i, 0))
            i = i + 1
        return collect

     # merge kmeans_pieces in collection
    def getKmeansPieces(self):
        collect_width = self.num * PIECE_WIDTH
        collect_height = PIECE_HEIGHT
        collect = Image.new('RGB', (collect_width, collect_height))
        i = 0
        for piece in self.pieces:
            colors = piece.kmeansColor()
            image = piece.drawKmeansImage(colors)
            collect.paste(image, box = (PIECE_WIDTH * i, 0))
            i = i + 1
        return collect