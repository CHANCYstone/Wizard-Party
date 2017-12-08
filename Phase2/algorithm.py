import sys
# from sets import Set
import itertools
import time
from copy import deepcopy
from collections import deque


def main(argv):
	# actualStack = []
	# stopRecursive = 0
	print("Hello!")
	if len(argv) != 2:
		print("Usage: python phase2algorithm.py [path_to_input#.py] [path_to_output#.py]")
		return#need to create .out beforehand
	print("Hey!")
	finalOrder = processInput(argv[0], argv[1])



def processInput(input_file, output_file):
	fin = open(input_file, "r")
	fout = open(output_file, "w")

	num_wiz_in_input = int(fin.readline().split()[0])
	num_constraints = int(fin.readline().split()[0])
	
	smarterConstraints = set()
	noNos = set()
	index = 0
	while index < num_constraints:
		constraint = fin.readline().split()
		a, b, c = [wiz for wiz in constraint]
		if not (a == b == c):
			if a > b:
				a, b = b, a
			smarterConstraints.add((a, b, c))
			noNos.add((a, c, b))
			noNos.add((b, c, a))
			index += 1
	# print smarterConstraints
	# print noNos
	# print len(smarterConstraints)
	constraintToTwoTuples = dict()
	for tup in smarterConstraints:
		a = tup[0]
		b = tup[1]
		c = tup[2]
		constraintToTwoTuples[tup] = [(a, b, c), (c, a, b)]
	# print constraintToTwoTuples
	mustBeSatisfied = []
	# permutationsEliminated = 0
	for key in constraintToTwoTuples:
		x, y = constraintToTwoTuples[key]
		# print x
		xA, xB, xC = x[0], x[1], x[2]
		# print xA, xB, xC
		# print y
		yA, yB, yC = y[0], y[1], y[2]
		# print yA, yB, yC
		if (xA, xB, xC) in noNos:
			constraintToTwoTuples[key][0] = None
			# permutationsEliminated += 1
			# print "broken one"
			# print "broken xA, xB, xC are: ", xA, xB, xC
			# print "yA, yB, yC are: ", yA, yB, yC
			mustBeSatisfied.append([yA, yB, yC])
		if (yA, yB, yC) in noNos:
			constraintToTwoTuples[key][1] = None
			# permutationsEliminated += 1
			# print "broken two"
			# print "broken yA, yB, yC are: ", yA, yB, yC
			# print "xA, xB, xC are: ", xA, xB, xC
			mustBeSatisfied.append([xA, xB, xC])
	# print constraintToTwoTuples
	# print permutationsEliminated
	# print mustBeSatisfied

	test = ['Oisin', 'Daragh', 'Paris', 'Ruben', 'Skylar', 'Lianne', 'Mckenna', 'Wesley', 'Pam', 'Joni', 'Dominick', 'Gene', 'Ayesha', 'Carla', 'Chase', 'Curt', 'Amari', 'Janette', 'Conner', 'Neal']

	mustBeSatisfied.sort()
	mustBeSatisfied = list(mustBeSatisfied for mustBeSatisfied, _ in itertools.groupby(mustBeSatisfied))
	# print "mustBeSatisfied: "
	# print mustBeSatisfied


	# for shit in mustBeSatisfied:
	#   s1, s2, s3 = shit[0], shit[1], shit[2]
	#   index1 = test.index(s1)
	#   index2 = test.index(s2)
	#   index3 = test.index(s3)
	#   if index1 > index2 > index3:
	#       print "ok"
	#   elif index3 > index2 > index1:
	#       print "ok2"
	#   else:
	#       print "shit"
	#   # if [s1, s2, s3] in mustBeSatisfied:
	#   #   print "hi"
	#   # if [s3, s2, s1] in mustBeSatisfied:
	#   #   print "we got a reversed here"
	#   # # if [s1, s3, s2] in mustBeSatisfied:
	#   # #     print "oh no 1"
	#   # # if [s2, s1, s3] in mustBeSatisfied:
	#   # #     print "oh no 2"
	#   # # if [s2, s3, s1] in mustBeSatisfied:
	#   # #     print "oh no 3"
	#   # # if [s3, s1, s2] in mustBeSatisfied:
	#   # #     print "oh no 4"
	#   # if [s3, s2, s1] not in mustBeSatisfied:
	#   #   print "good day to you"
	# print "see ya"

	noReversed = set()
	yesReversed = set()

	for newConstraint in mustBeSatisfied:
		wiz1, wiz2, wiz3 = newConstraint[0], newConstraint[1], newConstraint[2]
		if [wiz3, wiz2, wiz1] in mustBeSatisfied:
			# print "tough guys"
			# print wiz1, wiz2, wiz3
			yesReversed.add((wiz1, wiz2, wiz3))
		elif [wiz3, wiz2, wiz1] not in mustBeSatisfied:
			# print "yesReversed"
			noReversed.add((wiz1, wiz2, wiz3))
	
	# print "?????"
	# print yesReversed
	noReversed = list(noReversed)
	yesReversed = list(yesReversed)

	# print "yesReversed: "
	# print yesReversed
	# print "noReversed ok: "
	print noReversed
	wizardsSoFar = set()
	graph = {}
	for ordering in noReversed:
		a, b, c = ordering[0], ordering[1], ordering[2]
		if a not in graph:
			graph[a] = set([b])
			wizardsSoFar.add(a)
		if a in graph:
			graph[a].add(b)
		if b not in graph:
			graph[b] = set([c])
			wizardsSoFar.add(b)
		if b in graph:
			graph[b].add(c)
		if c not in graph:
			graph[c] = set([])
			wizardsSoFar.add(c)
	# print "graph:"
	# print graph
	sort = kahn_topsort(graph)
	# print "sort:"
	# print sort
	# copyOfYesReversed = deepcopy(yesReversed)
	notInYet = []
	for order in yesReversed:
		x, y, z = order[0], order[1], order[2]
		if not (x in wizardsSoFar and y in wizardsSoFar and z in wizardsSoFar):
			# print x, y, z
			notInYet.append((x, y, z))
	# print "notInYet: "
	# print notInYet
	shortNotInYet = []
	for tup in notInYet:
		x, y, z = tup[0], tup[1], tup[2]
		if (tup[2], tup[1], tup[0]) not in shortNotInYet:
			shortNotInYet.append((tup[0], tup[1], tup[2]))
	# print "shortNotInYet:"
	# print shortNotInYet
	rcount = 0
	for perm in shortNotInYet:
		# print "perm: ", perm
		a, b, c = perm[0], perm[1], perm[2]
		if a in sort and b in sort and c not in sort:
			# print "1"
			if sort.index(a) < sort.index(b):
				graph[b].add(c)
				graph[c] = set([])
				wizardsSoFar.add(c)
			elif sort.index(a) > sort.index(b):
				graph[c].add(b)
				wizardsSoFar.add(c)
			# print graph
			rcount += 1
			# print a, b, c
			shortNotInYet.remove(perm)
			# print shortNotInYet
			# notInYet.remove((c, b, a))
		elif b in sort and c in sort and a not in sort:
			# print "2"
			if sort.index(b) < sort.index(c):
				graph[a].add(b)
				wizardsSoFar.add(a)
			elif sort.index(b) > sort.index(c):
				graph[b].add(a)
				graph[a] = set([])
				wizardsSoFar.add(a)
			# print graph
			rcount += 1
			# print a, b, c
			shortNotInYet.remove(perm)
			# print shortNotInYet
			# notInYet.remove((c, b, a))
		elif a in sort and c in sort and b not in sort:
			# print "3"
			if sort.index(a) < sort.index(c):
				graph[a].add(b)
				graph[b] = set([c])
				wizardsSoFar.add(b)
			elif sort.index(a) > sort.index(c):
				graph[c].add(b)
				graph[b] = set([a])
				wizardsSoFar.add(b)
			# print graph
			rcount += 1
			# print a, b, c
			shortNotInYet.remove(perm)
			# print shortNotInYet
			# notInYet.remove((c, b, a))
	# print "new graph:"
	# print graph
	# print "rcount is: ", rcount
	# print "new notinyet"
	# print shortNotInYet

		# if x in sort and y in sort and z in sort:
			# if sort.index(x) < sort.index(y) < sort.index(z):
			# 	print "ok"
			# 	print x, y, z
			# 	print sort.index(x), sort.index(y), sort.index(z)
			# else:
			# 	print "nope"
			# 	print x, y, z
			# 	copyOfYesReversed.remove((x, y, z))
	# print copyOfYesReversed









def kahn_topsort(graph):
	in_degree = {u : 0 for u in graph}
	for u in graph:
		for v in graph[u]:
			in_degree[v] += 1
	Q = deque()
	for u in in_degree:
		if in_degree[u] == 0:
			Q.appendleft(u)
	L = []
	while Q:
		u = Q.pop()
		L.append(u)
		for v in graph[u]:
			in_degree[v] -= 1
			if in_degree[v] == 0:
				Q.appendleft(v)
	if len(L) == len(graph):
		return L
	else:
		return []








	# possibles = []
	# wizardsSoFar = []
	# wizardValues = dict()
	# if noReversed:

	# if len(noReversed) > 0:
	#   # left, mid, right = noReversed[0]
	#   # wizardsSoFar.append(left)
	#   # wizardsSoFar.append(mid)
	#   # wizardsSoFar.append(right)
	#   # possible = [left, mid, right]
	#   # possibles.append(possible)
	#   for strictCon in noReversed:
	#       x, y, z = strictCon[0], strictCon[1], strictCon[2]
	#       if not wizardValues:
	#           wizardValues[x] = 0
	#           wizardValues[y] = 1
	#           wizardValues[z] = 2
	#       if x not in wizardValues:
	#           if z in wizardValues:
	#               if y in wizardValues:







	#       if x not in wizardValues:
	#           wizardValues[x] = 0
	#       if y not in wizardValues:
	#           wizardValues[y] = wizardValues[x] + 1
	#       if z not in wizardValues:
	#           wizardValues[z] = wizardValues[y] + 1
	#       if x in wizardValues:
	#           if wizardValues[y] <= wizardValues[x]:
	#               difference = wizardValues[x] - wizardValues[y]





		# for strictCon in noReversed:
		#   for strictCon in noReversed:
		#       if strictCon[0] in wizardsSoFar and strictCon[1] in wizardsSoFar and strictCon[2] in wizardsSoFar:
		#           for checkIfPossible in possibles:




	# print possibles













if __name__ == '__main__':
	main(sys.argv[1:])


