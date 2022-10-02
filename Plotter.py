import matplotlib
import matplotlib.pyplot as plt
import platform
from typing import List

if platform.system() == 'Darwin':
    matplotlib.use('MacOSX')
else:
    matplotlib.use('TkAgg')

Num = int
KPI = str
Traversed = int
Result = dict


class Plotter:
    def __init__(self):
        pass

    # given a list of y values, this function plots it using matplotlib
    @staticmethod
    def plot(y: List[Num], title='', x_title='', y_title=''):
        plt.plot(y)
        plt.ylabel(y_title)
        plt.suptitle(title)
        plt.xlabel(x_title)
        plt.show()

    # plots a bar graph for execution time KPIs
    # x-axis = time, y-axis = instances
    @staticmethod
    def bar(kpi: KPI, traversed: Traversed, result: Result):
        fig, ax = plt.subplots(len(result.keys()), sharex=True, sharey=True)
        all_values = []
        for values in result.values():
            all_values += values
        scope = []
        counter = round(min(all_values), 1) - 0.2
        ceiling = round(max(all_values), 1) + 0.2
        # define scope
        while counter <= ceiling:
            scope.append(format(counter, '.1f'))
            counter += 0.1
        vals = {}
        points = []
        y = []
        counter = 0
        for algo in result.keys():
            # initialize all values in the scope as 0
            for i in scope:
                vals[i] = 0
            # count all results and increment values accordingly
            for point in result[algo]:
                temp = format(round(point, 1), '.1f')
                vals[temp] += 1
            # convert val dictionary to points list
            for val in vals.items():
                points.append([val[0], val[1]])
            points.sort()
            for point in points:
                y.append(point[1])
            ax[counter].bar(scope, y, color='blue', width=0.2)
            # clear all values from vals, points, and y for next algo
            vals.clear()
            points.clear()
            y.clear()
            counter += 1
        plt.suptitle('Benchmarking ' + kpi + ', Stations Traversed = '
                     + str(traversed))
        names = ', '.join(result.keys())
        plt.xlabel(kpi + ' for ' + names + ' in ms')
        plt.show()

    @staticmethod
    def line(kpi: KPI, result: Result):
        points = []
        x = []
        y = []
        for algo in result.keys():
            # create a list of points
            for point in result[algo]:
                points.append([point['traversed'], point['value']])
            # sort points in place before separating x and y
            points.sort()
            # separate x and y values from each point
            for p in points:
                x.append(p[0])
                y.append(p[1])
            plt.plot(x, y, label=algo)
            # clear all values for points, x, and y for next algo
            points.clear()
            x.clear()
            y.clear()
        plt.xlabel('Stations Traversed')
        plt.ylabel(kpi)
        plt.title('Benchmarking ' + kpi)
        plt.legend()
        plt.show()

    @staticmethod
    def line2(result: list):
        points = []
        x = []
        y = []
        for point in result:
            points.append([point['nodes'], point['average']])
            # sort points in place before separating x and y
        points.sort()
        # separate x and y values from each point
        for p in points:
            x.append(p[0])
            y.append(p[1])
        plt.plot(x, y)
        plt.xlabel('Number of Nodes in Graph')
        plt.ylabel('Execution Time in ms')
        plt.title('Execution Time of Transportation Islands')
        plt.show()
