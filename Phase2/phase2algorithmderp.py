import sys
# from sets import Set
from itertools import permutations
import time
from copy import deepcopy


# global actualStack
# global stopRecursive


def main(argv):
	# actualStack = []
	# stopRecursive = 0
	print("Hello!")
	if len(argv) != 2:
		print("Usage: python phase2algorithm.py [path_to_input#.py] [path_to_output#.py]")
		return#need to create .out beforehand
	print("Hey!")
	finalOrder = processInput(argv[0], argv[1])
	
	# print finalOrder

# graph = {}
# nodesInCycle = set()



def processInput(input_file, output_file):
	fin = open(input_file, "r")
	fout = open(output_file, "w")

	num_wiz_in_input = int(fin.readline().split()[0])
	num_constraints = int(fin.readline().split()[0])
	constraints = []
	index = 0
	graph = {}
	while index < num_constraints:
		constraint = fin.readline().split()
		a, b, c = [wiz for wiz in constraint]
		constraints.append([a, b, c])
		index += 1
	count = 3
	for constraint in constraints:
		print count
		a = constraint[0]
		b = constraint[1]
		# print a
		# print b
		if a not in graph:
			graph[a] = set([b])
		if a in graph:
			graph[a].add(b)
		if b not in graph:
			graph[b] = set([a])
		if b in graph:
			graph[b].add(a)
		# if there is a cycle
		print "adding in ", a, " and ", b
		# print "graph is now: ", graph
		print "======================================"
		# print "nodesInCycle pls be empty: ", nodesInCycle
		print "graphs: ", graph
		if cycle_exists(graph):
			find_nodes_in_cycle_dfs_visit.stack = []
			# find_nodes_in_cycle_dfs_visit.stopRecursive = 0
			find_nodes_in_cycle_dfs_visit.actualStack = []
			find_nodes_in_cycle_dfs_visit.splitPoint = []
			print "graph is: ", graph
			# found a cycle means need to run thru constraints
			# keep a counter for every edge that may break constraint
			# remove the edge that has the highest counter
			# print "cycle exists"
			# print "cycle is: ", nodesInCycle
			# stack = []
			# print "STACK IS::::::::::::::::::::: ", stack
			# global actualStack
			# actualStack = []
			# global stopRecursive
			# stopRecursive = 0
			nodes = find_nodes_in_cycle_exists(graph)
			print "nodes is: ", nodes
			# print("please work actualStack: ", actualStack)
			# stopRecursive = 0
			nodesInCycle = set(nodes)
			print "nodesInCycle is: ", nodesInCycle
			# miniGraphFromCycle = {}
			# actualStack = []
			# print("hope its empty ", nodesInCycle)


			# error below here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


			# print "graph is: ", graph
			copyOfGraph = deepcopy(graph)
			# print "copyOfGraph is: ", copyOfGraph
			copyOfGraph = {k : v for k, v in copyOfGraph.iteritems() if k in nodesInCycle}
			# for firstWiz in copyOfGraph:
			# 	if firstWiz not in nodesInCycle:
			# 		del copyOfGraph[firstWiz]
			# print "improved: ", copyOfGraph
			for firstWiz in copyOfGraph:
				copyOfGraph[firstWiz] = set([wizard for wizard in copyOfGraph[firstWiz] if wizard in nodesInCycle])
			# print "copyOfGraph is yay: ", copyOfGraph

			# for fnode in nodesInCycle:
			# 	gen = (x for x in nodesInCycle if x != fnode)
			# 	for snode in gen:
			# 		if fnode not in miniGraphFromCycle:
			# 			miniGraphFromCycle[fnode] = set([snode])
			# 		if fnode in miniGraphFromCycle:
			# 			miniGraphFromCycle[fnode].add(snode)
			# 		if snode not in miniGraphFromCycle:
			# 			miniGraphFromCycle[snode] = set([fnode])
			# 		if snode in miniGraphFromCycle:
			# 			miniGraphFromCycle[snode].add(fnode)
			# # print("------------------------------")
			# # print("nodesInCycle are: ", nodesInCycle)
			# # print("------------------------------")
			# print "------------------------------"
			# print "miniGraphFromCycle is: ", miniGraphFromCycle
			# print "------------------------------"
			# miniGraphEdges = generate_edges(miniGraphFromCycle)
			miniGraphEdges = generate_edges(copyOfGraph)
			# print "miniGraphEdges is: ", miniGraphEdges
			copyOfMiniGraphEdges = deepcopy(miniGraphEdges)
			# print "------------------------------"
			# print "oh snap copyOfMiniGraphEdges", copyOfMiniGraphEdges
			# eliminated = set()
			ok = set()
			for con in constraints:
				x = con[0]
				y = con[1]
				z = con[2]
				if x in nodesInCycle and y in nodesInCycle and z in nodesInCycle:
					# print("x is: ", x)
					# print("y is: ", y)
					# print("z is: ", z)
					# print "copy is: ", copyOfMiniGraphEdges
					if (x, y) in copyOfMiniGraphEdges:
						ok.add((x, y))
						ok.add((y, x))
			# print "ok constraints are: ", ok
			troubleEdges = [x for x in copyOfMiniGraphEdges if x not in ok]
			print "troubleEdges is: ", troubleEdges
			# print "?????????????????????????????????????????????????"
			# eliminatedLength = len(eliminated)
			# while eliminatedLength > 2:
			# 	for pair in eliminated:
			# 		print "time to eliminate the pair: ", pair 
			# 		first = pair[0]
			# 		second = pair[1]
			# 		eliminated.remove((first, second))
			# 		eliminated.remove((second, first))
			# 		print "eliminated is now: ", eliminated
					# eliminatedLength -= 2
						# print "trueeeee"
						# eliminated.add((x, y))
						# eliminated.add((y, x))
					# copyOfMiniGraphEdges.remove((x, y))
					# copyOfMiniGraphEdges.remove((y, x))
			# print "oh snap eliminated is now", eliminated
			# print "graph is ", graph
			# print "eliminated is: ", eliminated
			for tup in eliminated:
				first = tup[0]
				second = tup[1]
				# print "first is: ", first
				# print "second is: ", second
				# s = graph[first]
				# print(s)
				# graph[first] = 

				graph[first].remove(second)
			print "ghahhhhhhh", graph
			nodesInCycle.clear()
			# miniGraphFromCycle.clear()
			eliminated = []
			miniGraphEdges[:] = []
			copyOfMiniGraphEdges[:] = []
			find_nodes_in_cycle_dfs_visit.stack = []
			ok = set()
			copyOfGraph = {}
			# find_nodes_in_cycle_dfs_visit.stopRecursive = 0
			find_nodes_in_cycle_dfs_visit.actualStack = []
			find_nodes_in_cycle_dfs_visit.splitPoint = []
		count += 1
		# print "------------------------"
		# reset nodesInCycle to be empty again
		# nodesInCycle = set()
	print "---------------------------------"
	print graph
	# print("lets do this")
	start = None
	end = None
	for k in graph:
		print k
		if start is None and len(graph[k]) == 1:
			start = k
		elif start is not None and len(graph[k]) == 1:
			end = k
	# print "ok thomas"
	print "start is: ", start
	print "end is: ", end
	# print generate_edges(graph)
	solution = find_path(graph, start, end)
	# return " ".join(str(x) for x in solution)
	print solution
	fout.write(" ".join(str(x) for x in solution))

	# print "num_wiz_in_input is: ", num_wiz_in_input
	# print topologicalSort(graph, num_wiz_in_input)



def cycle_exists(G):     
	# nodesInCycle = set()
	marked = {u : False for u in G}
	# stack = []
	found_cycle = [False]
	for u in G:
		if not marked[u]:
			dfs_visit(G, u, found_cycle, u, marked)
		if found_cycle[0]:
			break
	# print "yayayaayayay", nodesInCycle
	# print "final stack from cycle exists: ", actualStack
	return found_cycle[0]



def dfs_visit(G, u, found_cycle, pred_node, marked):
	# if len(stack) == 0:
	# 	stack.append(u)
	# 	print "stack is starting with: ", stack
	# if stopPopping:
	# 	actualStack = list(stack)
	# 	stopPopping = False
	# paths = []
	if found_cycle[0]:
		return
	marked[u] = True
	# stack.append(u)
	# print "stack is now: ", stack
	for v in G[u]:
		# stack.append(v)
		# print "stack is now: ", stack
		if marked[v] and v != pred_node:
			# print "u is: ", u
			# print "G[u] is: ", G[u]
			# print "v is: ", v
			found_cycle[0] = True
			# nodesInCycle.add(u)
			# nodesInCycle.add(v)
			# print "pred_node is: ", pred_node
			# print "marked is: ", marked[u]
			# nodesInCycle.add(pred_node)
			# print "nodesInCycle are now: ", nodesInCycle
			# stack.pop()
			# print "last chance stack: ", stack
			# stopPopping = True
			# print "yes"
			# paths.append(v)
			# print "harry potter: ", paths
			return
		if not marked[v]:
			# if len(stack) > 1:
			# 	print "popping stack"
			# 	stack.pop()
			# 	print "stack is now", stack
			# print "failed u is: ", u
			# print "failed G[u] is: ", G[u]
			# print "failed v is: ", v
			# print "failed nodesInCycle is: ", nodesInCycle
			# print "continue"
			# stack.pop()
			# stack.append(v)
			# print "stack is now: ", stack
			# print "no"
			dfs_visit(G, v, found_cycle, u, marked)
			# print "post dfs is: ", v, " and ", u
		# else:
		# 	print "stack is going to pop"
		# 	stack.pop()
		# 	print "stack is now: ", stack
	# stack.pop()
	# print "after pop stack is now: ", stack







# stopRecursive = 0
stack = []
actualStack = []
splitPoint = []




def find_nodes_in_cycle_exists(G):
	global stack, actualStack, splitPoint
	copyOfActualStack = []
	# nodesInCycle = set()
	# print "G is: ", G
	# actualStack = []
	# stopRecursive = 0
	# luigi = []
	marked = {u : False for u in G}
	# stack = []
	found_cycle = [False]
	# splitPoint = []
	for u in G:
		# print "u is starting at: ", u
		if not marked[u]:
			# print "lets go"
			find_nodes_in_cycle_dfs_visit(G, u, found_cycle, u, marked, stack, actualStack, splitPoint)
			stack = []
			# actualStack = []
			splitPoint = []
			# print "luigi is: ", luigi
			# print actualStack
		if found_cycle[0]:
			# print "wario: ", luigi
			break
	# print "yayayaayayay", nodesInCycle
	# print("final stack from cycle exists: ", actualStack)
	# print "pls be different actualStack: ", actualStack
	print "ac : ", actualStack
	copyOfActualStack = deepcopy(actualStack)
	actualStack = []
	return copyOfActualStack[0]

# find_nodes_in_cycle_exists.luigi = []


def find_nodes_in_cycle_dfs_visit(G, u, found_cycle, pred_node, marked, stack, actualStack, splitPoint):
	# global actualStack
	# if len(stack) == 0:
	# 	stack.append(u)
	# 	print "stack is starting with: ", stack
	# if stopPopping:
	# 	actualStack = list(stack)
	# 	stopPopping = True
	# global stopRecursive
	# if find_nodes_in_cycle_dfs_visit.stopRecursive > 0:
	# 	return find_nodes_in_cycle_dfs_visit.actualStack
	# print "G is: ", G
	# print "u is: ", u
	# print "found_cycle is: ", found_cycle
	# print "pred_node is: ", pred_node
	# print "marked is: ", marked
	# print "stack rn is: ", stack
	# if stopRecursive > 0:
	# 	return
	if found_cycle[0]:
		# print "hopefully this works: ", actualStack
		# return find_nodes_in_cycle_dfs_visit.actualStack
		# print "end"
		return
	marked[u] = True
	stack.append(u)
	print "stack is now: ", stack
	for v in G[u]:
		# stack.append(v)
		# print "stack is now: ", stack
		if marked[v] and v != pred_node:
			# print "u is: ", u
			# print "G[u] is: ", G[u]
			# print "v is: ", v
			found_cycle[0] = True
			# find_nodes_in_cycle_dfs_visit.stopRecursive += 1
			# stopRecursive += 1
			# nodesInCycle.add(u)
			# nodesInCycle.add(v)
			# print "pred_node is: ", pred_node
			# print "marked is: ", marked[u]
			# nodesInCycle.add(pred_node)
			# print "nodesInCycle are now: ", nodesInCycle
			# stack.pop()
			# print("last chance stack: ", stack)
			# stopPopping = True
			# print "yes"
			# if stopRecursive > 0:
			# 	print "this is it: ", stack
			# find_nodes_in_cycle_dfs_visit.actualStack = list(stack)
			# print "stack is finallllly: ", stack
			# actualStack.append(list(stack))
			# print "vvvvvv is: ", v
			splitPoint.append(v)
			print "splitPoint is now: ", splitPoint
			position = stack.index(splitPoint[0])
			minis = stack[position:]
			actualStack.append(minis)
			# stack = []
			# print "finally actualStack is now: ", find_nodes_in_cycle_dfs_visit.actualStack
			print "finally actualStack is now: ", actualStack
			# print "maybe"
			return
			# return actualStack
			# return find_nodes_in_cycle_dfs_visit.actualStack
			# break
		if not marked[v]:
			# if len(stack) > 1:
			# 	print "popping stack"
			# 	stack.pop()
			# 	print "stack is now", stack
			# print "failed u is: ", u
			# print "failed G[u] is: ", G[u]
			# print "failed v is: ", v
			# print "failed nodesInCycle is: ", nodesInCycle
			# print "continue"
			# stack.pop()
			# stack.append(v)
			# print "stack is now: ", stack
			# print "no"
			# print "continue"
			# print "v is: ", v
			original = u
			# print "original is now: ", original
			find_nodes_in_cycle_dfs_visit(G, v, found_cycle, u, marked, stack, actualStack, splitPoint)
			# print "post dfs is: ", v, " and ", u
		# else:
		# 	print "stack is going to pop"
		# 	stack.pop()
		# 	print "stack is now: ", stack
	# if not stopPopping:
	# if stopRecursive == 0:
		# print "stack: ", stack
	# print "pls run"
	stack.pop()
	# print "pop original is: ", original
	# print "pop u is: ", u
	# print "pop v is: ", v
	# print "pls run2"
	# return actualStack
	# print "after pop stack is now: ", stack


# find_nodes_in_cycle_dfs_visit.stopRecursive = 0
# find_nodes_in_cycle_dfs_visit.actualStack = []































def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges



def find_path(graph, start_vertex, end_vertex, path=None):
    """ find a path from start_vertex to end_vertex 
        in graph """
    # print("path is: ", path)
    if path == None:
        path = []
    path = path + [start_vertex]
    # print("path is now: ", path)
    # print graph
    if start_vertex == end_vertex:
    	# print("returns: ", path)
        return path
    if start_vertex not in graph:
    	# print "pls no"
    	# print("start_vertex is: ", start_vertex)
    	# print("and graph is: ", graph)
        return None
    for vertex in graph[start_vertex]:
    	# print("vertex is: ", vertex)
        if vertex not in path:
            extended_path = find_path(graph, vertex, end_vertex, path)
            if extended_path: 
                return extended_path
    return None

# # A recursive function used by topologicalSort
# def topologicalSortUtil(v, visited, stack, num_wiz):
# 	# Mark the current node as visited.
# 	visited[v] = True
# 	# Recur for all the vertices adjacent to this vertex
# 	for i in range(num_wiz):
# 		if visited[i] == False:
# 			topologicalSortUtil(i, visited, stack, num_wiz)
# 	# Push current vertex to stack which stores result
# 	stack.insert(0, v)
# 	print "stack is: ", stack

# # The function to do Topological Sort. It uses recursive 
# # topologicalSortUtil()
# def topologicalSort(graph, num_wiz):
# 	# Mark all the vertices as not visited
# 	visited = [False]*num_wiz
# 	stack =[]
# 	# Call the recursive helper function to store Topological
# 	# Sort starting from all vertices one by one
# 	for i in range(num_wiz):
# 		if visited[i] == False:
# 			topologicalSortUtil(i, visited, stack, num_wiz)
# 	# Print contents of stack
# 	print "stack issssssss: ", stack





if __name__ == '__main__':
	main(sys.argv[1:])


