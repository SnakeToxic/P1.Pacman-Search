# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
	#dung stack để duyệt cho đến phần tử sâu nhất
    from util import Stack 
    stack = Stack()
    startNode= problem.getStartState()
    passed = {}
    cost =0
    action = [] #nhung hanh dong cua Pacman
    stack.push((startNode, action,cost)) #push trang thai dau tien vao stack  voi cost =0
    while not stack.isEmpty():
		current =stack.pop()
		if problem.isGoalState(current[0]):
			return current[1]
		#Kiem tra -> neu la diem goalstate thi tra ve vi tri hien hanh la cac day action
		if current[0] not in passed:
			passed[current[0]] = True
			for next, act, co in problem.getSuccessors(current[0]): #đẩy các successor vào stack
				if next and next not in passed:
					stack.push((next, current[1] + [act],current[2] + co))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue #cũng tương tự như DFS, nhưng chúng ta sẽ dùng Queue để duyệt theo từng phần tử cạnh bên
    queue = Queue()
    startNode= problem.getStartState()
    passed = {}
    cost =0
    action = [] 
    queue.push((startNode, action,cost)) 
    while not queue.isEmpty():
		current =queue.pop()
		if problem.isGoalState(current[0]):
			return current[1]
		
		if current[0] not in passed:
			passed[current[0]] = True
			for next, act, co in problem.getSuccessors(current[0]): #Nếu không phải thì đẩy các successor vào queue
				if next and next not in passed:
					queue.push((next, current[1] + [act],current[2] + co))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
	#chung ta ưu tiên đến cost hơn. Thay vì dùng queue như BFS, ta sử dụng PriorityQueue
    from util import PriorityQueue 
    Pr_queue = PriorityQueue()
    startNode= problem.getStartState()
    passed = {}
    cost =0
    action = [] 
    Pr_queue.push((startNode, action,cost),cost) #ưu tiên cost hơn
    while not Pr_queue.isEmpty():
		current =Pr_queue.pop()
		if problem.isGoalState(current[0]): #kiểm tra phần tử hiện hình có phải GoalState không.Nếu phải thì trả về dãy action
			return current[1]
		
		if current[0] not in passed: 
			passed[current[0]] = True
			for next, act, co in problem.getSuccessors(current[0]): #Nếu không phải thì đẩy các successor vào Pr_queue
				if next and next not in passed:
					Pr_queue.push((next, current[1] + [act],current[2] + co), current[2]+ co )
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
	#code xây dựng dựa trên UCS nhưng có điểm khác la từ cost và heuristic ta có thể tìm ra điểm có ưu tiên trước 
    from util import PriorityQueue 
    Pr_queue = PriorityQueue()
    startNode= problem.getStartState()
    passed = {} #điểm đã đi qua rồi.
    cost =0
    action = [] 
    Pr_queue.push((startNode, action,cost),cost) 
    while not Pr_queue.isEmpty():
		current =Pr_queue.pop()
		if problem.isGoalState(current[0]):
			return current[1]
		
		if current[0] not in passed: 
			passed[current[0]] = True
			for next, act, co in problem.getSuccessors(current[0]): 
				if next and next not in passed:
					Pr_queue.push((next, current[1] + [act],current[2] + co), current[2]+ heuristic(next, problem)+ co )
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
