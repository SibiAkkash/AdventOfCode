

''' 
	light red -> 1 bright white, 2 muted yellow
	dark orange -> 3 bright white, 4 muted yellow
	bright white -> 1 shiny gold
	muted yellow -> 2 shiny gold, 9 faded blue
	shiny gold -> 1 dark olive, 2 vibrant plum
	dark olive -> 3 faded blue, 4, dotted black
	vibrant plum -> 5 faded blue, 6 dotted black
	faded blue -> none
	dotted black -> none
'''

from typing import List, Dict, Tuple

Node = str
Weight = int
ParsedRule = List[Tuple[Node, Node, Weight]]

def parse_rule(rule: str) -> ParsedRule:
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


def make_graph(rules: List[str]) -> Dict[str, int]:
	nodes = []
	n = len(nodes)
	# graph = [[0 for i in range(n)] for j in range(n)]
	for rule in rules:
		print(rule, parse_rule(rule))

	# each parsed rule is a list of edges of a directed weighted graph
	# add each edge (rule) to the graph, build the graph from the edges
	# the problem is to find the number of bag colours that can eventually contain a shiny gold bag
	# which is to ask how many nodes in the graph have a path to the target node (shiny gold bag) 



if __name__ == "__main__":
	with open('./7/sample_input.txt', 'r') as input_file:
		input_text = input_file.read()
		input = input_text.split('\n')
	make_graph(input)
	