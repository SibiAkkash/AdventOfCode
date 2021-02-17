
from typing import List, Tuple
Bag = str
Count = int

class Graph:
	def __init__(self, num_vertices: int) -> None:
		# stores bag_types
		self.vertices = []
		# maps bag_type to an id
		self.vertex_map = {}
		# adjacency matrix
		self.adj = [[0 for i in range(num_vertices)] for j in range(num_vertices)]

	def add_vertex(self, bag_type: Bag) -> None:
		# self.vertices = ['blue', 'black', 'red', ....]
		# self.vertex_map[2] = "red"
		# self.adj[2][3]: edge from bag 2 -> bag 3, with a weight
		self.vertices.append(bag_type)
		self.vertex_map[bag_type] = len(self.vertices) - 1

	# adds an directed weighted edge from outer_bag to inner_bag with weight = count
	def add_edge(self, outer_bag: Bag, inner_bag: Bag, count: Count) -> None:
		# check if vertices are present in graph
		if outer_bag not in self.vertices:
			self.add_vertex(outer_bag)
		if inner_bag not in self.vertices:
			self.add_vertex(inner_bag)

		outer_bag_id = self.vertex_map[outer_bag]
		inner_bag_id = self.vertex_map[inner_bag]
		self.adj[outer_bag_id][inner_bag_id] = count

	def get_vertices(self) -> List[str]:
		return self.vertices
	
	def get_adjacency_matrix(self) -> List[List[int]]:
		return self.adj	

	def show_adjacency_matrix(self) -> None:
		for i in range(len(self.adj)):
			print(self.vertices[i], end=' ->\t')
			print(self.adj[i])

	def get_incoming_vertices(self, bag_type: Bag) -> List[Bag]:
		vertices = []
		bag_type_id = self.vertex_map[bag_type]
		# print(f'{bag_type} id: {bag_type_id}')
		for i in range(len(self.adj)):
			# if there is an edge from some bag to the given gold bag
			# add it to the vertices []
			if self.adj[i][bag_type_id] != 0:
				vertices.append(self.vertices[i])

		return vertices

	def get_adjacent_vertices(self, bag_type: Bag) -> List[Tuple[Bag, Count]]:
		vertices = []
		bag_type_id = self.vertex_map[bag_type]
		for i in range(len(self.adj)):
			bag_count = self.adj[bag_type_id][i]
			inner_bag_type = self.vertices[i]
			if bag_count != 0:
				vertices.append((inner_bag_type, bag_count))
		return vertices

	
	