from Graph_builder import Graph_builder
from Graph import Graph
from Csv_reader import Csv_reader
# from Metric_Extractor import Metric_Extractor
from Itinerary import Itinerary
from Graph_Algorithms.Dijkstra import Dijkstra
from Graph_Algorithms.A_star import A_star
# from Graph_Algorithms.Priority_Queue import PriorityQueue
# from ShortestPath import ShortestPath
from Test import Test
# from KPIs.CpuTime import CpuTime
# from KPIs.ExecutionTime import ExecutionTime
# from KPIs.Visited import Visited
# from KPIs.Inserts import Inserts
from KPIs.Compares import Compares
# from Benchmark import Benchmark
# from Plotter import Plotter

csv_reader = Csv_reader()

london_sub_graph = Graph_builder(csv_reader, Graph())
london_sub_graph.create_station_nodes('_dataset/london.stations.csv')
london_sub_graph.create_connections('_dataset/london.connections.csv')
# london_sub_graph.graph.print_all_connections()
# london_sub_metrics = Metric_Extractor(london_sub_graph.graph)
# print('Average Node Degree: '+str(london_sub_metrics.get_avg_degree()))
# print('Total Edge Count: '+str(london_sub_metrics.get_edge_count()))
# print('Total Node Count: '+str(london_sub_metrics.get_node_count()))
# london_sub_metrics.plot_node_dist()

# creating an itinerary from station 36 to station 289
itinerary = Itinerary(london_sub_graph.graph, 1, 30, A_star())
itinerary.print_itinerary()
test = Test(london_sub_graph.graph, A_star(), Compares(), 1, 2)
print("A* Compares = ", test.find_measurement())
test = Test(london_sub_graph.graph, Dijkstra(), Compares(), 1, 2)
print("Dijkstra Compares = ", test.find_measurement())
# benchmark = Benchmark(london_sub_graph.graph, [Dijkstra(), A_star()], [15], 3)
# results = benchmark.do_bench()
# print(results)
# result = results['Execution Time']
# plot_kpi = Plotter()
# plot_kpi.bar('Execution Time', 15, result)

# test_graph1 = Graph()
# test_graph1.add_edge(1, 2, 2, 'red')
# test_graph1.add_edge(1, 6, 1, 'green')
# test_graph1.add_edge(1, 5, 3, 'blue')
# test_graph1.add_edge(1, 10, 2, 'blue')
# test_graph1.add_edge(2, 3, 4, 'red')
# test_graph1.add_edge(2, 6, 1, 'green')
# test_graph1.add_edge(3, 4, 2, 'red')
# test_graph1.add_edge(4, 5, 4, 'purple')
# test_graph1.add_edge(4, 7, 2, 'purple')
# test_graph1.add_edge(6, 8, 2, 'yellow')
# test_graph1.add_edge(8, 9, 3, 'blue')
# test_graph1.add_edge(9, 10, 2, 'blue')

# metric = Metric_Extractor(test_graph1)
# print("Node count = ", metric.get_node_count())
# print("Edge count = ", metric.get_edge_count())
# print("Degree node 1 = ", metric.get_degree(1))
# print("Average degree = ", metric.get_avg_degree())
