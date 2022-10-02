from typing import List
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
import random

Algorithm = ShortestPath
Station = int


class Benchmark:

    def __init__(self, graph: Graph, algos: List[Algorithm],
                 stations_traversed: List[Station], repetitions=0):
        self.graph = graph
        self.algos = algos
        self.stations_traversed = stations_traversed
        self.repetitions = repetitions

    # executes bench(es) for each algorithm
    def do_bench(self):
        bench = self.get_bench()
        results = {}
        exec_time = {}
        cpu_time = {}
        compares = {}
        inserts = {}
        visited = {}
        for algo in self.algos:
            exec_time[algo.get_name()] = []
            cpu_time[algo.get_name()] = []
            compares[algo.get_name()] = []
            inserts[algo.get_name()] = []
            visited[algo.get_name()] = []
        # if input indicates execution time KPI,
        # execute algorithms using the bench for many repetitions
        if self.repetitions > 0:
            for algo in self.algos:
                counter = 1
                case = bench[0]
                for kpi in [ExecutionTime(), CpuTime()]:
                    test = Test(self.graph, algo, kpi,
                                case['from_node_id'], case['to_node_id'])
                    if counter == 1:
                        for i in range(case['num']):
                            exec_time[algo.get_name()].append(
                                test.find_measurement())
                    elif counter == 2:
                        for i in range(case['num']):
                            cpu_time[algo.get_name()].append(
                                test.find_measurement())
                    counter += 1
            results['Execution Time'] = exec_time
            results['CPU Time'] = cpu_time
        # if input indicates iterative KPI, execute algorithms for each bench
        elif self.repetitions == 0:
            for algo in self.algos:
                for case in bench:
                    counter = 1
                    for kpi in [Compares(), Inserts(), Visited()]:
                        test = Test(self.graph, algo, kpi,
                                    case['from_node_id'], case['to_node_id'])
                        val = {'traversed': case['num'],
                               'value': test.find_measurement()}
                        if counter == 1:
                            compares[algo.get_name()].append(val)
                        elif counter == 2:
                            inserts[algo.get_name()].append(val)
                        elif counter == 3:
                            visited[algo.get_name()].append(val)
                        counter += 1
            results['Compares'] = compares
            results['Inserts'] = inserts
            results['Visited'] = visited
        return results

    # creates bench(es) based on input parameters
    # repetitions = 0 indicates visited, inserts, or compares KPI
    # repetitions > 0 indicates execution time or CPU time KPI
    def get_bench(self):
        bench = []
        done = {}
        counter = 0
        for i in self.stations_traversed:
            done[i] = 0
        all_nodes = self.graph.all_nodes
        # shuffle all node keys
        random_nodes = list(all_nodes.keys())
        random.shuffle(random_nodes)
        # find a path (bench) that traverses specified number of stations
        for i in random_nodes:
            for j in random_nodes:
                paths = Itinerary(self.graph, i, j, A_star())
                num = self.stations_traversed[0]
                # if input arguments indicate an execution time KPI,
                # return a single bench
                if self.repetitions > 0 and paths.find_shortest_path(
                )['stations traversed'] == num:
                    num = self.repetitions
                    bench.append({'num': num,
                                  'from_node_id': i,
                                  'to_node_id': j})
                    return bench
                # if input arguments indicate an interative KPI,
                # return multiple benches
                for k in range(len(self.stations_traversed)):
                    num = self.stations_traversed[k]
                    if paths.find_shortest_path()['stations traversed'] \
                            == num and done[num] != 1:
                        bench.append({'num': num,
                                      'from_node_id': i, 'to_node_id': j})
                        done[num] = 1
                        counter += 1
                    if counter == len(self.stations_traversed):
                        return bench
        return bench
