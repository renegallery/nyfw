__author__ = 'Rene'
from collections import namedtuple
from math import sqrt
from PIL import Image
import random


Point = namedtuple('Point', ('coords', 'n', 'ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))

def get_points(img):
    points = []
    w, h = img.size
    for count, color in img.getcolors(w * h):
        points.append(Point(color, 3, count))
    return points

rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))

def colorz(image, n=3):
    img = image
    img.thumbnail((200, 200))
    w, h = img.size

    points = get_points(img)
    clusters = kmeans(points, n, 1)
    rgbs = [map(int, c.center.coords) for c in clusters]

    pix = img.load()
    pixel1 = pix[w/2, h/3]
    pixel1 = Point(pixel1[:3], 3, 1)
    pixel2 = Point(pix[w / 2, h * 2 / 3][:3], 3, 1)

    # which cluster does this 2 points belong to
    c1 = pointCluster(pixel1, clusters)
    c2 = pointCluster(pixel2, clusters)
    rgbs1 = map(int, c1.center.coords)
    rgbs2 = map(int, c2.center.coords)

    return [rgbs1, rgbs2]

def euclidean(p1, p2):
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))

def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)

def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    return clusters

def pointCluster(pixel, clusters):
    c = [Point(c.center.coords, 3, 1) for c in clusters]
    d = []
    d.append(euclidean(pixel, c[0]))
    d.append(euclidean(pixel, c[1]))
    d.append(euclidean(pixel, c[2]))
    idx = d.index(min(d))
    return clusters[idx]
