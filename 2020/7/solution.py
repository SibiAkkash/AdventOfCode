from typing import List, Dict, Tuple
from graph import Graph
from collections import deque

Node = str
Weight = int
ParsedRule = List[Tuple[Node, Node, Weight]]

def parse_rule(rule: str) -> ParsedRule:
	# sample rule: shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
	parts = rule.split("bags contain")
	
	# get outer and inner bags for graph
	outer_bag = parts[0].strip()
	
	# this type of bag cannot contain any bag inside it 
	if parts[1].strip().startswith("no"):
		return [(outer_bag, None, 0)]

	inner = parts[1].split(',')
	# store bag type and no of bags, for each inner bag type
	inner_bags = []
	for bag in inner:
		# 3 bright blue bags -> ['3', 'bright', 'blue', 'bags']
		components = bag.split()
		# we don't need that last 'bags' word.
		components.pop()
		# get no of bags
		count = int(components[0])
		# get inner bag type
		bag_type = ' '.join(components[1:])
		inner_bags.append((outer_bag, bag_type, count))

	return inner_bags	


def make_graph(rules: List[str]) -> Graph:
	# each parsed rule is a list of edges of a directed weighted graph
	# add each edge (rule) to the graph, build the graph from the edges
	# the problem is to find the number of bag colours that can eventually contain a shiny gold bag
	# which is to ask how many nodes in the graph have a path to the target node (shiny gold bag) 
	bag_types = set()
	parsed_rules = []
	for rule in rules:
		edges = parse_rule(rule)
		for edge in edges:
			# print(edge)
			bag_type_1, bag_type_2 = edge[0], edge[1]
			# add the different bag_types to a set
			bag_types.add(bag_type_1)
			# this could be and edge that goes no where, that is this bag_type cannot contain any bags
			if bag_type_2 is not None:
				parsed_rules.append(edge)
				bag_types.add(bag_type_2)
			
	#* we've got all the bag types as the nodes of a graph
	#*  and the rules in the form of edges of a graph
	# print(bag_types)
	# print(*parsed_rules, sep='\n')

	# add the nodes and edges to a graph
	graph = Graph(len(bag_types))
	for bag_type in bag_types:
		graph.add_vertex(bag_type)
	for rule in parsed_rules:
		graph.add_edge(rule[0], rule[1], int(rule[2]))
	
	return graph

def bags_that_can_contain(graph: Graph, bag_type: str) -> int:
	visited = set()
	# get bags that directly can contain the shiny gold bag
	vertices_list = graph.get_incoming_vertices(bag_type)
	# make it a deque for faster pops from front
	current_bags = deque(bag for bag in vertices_list)
	# get all bags that can eventually contain the gold bag
	while current_bags:
		current_bag = current_bags.popleft()
		if current_bag in visited:
			continue
		next_order_bags = graph.get_incoming_vertices(current_bag)
		current_bags.extend(next_order_bags)
		visited.add(current_bag)
		
	# print(visited)
	return len(visited)

def number_of_bags_inside(graph: Graph, bag_type: str) -> int:

	# no more bags can be added 
	if bag_type is None:
		return 0
	adj_vertices = graph.get_adjacent_vertices(bag_type)
	if len(adj_vertices) == 0:
		return number_of_bags_inside(graph, None)
	# recursively find number of bags inside a given bag_type 
	total = 0
	for inner_bag in adj_vertices:
		inner_bag_type, count = inner_bag
		total += count + count * number_of_bags_inside(graph, inner_bag_type)
	return total

if __name__ == "__main__":
	input_file = 'input.txt'
	with open(f'./7/{input_file}', 'r') as input_file:
		input_text = input_file.read()
		input = input_text.split('\n')
	graph = make_graph(input)
	# print(f'bag types: {graph.get_vertices()}')
	# graph.show_adjacency_matrix()
	
	# Part 1
	# print(bags_that_can_contain(graph, 'shiny gold'))
	# Part 2
	print(number_of_bags_inside(graph, 'shiny gold'))
	