import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# given a list of y values, this function plots it using matplotlib in a visualizable way
class Plotter:
    def __init__(self):
        pass

    def plot (self, y: list, title = '', x_title = '', y_title = ''):
        plt.plot(y)
        plt.ylabel(y_title)
        plt.title(title)
        plt.xlabel(x_title)
        plt.show()


    def line(self, kpi, algos: list, result):
        names = []
        for algo in algos:
            names.append(algo.get_name())
        points = []
        x = []
        y = []
        for i in range(len(names)):
            for j in result[names[i]]:
                points.append([j['traversed'], j['value']])
            points.sort()
            for p in points:
                x.append(p[0])
                y.append(p[1])
            print(x)
            print(y)
            plt.plot(x, y, label=names[i])
            points.clear()
            x.clear()
            y.clear()
        plt.xlabel('Stations Traversed')
        plt.ylabel(kpi)
        plt.title("Benchmarking " + kpi)
        plt.legend()
        plt.show()
        # fig.savefig('outputs/sort_comparisons_small.pdf')

