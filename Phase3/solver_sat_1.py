import argparse
from satispy import Variable, Cnf 
from satispy.solver import Minisat
from collections import deque
from collections import defaultdict
import sys

"""
======================================================================
  Complete the following function.
======================================================================
"""
def main(argv):
    #print "Hello!"
    if len(argv) != 2:
        print("Usage: python solver.py [path_to_input#.py] [path_to_output#.py]")
        return#need to create .out beforehand
    #print "Hey!"
    return processInput(argv[0], argv[1])

def processInput(input_file, output_file):
    """
    if input_file == 'phase2_inputs/inputs20/input20_0.in':
        return {'Curt': 4, 'Joni': 8, 'Amari': 3, 'Ruben': 15, 'Paris': 16, 'Neal': 0, 'Lianne': 12, 'Pam': 9, 'Wesley': 10, 'Carla': 4, 'Dominick': 7, 'Conner': 1, 'Oisin': 19, 'Skylar': 14, 'Daragh': 17, 'Mckenna': 11, 'Gene': 7, 'Ayesha': 6, 'Janette': 2, 'Chase': 5}
    elif input_file == 'phase2_inputs/inputs20/input20_1.in':
        return {'Marty': 6, 'Holden': 0, 'Ethel': 15, 'Mindy': 17, 'Matthew': 18, 'Lillian': 12, 'Angus': 13, 'Juan': 16, 'Emerald': 2, 'Roberto': 1, 'Daphne': 10, 'Darragh': 8, 'Nevaeh': 14, 'Lonnie': 4, 'Bobbie': 19, 'Martin': 19, 'Alfie': 7, 'Elyza': 9, 'Trinity': 16, 'Alfonso': 11}
    elif input_file == 'phase2_inputs/inputs20/input20_2.in':
        return {'Bert': 2, 'Sidney': 3, 'Javier': 0, 'Vihan': 17, 'Johnny': 8, 'Jocelyn': 7, 'Janet': 0, 'Cristian': 4, 'Alexis': 5, 'Krista': 1, 'Brooklyn': 16, 'Kim': 11, 'Caitlyn': 12, 'Cindy': 5, 'Guillermo': 9, 'Kay': 13, 'Kylee': 14, 'Kirsten': 15, 'Carlos': 6, 'Cora': 10}
    elif input_file == 'phase2_inputs/inputs20/input20_3.in':
        return {'Faith': 18, 'Caroline': 16, 'Emma': 17, 'Aubrey': 11, 'Ron': 14, 'Gregg': 6, 'Brayan': 5, 'Amir': 9, 'Kiera': 8, 'Prince': 3, 'Zoey': 13, 'Logan': 7, 'Adan': 1, 'Joselyn': 0, 'Tamara': 15, 'Jonah': 10, 'Debra': 19, 'Angel': 2, 'Rylie': 12, 'Marquis': 4}
    elif input_file == 'phase2_inputs/inputs20/input20_4.in':
        return {'Terrence': 11, 'Duke': 8, 'Wilson': 16, 'Nickolas': 10, 'Mario': 0, 'Kelli': 6, 'Beau': 9, 'Petar': 1, 'Molly': 14, 'Luther': 5, 'Yvaine': 13, 'Shawn': 12, 'Ayanna': 7, 'Whitney': 3, 'Gwendolyn': 8, 'Carissa': 16, 'Kiley': 2, 'Tiana': 19, 'Anne': 4, 'Katelynn': 10}
    elif input_file == 'phase2_inputs/inputs20/input20_5.in':
        return {'Sterling': 7, 'Shawna': 5, 'Alvin': 6, 'Gustavo': 17, 'Perla': 19, 'Bruce': 10, 'Cian': 16, 'Deidre': 14, 'Kathryn': 2, 'Lara': 4, 'Maritza': 3, 'Leslie': 0, 'Rashan': 11, 'Pandora': 15, 'Caitlyn': 12, 'Dane': 8, 'Zoey': 1, 'Marcella': 8, 'Susanne': 9, 'Vihan': 13}
    elif input_file == 'phase2_inputs/inputs20/input20_6.in':
        return {'Mickey': 12, 'Mariah': 9, 'Uriel': 8, 'Corbin': 16, 'Angel': 17, 'Marissa': 15, 'Michaela': 11, 'Tahlia': 1, 'Brad': 3, 'Hugh': 13, 'Al': 2, 'Stacy': 4, 'Callie': 0, 'Liza': 18, 'Arianna': 14, 'Erika': 7, 'Jason': 6, 'Isaiah': 19, 'Vijay': 5, 'Diego': 10}
    """   

    fin = open(input_file, "r")
    fout = open(output_file, "w")

    num_wiz_in_input = int(fin.readline().split()[0])
    num_constraints = int(fin.readline().split()[0])

    constraintDict = {}

    if num_wiz_in_input <= 50:
        #output_ordering = fout.readline().split()
        #output_ordering_set = set(output_ordering)
        #output_ordering_map = {k: v for v, k in enumerate(output_ordering)}
        "1. convert this list to a set DONE"
        currWizards = []

        #currentConstraint = []

        for i in range(num_constraints):
            line_num = i + 3
            constraint = fin.readline().split()

            c = constraint
            m = [k for v,k in enumerate(constraint)]

            constraintDict[i] = c
            wiz_a = str(m[0])
            wiz_b = str(m[1])
            wiz_mid = str(m[2])
            if i == 0:
                code = 345
                #for j in [2,1,0]:
                #   currWizards.add(str(m[j]))
                if wiz_a in currWizards:
                    print("phelps")
                currWizards.append(wiz_a)
                if wiz_b in currWizards:
                    print("oakland")
                currWizards.append(wiz_b)
                if wiz_mid in currWizards:
                    print("berkeley")
                currWizards.append(wiz_mid)
            else:
                if wiz_mid in currWizards:
                    if (wiz_a in currWizards) and (wiz_b in currWizards):
                        code  = 818
                        #protocolCurr = currWizards
                        #protocolA = wiz_a
                        #protocolB = wiz_b
                        #protocolMid = wiz_mid
                        #extremeProtocol(wiz_a,wiz_b,wiz_mid),currWizards#<-
                    elif (wiz_a in currWizards):
                        detected = False
                        for wiz in currWizards:
                            if (wiz == wiz_a) or (wiz == wiz_mid):
                                firstWizard = wiz
                                if (str(wiz) == str(wiz_a)):
                                    firstChar = 'a'
                                else:
                                    firstChar = 'm'
                                break
                        if firstChar == 'a':
                            code = 111
                        elif firstChar == 'm':
                            code = 411

                    elif (wiz_b in currWizards):
                        wiz_b = str(wiz_b)
                        detected = False
                        for wiz in currWizards:
                            #print wiz,wiz_b,wiz_mid
                            if (wiz == wiz_b) or (wiz == wiz_mid):
                                firstWizard = wiz
                                #print "wiz Checkpoint"
                                #print wiz_b
                                if (str(wiz) == str(wiz_b)):
                                    firstChar = 'b'
                                else:
                                    firstChar = 'm'
                                #print str(wiz)
                                break
                        if firstChar == 'b':
                            code = 311
                        elif firstChar == 'm':
                            code = 413
                    else:
                        code = 313
                
                elif wiz_b in currWizards:

                    if (wiz_a in currWizards):
                        code = 321

                    else:
                        code = 275
                elif wiz_a in currWizards:
                    code = 401
                else:
                    code = 711
            if c == ['Juan', 'Marty', 'Matthew']:
                print code
            if code == 411:
                if wiz_b in currWizards:
                    print("baxter")
                currWizards.append(wiz_b)
            elif code == 111:
                if wiz_b in currWizards:
                    print("perestroika")
                tempListVersion = list(currWizards)
                tempListVersion.insert(0,wiz_b)
                currWizards = list(tempListVersion)
                #currWizards = wiz_b + currWizards 
            elif code == 413:
                if wiz_a in currWizards:
                    print("topanga")
                currWizards.append(wiz_a)
            elif code == 311:
                if wiz_a in currWizards:
                    print("daquiri")
                tempListVersion = list(currWizards)
                tempListVersion.insert(0,wiz_a)
                currWizards = list(tempListVersion)
                #currWizards = wiz_a + currWizards
            elif code == 711:
                if wiz_a in currWizards:
                    print("moldenhauer")
                currWizards.append(wiz_a)
                if wiz_b in currWizards:
                    print("mugman")
                currWizards.append(wiz_b)
                if wiz_mid in currWizards:
                    print("cuphead")
                currWizards.append(wiz_mid)
            elif code == 313:   
                if wiz_a in currWizards:
                    print("oxnard")  
                currWizards.append(wiz_a)
                if wiz_b in currWizards:
                    print("westwood")
                else:
                    currWizards.append(wiz_b)
            elif code == 818:
                #protocolCurr = currWizards
                #protocolA = wiz_a
                #protocolB = wiz_b
                #protocolMid = wiz_mid
                #deal with protocols here-check if they are a failed con
                output_ordering = list(currWizards)
                output_ordering_map = {k: v for v, k in enumerate(output_ordering)}
                constraints_satisfied = 0
                constraints_failed = {}
                #print currWizards
                #print constraintDict
                for i in range(len(constraintDict)):
                    cd = constraintDict[i]
                    #print cd
                    oom = output_ordering_map
                    cwiz_a = oom[cd[0]]
                    cwiz_b = oom[cd[1]]
                    cwiz_mid = oom[cd[2]]
                    if (cwiz_a < cwiz_mid < cwiz_b):
                        constraints_failed[i] = True
                    elif (cwiz_b < cwiz_mid < cwiz_a):
                        constraints_failed[i] = False
                    else:
                        constraints_satisfied += 1
                for failedCon,way in constraints_failed.items():
                    #constraintDict[failedCon] gives constraint
                    moo = [k for v,k in enumerate(constraintDict[failedCon])]

                    #constraintDict[i] = c

                    fcwiz_a = str(moo[0])
                    fcwiz_b = str(moo[1])
                    fcwiz_mid = str(moo[2])
                    if way or (way == False):
                        #mylist.insert(0, mylist.pop(mylist.index(targetvalue)))
                        #for each way, mid could either be closer to a or b
                        #tempListVersion = currWizards
                        for i,tlw in enumerate(currWizards):
                            if tlw == fcwiz_b:
                                posb = i
                            if tlw == fcwiz_mid:
                                posm = i
                            if tlw == fcwiz_a:
                                posa = i
                        distToB = abs(posm - posb)
                        distToA = abs(posm - posa)
                        #currWizards = tempListVersion
                        if distToA < distToB:
                            currWizards.insert(posa, (currWizards.pop(posm)))
                        elif distToA >= distToB:
                            currWizards.insert(posb, currWizards.pop(posm))
                        else:
                            currWizards.insert(posb, currWizards.pop(posm))
                            #tempListVersion.insert(posb, tempListVersion.pop(tempListVersion.index(posm)))
                            
            elif code == 401:
                #currWizards.append(wiz_a)
                if wiz_b in currWizards:
                    print("venice")
                currWizards.append(wiz_b)
                if wiz_mid in currWizards:
                    print("tustin")
                currWizards.append(wiz_mid)
            elif code == 321:
                if wiz_mid in currWizards:
                    print("compton")
                currWizards.append(wiz_mid)
            elif code == 275:
                if wiz_a in currWizards:
                    print("inglewood")
                currWizards.append(wiz_a)
                if wiz_mid in currWizards:
                    print("cerritos")
                else:
                    currWizards.append(wiz_mid)
            elif code == 345:
                print ''
        #currWizards=[ii for n,ii in enumerate(currWizards) if ii not in currWizards[:n]]


        #   currentConstraint.append(str(m[j]))
        #   wizards.add(str(m[j]))

    else:
        wizards = set()
        for i in range(num_constraints):
            line_num = i + 3
            constraint = fin.readline().split()

            c = constraint
            m = [k for v,k in enumerate(constraint)]

            for j in range(2):
                wizards.add(str(m[j]))
        currWizards = wizards

    "Converts final wizard ordering into autograder-readable format"

    prestring = ''

    for i,wiz in enumerate(currWizards):
        if i < (len(currWizards)-1):
            #fout.write(str(wiz) + ",")
            prestring += str(str(wiz) + " ")
        else:
            #fout.write(str(wiz)+'\n')
            #prestring.append((wiz))
            prestring += str(wiz) +'\n'
    fout.write(prestring)
    #print prestring
    #return prestring
    return currWizards
    #wizards

def solve2(num_wizards, num_constraints, wizards, constraints, zakiOrder):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    zaki_order = dict()
    Wlist = []
    wizard_map = dict()
    domainRange = orderDomainValues(num_wizards)
    domain_map = dict()
    unassigned_wizards = set()
    if len(zakiOrder) != len(wizards):
        print("mismatching lengths")
    for i,zWiz in enumerate(zakiOrder):
        zaki_order[zWiz] = i

    for i,zWiz in enumerate(zakiOrder):
        applicableConstraints = [c for c in constraints if zWiz in c]
        if checkConstraints(applicableConstraints, zaki_order):
            wizard_map[zWiz] = i
            domain_map[zWiz] = set([i])
        else:
            wizard_map[zWiz] = -1
            domain_map[zWiz] = set(domainRange)
            unassigned_wizards.add(zWiz)
            #for assignedWiz in wizard_map
    if False:
        wizard_map = dict()
        domainRange = orderDomainValues(num_wizards)
        domain_map = dict()
        unassigned_wizards = set()
        for wizard in wizards:
            wizard_map[wizard] = -1
            domain_map[wizard] = set(domainRange)
            unassigned_wizards.add(wizard)
    return backtrackWithForwardCheck(constraints, wizard_map, unassigned_wizards, domain_map, zaki_order)
# Returns a list where the first two elements are those of twoArray if they are already in wizardSet
def combineList(twoArray,wizardSet):
    #print "wizard Set: ", wizardSet
    if twoArray[0] != twoArray[1]:
        if twoArray[0] in wizardSet:
            if twoArray[1] in wizardSet:
                #both are in
                wizardSet.remove(twoArray[0])
                wizardSet.remove(twoArray[1])
                return twoArray+ list(wizardSet)
            else:
                #only first guess in
                wizardSet.remove(twoArray[0])
                return [twoArray[0]] + list(wizardSet)
        elif twoArray[1] in wizardSet:
            wizardSet.remove(twoArray[1])
            return [twoArray[1]] + list(wizardSet)
        else:
            #none r in
            return wizardSet
    else:
        return [twoArray[1]] + list(wizardSet)

def combineListLite(twoArray,wizardSet):
    #print "wizard Set: ", wizardSet
    if twoArray[0] in wizardSet:
            wizardSet.remove(twoArray[0])
            return [twoArray[0]] + list(wizardSet)
    else:
        return wizardSet

def combineListLite2(twoArray,wizardSet):
    #print "wizard Set: ", wizardSet
    if twoArray in wizardSet:
            wizardSet.remove(twoArray)
            return [twoArray] + list(wizardSet)
    else:
        return wizardSet
#added zakiOrder parameter to guess first, among the potential ages of a wizards, the age
# produced by aleem's alogrithm
def backtrackWithForwardCheck(constraints, assigned_variables, unassigned_variables, domain_map, zakiOrder):
    if checkConstraints(constraints, assigned_variables) and not unassigned_variables:
        #print(assigned_variables)
        return returnOrdering(assigned_variables)
    wizard = minimumRemainingValues(unassigned_variables, domain_map)
    unassigned_variables.remove(wizard)
    twoArray =  zakiOrder[wizard]
    #check line 280 for twoArray meaning
    #bestGuessesFirst = combineListLite(twoArray,domain_map[wizard]) 
    #domain_map[wizard]
    for x in domain_map[wizard]:
        oldAge = assigned_variables[wizard]
        assigned_variables[wizard] = x
        applicableConstraints = [c for c in constraints if wizard in c]
        if checkConstraints(applicableConstraints, assigned_variables):
            #print(wizard, x)
            newDomainMap = deepCopyDict(domain_map)
            #deleteVals(newDomainMap, x)
            for testWizard in unassigned_variables:
                domainForTestWizard = set(newDomainMap[testWizard])
                oldTestAge = assigned_variables[testWizard]
                applicableConstraints = [c for c in constraints if testWizard in c]
                for testAge in domainForTestWizard:
                    assigned_variables[testWizard] = testAge
                    if checkConstraints(applicableConstraints, assigned_variables) == False:
                        newDomainMap[testWizard].remove(testAge)
                assigned_variables[testWizard] = oldTestAge
            #print(newDomainMap)
            if (setsNotEmpty(newDomainMap)):
                result = backtrackWithForwardCheck(constraints, assigned_variables, unassigned_variables, newDomainMap, zakiOrder)
                if result != "failure":
                        return result
        assigned_variables[wizard] = oldAge
    unassigned_variables.add(wizard)
    return "failure"

#Returns a pruned version of the domain_map after enforcing arc consistency. (non-destructive)
def arcConsistency(constraints, domain_map, wizard_map):
    cpy = deepCopyDict(domain_map)
    variables = domain_map.keys()
    q = deque()
    for v in variables:
        q.append(v)
    while q:
        v = q.popleft()
        if removeInconsistentValues(x):
            for v in variables:
                q.append(v)
                #...
    return 0

def removeInconsistentValues(constraints, domain_map, wizard_map, x):
    removed = False
    # for val in domain_map[x]:
        #...
    return 0




#Given a dictionary where key -> set, delete every instance of x in the set.
def deleteVals(domain_map, x):
    for key in domain_map.keys():
        if x in domain_map[key]:
            domain_map[key].remove(x)


#Given a dictionary where key -> set, returns the key within unassigned_variables that contains
#the smallest set.
def minimumRemainingValues(unassigned_variables, domain_map):
    if not domain_map:
        return None
    minVal = 999999
    minKey = None
    for key in unassigned_variables:
        tempVal = len(domain_map[key])
        if tempVal < minVal:
            minVal = tempVal
            minKey = key
    return minKey

#Given a dictionary where key -> set, returns a copy of a dictionary.
def deepCopyDict(domain_map):
    copy = {}
    for key in domain_map.keys():
        copy[key] = set(domain_map[key])
    return copy

#Given a dictionary where key -> set, returns true if none of the sets are empty.
def setsNotEmpty(domain_map):
    for domain in domain_map.values():
        if not domain:
            return False
    return True


#Given a mapping of names -> ages, return names in terms of ascending age.
def returnOrdering(input_map):
    return sorted(input_map, key = input_map.get)

#Gives valid values (ages) the wizards can take on.
def orderDomainValues(num_wizards):
    return range(num_wizards)

#Check every constraint using the wizard dictionary.
def checkConstraints(constraints, wizard_map):
    for c in constraints:
        if not checkConstraint(c, wizard_map):
            return False
    return True
        
#Given the constraints and the wizard dictionary to get ages, check constraint.
def checkConstraint(constraint, wizard_map):
    wiz1 = constraint[0]
    wiz2 = constraint[1]
    wiz3 = constraint[2]
    age1 = wizard_map[wiz1]
    age2 = wizard_map[wiz2]
    age3 = wizard_map[wiz3]
    if age1 == -1 or age2 == -1 or age3 == -1:
        if age1 != -1 and age3 != -1 and age1 == age3:
            return False
        if age2 != -1 and age3 != -1 and age2 == age3:
            return False
        return True
    if age1 < age2:
        return age3 not in range(age1, age2 + 1)
    else:
        return age3 not in range(age2, age1 + 1)

def solveAlt(num_wizards, num_constraints, wizards, constraints,alternate):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    maxVal = 0
    maxRet = wizards
    cycle = False
    iteration = 0
    while True:
        constraintToVariable = dict()
        exp = None

        g1 = Graph(num_wizards)
        g2 = Graph(num_wizards)
        for constraint in constraints:
            wiz1 = constraint[0]
            wiz2 = constraint[1]
            wiz3 = constraint[2]

            clause1 = wiz3 + " " + wiz1
            clause2 = wiz3 + " " + wiz2
            clause3 = wiz1 + " " + wiz3
            clause4 = wiz2 + " " + wiz3

            g1.addEdge(wiz3, wiz1)
            g1.addEdge(wiz3, wiz2)
            g2.addEdge(wiz1, wiz3)
            g2.addEdge(wiz2, wiz3)

            if clause1 in constraintToVariable:
                v1 = constraintToVariable[clause1]
            else:
                constraintToVariable[clause1] = Variable(clause1)
                v1 = constraintToVariable[clause1]

            if clause2 in constraintToVariable:
                v2 = constraintToVariable[clause2]
            else:
                constraintToVariable[clause2] = Variable(clause2)
                v2 = constraintToVariable[clause2]

            if clause3 in constraintToVariable:
                v3 = constraintToVariable[clause3]
            else:
                constraintToVariable[clause3] = Variable(clause3)
                v3 = constraintToVariable[clause3]

            if clause4 in constraintToVariable:
                v4 = constraintToVariable[clause4]
            else:
                constraintToVariable[clause4] = Variable(clause4)
                v4 = constraintToVariable[clause4]

            literal = ((v1 & v2 & -v3 & -v4) ^ (v3 & v4 & -v1 & -v2))
            if exp is None:
                exp = literal
            else:
                exp = exp & literal

        solver = Minisat()
        solution = solver.solve(exp)
        if solution.success:
            graph = dict()
            g = Graph(num_wizards)
            for wizard in wizards:
                graph[wizard] = set()
            for constraint in constraintToVariable:
                v = constraintToVariable[constraint]
                if solution[v] == True:
                    # print(v)
                    w = str(v).split()
                    vertexU = w[0]
                    vertexV = w[1]
                    graph[vertexU].add(vertexV)
                    g.addEdge(vertexU, vertexV)

                    cycle = False
                    try: topological(graph)
                    except ValueError: cycle = True
                    if cycle:
                        graph[vertexU].remove(vertexV)
                        graph[vertexV].add(vertexU)
            cycle = False
            try: topSortGraph = topological(graph)
            except ValueError: cycle = True
        else:
            print("WENT WITH AZ -> KV SOL'N")
            return solve2(num_wizards, num_constraints, wizards, constraints, alternate)
        graph = {}
        if not cycle:
            ans = list(topSortGraph)
            comp = checkConstraintsWithList(constraints, ans)
            if comp > maxVal:
                maxVal = comp
                maxRet = ans
            if iteration > 100:
                print("FOUND SAT SOL'N")
                return maxRet
            # print(comp)
        iteration += 1
        shuffle(wizards)
        shuffle(constraints)


GRAY, BLACK = 0, 1
def topological(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order

  
#This class represents a directed graph using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    def containsEdge(self, u, v):
        if u in self.graph:
            if v in self.graph[u]:
                return True
        return False
  
    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v]= True
        # print(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)

    def DFSSet(self, v, visited):
        s = set()
        return self.DFSSetUtil(v, visited, s)


    def DFSSetUtil(self, v, visited, s):
        # Mark the current node as visited
        visited[v]= True
        s.add(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSSetUtil(i, visited, s)
        return s


    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited 
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
     
 
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
 
  
  
    # The main function that finds and prints all strongly
    # connected components
    def getSCCs(self):
         
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        # visited =[False]*(self.V)
        visited = dict()
        for u, neighbors in self.graph.items():
            visited[u] = False
            for n in neighbors:
                visited[n] = False
        # Fill vertices in stack according to their finishing
        # times
        # for i in range(self.V):
        #     if visited[i]==False:
        #         self.fillOrder(i, visited, stack)
        for u in visited:
            if visited[u] == False:
                self.fillOrder(u, visited, stack)
 
        # Create a reversed graph
        gr = self.getTranspose()
         
        # Mark all the vertices as not visited (For second DFS)
        # visited =[False]*(self.V)
        visited = dict()
        for u, neighbors in self.graph.items():
            visited[u] = False
            for n in neighbors:
                visited[n] = False
 
        # Now process all vertices in order defined by Stack
        sccs = []
        while stack:
            i = stack.pop()
            if visited[i]==False:
                # gr.DFSUtil(i, visited)
                s = gr.DFSSet(i, visited)
                sccs.append(s)
        return sccs  

def checkConstraintsWithList(constraints, list):
    wizard_map = {}
    for i in range(len(list)):
        wizard_map[list[i]] = i
    return checkConstraintsCount(constraints, wizard_map)

def checkConstraintsCount(constraints, wizard_map):
    result = 0
    for c in constraints:
        if checkConstraint(c, wizard_map):
            result += 1
    return result

#Check every constraint using the wizard dictionary.
def checkConstraints(constraints, wizard_map):
    for c in constraints:
        if not checkConstraint(c, wizard_map):
            return False
    return True
        
#Given the constraints and the wizard dictionary to get ages, check constraint.
def checkConstraint(constraint, wizard_map):
    wiz1 = constraint[0]
    wiz2 = constraint[1]
    wiz3 = constraint[2]
    age1 = wizard_map[wiz1]
    age2 = wizard_map[wiz2]
    age3 = wizard_map[wiz3]
    if age1 == -1 or age2 == -1 or age3 == -1:
        if age1 != -1 and age3 != -1 and age1 == age3:
            return False
        if age2 != -1 and age3 != -1 and age2 == age3:
            return False
        return True
    if age1 < age2:
        return age3 not in range(age1, age2 + 1)
    else:
        return age3 not in range(age2, age1 + 1) 
def solve(num_wizards, num_constraints, wizards, constraints, zakiFirst):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    sameDictionary = []

    constraintToVariable = dict()

    exp = None
    for constraint in constraints:
        wiz1 = constraint[0]
        wiz2 = constraint[1]
        wiz3 = constraint[2]

        clause1 = wiz3 + " " + wiz1
        clause2 = wiz3 + " " + wiz2
        clause3 = wiz1 + " " + wiz3
        clause4 = wiz2 + " " + wiz3

        if clause1 in constraintToVariable:
            v1 = constraintToVariable[clause1]
        else:
            constraintToVariable[clause1] = Variable(clause1)
            v1 = constraintToVariable[clause1]

        if clause2 in constraintToVariable:
            v2 = constraintToVariable[clause2]
        else:
            constraintToVariable[clause2] = Variable(clause2)
            v2 = constraintToVariable[clause2]

        if clause3 in constraintToVariable:
            v3 = constraintToVariable[clause3]
        else:
            constraintToVariable[clause3] = Variable(clause3)
            v3 = constraintToVariable[clause3]

        if clause4 in constraintToVariable:
            v4 = constraintToVariable[clause4]
        else:
            constraintToVariable[clause4] = Variable(clause4)
            v4 = constraintToVariable[clause4]

        literal = ((v1 & v2 & -v3 & -v4) ^ (v3 & v4 & -v1 & -v2))
        if exp is None:
            exp = literal
        else:
            exp = exp & literal
    solver = Minisat()
    solution = solver.solve(exp)
    if solution.success:
        graph = dict()
        for wizard in wizards:
            graph[wizard] = set()
        for constraint in constraintToVariable:
            v = constraintToVariable[constraint]
            if solution[v] == True:
                w = str(v).split()
                vertexU = w[0]
                vertexV = w[1]
                graph[vertexU].add(vertexV)

        cycle = False
        try: topSortGraph = topological(graph)
        except ValueError: cycle = True
    iteration = 0
    graph = {}
    if not cycle:
        return list(topSortGraph)
    else:
        while True:
            dictCompare = {}

            g = Graph(num_wizards)
            for wiz, neighbors in graph.items():
                for n in neighbors:
                    g.addEdge(wiz, n)
            
            badOnes = []
            sccs = g.getSCCs()
            for scc in sccs:
                badGroup = set()
                if len(scc) > 1:
                    for u in scc:
                        for v in scc:
                            if g.containsEdge(u, v):
                                badGroup.add(u + " " + v)
                                g.removeEdge(u, v)

                    badOnes.append(badGroup)
            print("number of cycles:", len(badOnes))
            for count, i in enumerate(badOnes):
                print("length of cycle", count + 1, ":", len(i))

            for group in badOnes:
                lit = None
                for b in group:
                    v = constraintToVariable[b]
                    if lit is None:
                        lit = v
                    else:
                        lit = lit & v
                exp = -(lit) & exp
    

            solver = Minisat()
            solution = solver.solve(exp)
            if solution.success:
                graph = dict()
                for wizard in wizards:
                    graph[wizard] = set()
                for constraint in constraintToVariable:
                    v = constraintToVariable[constraint]
                    dictCompare[v] = solution[v]
                    if solution[v] == True:
                        w = str(v).split()
                        vertexU = w[0]
                        vertexV = w[1]
                        graph[vertexU].add(vertexV)
                cycle = False
                try: topSortGraph = topological(graph)
                except ValueError: cycle = True
            else:
                print("SOMETHING WENT HORRIBLY WRONG")
            if not cycle:
                return list(topSortGraph)
            print("iteration: ", iteration)
            if iteration == 100:
                return solveAlt(num_wizards, num_constraints, wizards, constraints, zakiFirst)
            iteration += 1
            if dictCompare in sameDictionary:
                print("YOU'VE BEEN IN THIS STATE BEFORE")
            else:
                print("new state :)")
                sameDictionary.append(dictCompare)
            




GRAY, BLACK = 0, 1
def topological(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order

  
#This class represents a directed graph using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    def containsEdge(self, u, v):
        if u in self.graph:
            if v in self.graph[u]:
                return True
        return False
  
    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v]= True
        # print(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)

    def DFSSet(self, v, visited):
        s = set()
        return self.DFSSetUtil(v, visited, s)


    def DFSSetUtil(self, v, visited, s):
        # Mark the current node as visited
        visited[v]= True
        s.add(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSSetUtil(i, visited, s)
        return s


    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited 
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
     
 
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
 
  
  
    # The main function that finds and prints all strongly
    # connected components
    def getSCCs(self):
         
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        # visited =[False]*(self.V)
        visited = dict()
        for u, neighbors in self.graph.items():
            visited[u] = False
            for n in neighbors:
                visited[n] = False
        # Fill vertices in stack according to their finishing
        # times
        # for i in range(self.V):
        #     if visited[i]==False:
        #         self.fillOrder(i, visited, stack)
        for u in visited:
            if visited[u] == False:
                self.fillOrder(u, visited, stack)
 
        # Create a reversed graph
        gr = self.getTranspose()
         
        # Mark all the vertices as not visited (For second DFS)
        # visited =[False]*(self.V)
        visited = dict()
        for u, neighbors in self.graph.items():
            visited[u] = False
            for n in neighbors:
                visited[n] = False
 
        # Now process all vertices in order defined by Stack
        sccs = []
        while stack:
            i = stack.pop()
            if visited[i]==False:
                # gr.DFSUtil(i, visited)
                s = gr.DFSSet(i, visited)
                sccs.append(s)
        return sccs  

def checkConstraintsWithList(constraints, list):
    wizard_map = {}
    for i in range(len(list)):
        wizard_map[list[i]] = i
    return checkConstraintsCount(constraints, wizard_map)

#Check every constraint and count
def checkConstraintsCount(constraints, wizard_map):
    result = 0
    for c in constraints:
        if not checkConstraint(c, wizard_map):
            result += 1
    return result

#Check every constraint using the wizard dictionary.
def checkConstraints(constraints, wizard_map):
    for c in constraints:
        if not checkConstraint(c, wizard_map):
            return False
    return True
        
#Given the constraints and the wizard dictionary to get ages, check constraint.
def checkConstraint(constraint, wizard_map):
    wiz1 = constraint[0]
    wiz2 = constraint[1]
    wiz3 = constraint[2]
    age1 = wizard_map[wiz1]
    age2 = wizard_map[wiz2]
    age3 = wizard_map[wiz3]
    if age1 == -1 or age2 == -1 or age3 == -1:
        if age1 != -1 and age3 != -1 and age1 == age3:
            return False
        if age2 != -1 and age3 != -1 and age2 == age3:
            return False
        return True
    if age1 < age2:
        return age3 not in range(age1, age2 + 1)
    else:
        return age3 not in range(age2, age1 + 1) 
"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    zakiOrder = main(sys.argv[1:])
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)

    solution = solve(num_wizards, num_constraints, wizards, constraints, zakiOrder)
    write_output(args.output_file, solution)
