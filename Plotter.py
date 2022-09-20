import math
import random
import matplotlib.pyplot as plt

# given a list of y values, this function plots it using matplotlib in a visualizable way
class Plotter:
    def __init__(self):
        pass

    def plot (self, y: list, title = '', x_title = '', y_title = ''):
        plt.figure(dpi=150)
        plt.plot(y)
        plt.ylabel(y_title)
        plt.suptitle(title)
        plt.xlabel(x_title)
        plt.show()
