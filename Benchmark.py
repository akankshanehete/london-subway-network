from ShortestPath import ShortestPath
from Graph import Graph
from Itinerary import Itinerary
from Graph_Algorithms.A_star import A_star
from KPIs.ExecutionTime import ExecutionTime
from KPIs.Compares import Compares
from KPIs.Visited import Visited
from KPIs.CpuTime import CpuTime
from KPIs.Inserts import Inserts
from Test import Test
from Plotter import Plotter
import random


class Benchmark():

    def __init__(self, graph: Graph, algos, stations_traversed: list, repetitions=0):
        self.graph = graph
        self.algos = algos
        self.stations_traversed = stations_traversed
        self.repetitions = repetitions

    def plot_bar(self):
        print(self.do_bench())

    def plot_line(self):
        line_graph = Plotter()
        values = self.do_bench()

    def do_bench(self):
        bench = self.get_bench()
        results = {}
        exec = {}
        cpu = {}
        compares = {}
        inserts = {}
        visited = {}
        for algo in self.algos:
            exec[algo.get_name()] = []
            cpu[algo.get_name()] = []
            compares[algo.get_name()] = []
            inserts[algo.get_name()] = []
            visited[algo.get_name()] = []
        if self.repetitions > 0:
            # Execution time KPIs
            for algo in self.algos:
                counter = 1
                case = bench[0]
                for kpi in [ExecutionTime(), CpuTime()]:
                    test = Test(self.graph, algo, kpi, case['from_node_id'], case['to_node_id'])
                    if counter == 1:
                        for i in range(case['num']):
                            exec[algo.get_name()].append(test.find_measurement())
                    elif counter == 2:
                        for i in range(case['num']):
                            cpu[algo.get_name()].append(test.find_measurement())
                    counter += 1
            results['Execution Time'] = exec
            results['CPU Time'] = cpu
        elif self.repetitions == 0:
            # Iterative KPIs
            for algo in self.algos:
                for case in bench:
                    counter = 1
                    for kpi in [Compares(), Inserts(), Visited()]:
                        test = Test(self.graph, algo, kpi, case['from_node_id'], case['to_node_id'])
                        if counter == 1:
                            compares[algo.get_name()].append({'traversed': case['num'], 'value': test.find_measurement()})
                        elif counter == 2:
                            inserts[algo.get_name()].append({'traversed': case['num'], 'value': test.find_measurement()})
                        elif counter == 3:
                            visited[algo.get_name()].append({'traversed': case['num'], 'value': test.find_measurement()})
                        counter += 1
            results['Compares'] = compares
            results['Inserts'] = inserts
            results['Visited'] = visited
        return results

    def get_bench(self):
        bench = []
        done = {}
        counter = 0
        for i in self.stations_traversed:
            done[i] = 0
        all_nodes = self.graph.all_nodes
        for i in all_nodes:
            for j in all_nodes:
                paths = Itinerary(self.graph, i, j, A_star())
                num = self.stations_traversed[0]
                if self.repetitions > 0 and paths.find_shortest_path()[1] == num:
                    num = self.repetitions
                    bench.append({'num': num, 'from_node_id': i, 'to_node_id': j})
                    return bench
                for k in range(len(self.stations_traversed)):
                    num = self.stations_traversed[k]
                    if paths.find_shortest_path()[1] == num and done[num] != 1:
                        bench.append({'num': num, 'from_node_id': i, 'to_node_id': j})
                        done[num] = 1
                        counter += 1
                    if counter == len(self.stations_traversed):
                        return bench
        return bench
