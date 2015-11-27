__author__ = 'Fares'

import util


class WaterJugProblem:
    def __init__(self):
        self.capacities = (4, 3) # the size of the jugs stored in tuple


    def startState(self):
        return (0, 0)

    def isGoal(self, state): # it will test if a certain state is goal state or not
        return state[0] == 2

    def getSuccessors(self, (J1, J2)):  # returns	list	of	successors	to	state
        successors = [] # list
        (C1, C2) = self.capacities
        if(J1 < C1):  successors.append(((C1, J2),'Fill J1', 1)) # the possible operations or moves
        if(J2 < C2):  successors.append(((J1, C2),'Fill J2', 1))
        if J1 > 0:    successors.append(((0, J2),'Dump J1', 1))
        if J2 > 0:    successors.append(((J1, 0),'Dump J2', 1))

        if J1+J2 <= 3:
            alpha=J1+J2
            successors.append(((0,alpha),'Dump J1 into J2',1))
        if J1+J2 <= 4:
            alpha=J1+J2
            successors.append(((alpha,0),'Dump J2 into J1',1))
        if J1+J2 > 4:
            alpha = J1+J2-4
            successors.append(((C1,alpha),'Fill J1 from J2',1))
        if J1+J2 > 3:
            alpha = J1+J2-3
            successors.append(((alpha,C2),'Fill J2 from J1',1))

        return successors


def waterHeurestic(state, problem=None):
    return abs(state[0]-2)


class Node():
    def __init__(self, state, path, cost=0, heuristic=0, problem=None):
        self.state = state
        self.path = path
        self.cost = cost
        self.heuristic = heuristic
        self.problem = problem

    def getSuccessors(self, heuristicFunction=None):
        children = []
        for successor in self.problem.getSuccessors(self.state):
            state = successor[0]
            path = list(self.path)
            path.append(successor[1])
            cost = self.cost + successor[2]
            if heuristicFunction:
                heuristic = heuristicFunction(state, self.problem)
            else:
                heuristic = 0
            node = Node(state, path, cost, heuristic, self.problem)
            children.append(node)
        return children

def nullHeuristic(state, problem=None):
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."

    closed = set()
    Q = util.PriorityQueue()

    startNode = Node(problem.startState(), [], 0, 0, problem)
    Q.push(startNode, startNode.cost + startNode.heuristic)
    visited = 0
    while True:
        if Q.isEmpty():
            return False
        node = Q.pop()
        visited +=1
        if problem.isGoal(node.state):
            print 'expanded',len(closed)
            return node.path
        if node.state not in closed:
            closed.add(node.state)
            for childNode in node.getSuccessors(heuristic):
                Q.push(childNode, childNode.cost + childNode.heuristic)





def test():
    problem = WaterJugProblem()
    print 'waterHeurestic'
    path = aStarSearch(problem,waterHeurestic)
    print 'nullHeuristic'
    path = aStarSearch(problem,nullHeuristic)
    print path



test()
