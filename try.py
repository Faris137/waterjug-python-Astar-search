__author__ = 'Fares'

import util


class WaterJugProblem:
    def __init__(self):
        self.capacites = (4, 3)
        self.statesCount =1

    def startState(self):
        return (0, 0)

    def isGoal(self, state):
        return state[0] == 2

    def getSuccessors(self, (J1, J2)):  # returns	list	of	successors	to	state
        successors = []
        (C1, C2) = self.capacites
        if(J1 < C1):  successors.append(((C1, J2),'Fill J1', 1))
        if(J2 < C2):  successors.append(((J1, C2),'Fill J2', 1))
        if J1 > 0:    successors.append(((0, J2),'Dump J1', 1))
        if J2 > 0:    successors.append(((J1, 0),'Dump J2', 1))
        if J2 < C2 and J1 > 0:
            delta = min(J1, C2 - J2)
            successors.append(((J1 - delta, J2 + delta),'Pour J1 into J2', 1))
        if J1 < C1 and J2 > 0:
            delta = min(J2, C1 - J1)
            successors.append(((J1 + delta, J2 - delta),'pour J2 into J1', 1))

        self.statesCount += len(successors)
        return successors


class Node():
    """
    A container storing the current state of a node, the list
    of  directions that need to be followed from the start state to
    get to the current state and the specific problem in which the
    node will be used.
    """

    def __init__(self, state, path, cost=0, heuristic=0, problem=None):
        self.state = state
        self.path = path
        self.cost = cost
        self.heuristic = heuristic
        self.problem = problem

    def __str__(self):
        string = "Current State: "
        string += self.__str__(self.state)
        string += "\n"
        string == "Path: " + self.path + "\n"
        return string

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
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."

    closed = set()
    fringe = util.PriorityQueue()

    startNode = Node(problem.startState(), [], 0, 0, problem)
    fringe.push(startNode, startNode.cost + startNode.heuristic)

    while True:
        if fringe.isEmpty():
            return False
        node = fringe.pop()
        if problem.isGoal(node.state):
            return node.path
        if node.state not in closed:
            closed.add(node.state)
            for childNode in node.getSuccessors(heuristic):
                fringe.push(childNode, childNode.cost + childNode.heuristic)



def test():
    problem = WaterJugProblem()
    path = aStarSearch(problem)
    print path
    print problem.statesCount


test()