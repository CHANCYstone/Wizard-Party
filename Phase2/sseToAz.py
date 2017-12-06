import argparse
import sys
from satispy import Variable, Cnf 
from satispy.solver import Minisat
from collections import deque
from collections import defaultdict
from random import shuffle

"""
======================================================================
  Complete the following function.
======================================================================
"""
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
    return constraintDict
    #currWizards,
    
    #wizards

def main(argv):
    #print "Hello!"
    if len(argv) != 2:
        print("Usage: python solver.py [path_to_input#.py] [path_to_output#.py]")
        return#need to create .out beforehand
    #print "Hey!"
    return processInput(argv[0], argv[1])

def solve(num_wizards, num_constraints, wizards, constraints, constraintDiction):
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

    #constraintDict = {}

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
        graph = {}
        if not cycle:
            ans = list(topSortGraph)
            comp = checkConstraintsWithList(constraints, ans)
            if comp > maxVal:
                maxVal = comp
                maxRet = ans
            if iteration > 100:
                return az(maxRet,constraintDiction) #maxRet
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

def az(solution,constraintDict):

    output_ordering = solution
    #currWizards = list(solution)
    #list(currWizards)
    output_ordering_map = {k: v for v, k in enumerate(output_ordering)}
    constraints_satisfied = 0
    constraints_failed = {}
    #print currWizards
    #print constraintDict
    currentCsSatfied = 0
    for i in range(len(constraintDict)):
        cd = constraintDict[i]
        #print cd

        oom = output_ordering_map
        cwiz_a = oom[cd[0]]
        cwiz_b = oom[cd[1]]
        cwiz_mid = oom[cd[2]]
        if (cwiz_a < cwiz_mid < cwiz_b):
            constraints_failed[i] = True
            currentCsSatfied += 1 
        elif (cwiz_b < cwiz_mid < cwiz_a):
            constraints_failed[i] = False
            currentCsSatfied += 1 
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
            for i,tlw in enumerate(output_ordering):
                if tlw == fcwiz_b:
                    posb = i
                if tlw == fcwiz_mid:
                    posm = i
                if tlw == fcwiz_a:
                    posa = i
            distToB = abs(posm - posb)
            distToA = abs(posm - posa)
            #currWizards = tempListVersion
            testerA = 0
            testerB = 0
            testerC = 0
            testerD = 0
            #VKV
            #tester x = (amount of c's solved using method x) - (currentCsSatfied) 
            # if A,B,C < 0, do nothing
            output_ordering1 = output_ordering
            output_ordering1.insert(posa, (output_ordering1.pop(posm)))
            for i in range(len(constraintDict)):
                cd = constraintDict[i]
                #print cd
                output_ordering_map = {k: v for v, k in enumerate(output_ordering1)}
                oom = output_ordering_map
                cwiz_a = oom[cd[0]]
                cwiz_b = oom[cd[1]]
                cwiz_mid = oom[cd[2]]
                if (cwiz_a < cwiz_mid < cwiz_b):
                    testerA += 1
                elif (cwiz_b < cwiz_mid < cwiz_a):
                    testerA += 1
            testerA = testerA - currentCsSatfied 
            output_ordering2 = output_ordering
            output_ordering2.insert(posb, output_ordering2.pop(posm))
            for i in range(len(constraintDict)):
                cd = constraintDict[i]
                #print cd
                output_ordering_map = {k: v for v, k in enumerate(output_ordering2)}
                oom = output_ordering_map
                cwiz_a = oom[cd[0]]
                cwiz_b = oom[cd[1]]
                cwiz_mid = oom[cd[2]]
                if (cwiz_a < cwiz_mid < cwiz_b):
                    testerB += 1
                elif (cwiz_b < cwiz_mid < cwiz_a):
                    testerB += 1
            testerB = testerB - currentCsSatfied
            output_ordering3 = output_ordering
            output_ordering3.insert(posb, output_ordering3.pop(posm))
            for i in range(len(constraintDict)):
                cd = constraintDict[i]
                #print cd
                output_ordering_map = {k: v for v, k in enumerate(output_ordering3)}
                oom = output_ordering_map
                cwiz_a = oom[cd[0]]
                cwiz_b = oom[cd[1]]
                cwiz_mid = oom[cd[2]]
                if (cwiz_a < cwiz_mid < cwiz_b):
                    testerC += 1
                elif (cwiz_b < cwiz_mid < cwiz_a):
                    testerC += 1
            testerC = testerC - currentCsSatfied
            if ((testerA < 0) and (testerB < 0) and (testerC < 0)):
                output_ordering =  output_ordering
            elif ((testerA <= testerB) and (testerB >= testerC)):
                output_ordering = output_ordering2
            elif ((testerA <= testerC) and (testerC >= testerB)):
                output_ordering = output_ordering3
            elif ((testerB <= testerA) and (testerA >= testerC)):
                output_ordering = output_ordering1


    return output_ordering
  
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
    consDict = main(sys.argv[1:])
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
###TEST
    # cycle = True
    # solution = None
    # while cycle == True:
    #     try: solution = solve(num_wizards, num_constraints, wizards, constraints)
    #     except ValueError: 
    #         cycle = True
    #         print("cycle")
    #         continue
    #     cycle = False
###ENDTEST
    solution = solve(num_wizards, num_constraints, wizards, constraints,consDict)
    write_output(args.output_file, solution)