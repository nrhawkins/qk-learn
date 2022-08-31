from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import argparse
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))


class Fractal(ABC):

    DEFAULTS = {"starting_point": Point(0, 0), "n": 100,
                "fractals": ("barnsley", "mandlebrot", "sierpinski")}

    def __init__(self):
        self.x = [self.DEFAULTS["starting_point"].x]
        self.y = [self.DEFAULTS["starting_point"].y]
        self.n = self.DEFAULTS["n"]

    @abstractmethod
    def transform(self):
        pass

    def draw(self):
        self.transform()
        plt.plot(self.x, self.y)
        plt.show()


class Mandelbrot(Fractal):

    def __init__(self, n):
        super().__init__()
        self.x = [1, 2, 3]
        self.y = [1, 2, 3]
        self.n = n

    def transform(self):
        print("transform")


class BarnsleyFern(Fractal):

    def __init__(self):
        super().__init__()

    def transform(self):
        print("transform")


class SierpinskiTriangle(Fractal):

    def __init__(self):
        super().__init__()

    def transform(self):
        print("transform")


parser = argparse.ArgumentParser()
parser.add_argument("fractal", help="fractal to draw", type=str)
parser.add_argument("n", help="number of points to draw", type=int)
args = parser.parse_args()

if args.fractal == "mandelbrot":
    f = Mandelbrot(args.n)
    f.draw()
    print("mandelbrot")
    print("point: ", Fractal.DEFAULTS['starting_point'])
