import math
import random

# given a list of y values, this function plots it on the console in a visualizable way
class Plotter:
    def __init__(self):
        pass

    def plot (self, y: list, title = '', x_title = '', y_title = ''):
        print('\t\t'+title)
        input_list=y
        input_max = max(*input_list)
        s = len(str(input_max))
        f = '%%0%dd' % s
        g = '%%0%dd' % len(str(len(input_list)))
        graph_dict = [['.'] * (len(input_list) * 4 + s) for _ in range(input_max + 2)]
        for x, y in enumerate(graph_dict): y[:s] = f % (input_max - x);y[s] = '|'
        graph_dict[-2][:] = ' ' * s + '+' + '-' * (len(input_list) * 4 - 1)
        graph_dict[-1][:s + 2] = ' ' * (s + 2)
        graph_dict[-1][s + 2:] = ['%-4s' % (g % -~x) for x in range(len(input_list))]

        def r(n, y, x, z, o):
            for v in graph_dict[input_max - n + (n - y) * z // 4 + 1:input_max]: v[x * 4 + s + o] = '|'

        for x, y in enumerate(input_list):
            graph_dict[input_max - y][x * 4 + s + 2] = 'o'
            for v in graph_dict[input_max - y + 1:input_max]: v[x * 4 + s + 2] = '|'
            if x == len(input_list) - 1: break
            n = input_list[x + 1]
            r(n, y, x, 3, 3)
            r(n, y, x, 2, 4)
            r(n, y, x, 1, 5)
        print('\n'.join(map(''.join, graph_dict)))
        print('\t\t'+x_title)
        if y_title != '':
            print('y axis title: '+ y_title)

