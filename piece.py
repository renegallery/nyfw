__author__ = 'Rene'

from PIL import Image
from kmeans import colorz

PIECE_WIDTH = 280
PIECE_HEIGHT = 930
WRITE_SIZE = (PIECE_WIDTH, PIECE_HEIGHT)

class piece:

    def __init__(self):
        self.image = Image.new('RGB', (0,0))

    def __init__(self, image):
        self.image = image.resize( (PIECE_WIDTH, PIECE_HEIGHT), Image.BILINEAR )

    # show image of piece
    def showImage(self):
        self.image.show()

    # get image of piece
    def getImage(self):
        return self.image

    # get the average color of this piece
    def avgColor(self):
        color_tuple = [None, None, None]
        for channel in range(3):
            pixels = self.image.getdata(band = channel)
            values = []
            for pixel in pixels:
                values.append(pixel)
            color_tuple[channel] = sum(values) / len(values)
        return tuple(color_tuple)

    # get the most frequent color of this piece
    def mostFrequentColor(self):
        image = self.image
        w, h = image.size
        pixels = image.getcolors(w * h)

        most_frequent_pixel = pixels[0]

        for count, colour in pixels:
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count, colour)

        return most_frequent_pixel[1]

    # get the average image of this piece
    def drawImage(self, rgb):
        im = Image.new("RGB", WRITE_SIZE, rgb)
        return im

    # write the average color to a image in WRITE_SIZE
    def saveImage(rgb, filename):
        im = Image.new("RGB", WRITE_SIZE, rgb)
        im.save(filename)

    # get the 3-means color
    def kmeansColor(self):
        image = self.image
        cluster = colorz(image, n = 3)
        return cluster

    # get the 3 dominant color image
    def drawKmeansImage(self, color_list):
        im = []
        for i in range(2):
            im.append(Image.new("RGB", WRITE_SIZE, tuple(color_list[i])))
        im1 = im[0]
        im1.paste(im[1], (0, PIECE_HEIGHT / 2))
        #im1.paste(im[2], (0, PIECE_HEIGHT * 2 / 3))
        return im1

    # write the average color to a image in WRITE_SIZE
    def saveKmeansImage(rgb, filename):
        im = []
        for i in range(3):
            im.append(Image.new("RGB", WRITE_SIZE, tuple(color_list[i])))
        im1 = im[0]
        im1.paste(im[1], (0, PIECE_HEIGHT / 2))
        #im1.paste(im[2], (0, PIECE_HEIGHT * 2 / 3))
        im1.save(filename)
