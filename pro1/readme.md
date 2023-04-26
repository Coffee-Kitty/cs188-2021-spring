

| **Files you'll edit:**               |                                                              |
| ------------------------------------ | ------------------------------------------------------------ |
| `search.py`                          | Where all of your search algorithms will reside.             |
| `searchAgents.py`                    | Where all of your search-based agents will reside.           |
| **Files you might want to look at:** |                                                              |
| `pacman.py`                          | The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project. |
| `game.py`                            | The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid. |
| `util.py`                            | Useful data structures for implementing search algorithms.   |
| **Supporting files you can ignore:** |                                                              |
| `graphicsDisplay.py`                 | Graphics for Pacman                                          |
| `graphicsUtils.py`                   | Support for Pacman graphics                                  |
| `textDisplay.py`                     | ASCII graphics for Pacman                                    |
| `ghostAgents.py`                     | Agents to control ghosts                                     |
| `keyboardAgents.py`                  | Keyboard interfaces to control Pacman                        |
| `layout.py`                          | Code for reading layout files and storing their contents     |
| `autograder.py`                      | Project autograder                                           |
| `testParser.py`                      | Parses autograder test and solution files                    |
| `testClasses.py`                     | General autograding test classes                             |
| `test_cases/`                        | Directory containing the test cases for each question        |
| `searchTestClasses.py`               | Project 1 specific autograding test classes                  |



## Welcome to Pacman

运行游戏：

```
python pacman.py
```

The simplest agent in `searchAgents.py` is called the `GoWestAgent`, which always goes West (a trivial reflex agent). This agent can occasionally win:

```
python pacman.py --layout testMaze --pacman GoWestAgent
```

This agent can occasionally win:

```
python pacman.py --layout testMaze --pacman GoWestAgent
```

![image-20230422133610864](C:\Users\86185\AppData\Roaming\Typora\typora-user-images\image-20230422133610864.png)



But, things get ugly for this agent when turning is required:

```
python pacman.py --layout tinyMaze --pacman GoWestAgent
```

![image-20230422133623497](C:\Users\86185\AppData\Roaming\Typora\typora-user-images\image-20230422133623497.png)

按ctrl + c退出

Note that `pacman.py` supports a number of options that can each be expressed in a long way (e.g., `--layout`) or a short way (e.g., `-l`). You can see the list of all options and their default values via:

```
python pacman.py -h
```



Graph Search Pseudocode

图形搜索伪码

For the search algorithm implementations in q1-3, you will implement the following roughly-written pseudocode for graph search:

```
Algorithm: GRAPH_SEARCH:
frontier = {startNode}
expanded = {}
while frontier is not empty:
    node = frontier.pop()
    if isGoal(node):
        return path_to_node
    if node not in expanded:
        expanded.add(node)
        for each child of node's children:
            frontier.push(child)
return failed
```



## Question 1 (4 points): Finding a Fixed Food Dot using Depth First Search

```
    # 初始化状态
    frontier = util.Stack()
    frontier.push((problem.getStartState(),[]))
    expanded = set()

    # 开始搜索
    while not frontier.isEmpty():
        (curState, preAct) = frontier.pop()
        if problem.isGoalState(curState):
            return preAct
        if curState not in expanded:
            expanded.add(curState)
            children = problem.expand(curState)
            for child in children:
                # 由于是图搜索，所以加入时还要判
                if child[0] not in expanded:
                    frontier.push(([child[0], preAct + [child[1]]]))
```

DFS总是优先拓展更深的节点  ， 更深可以由栈来决定

假设共n个节点，每个节点有d个后继节点

时间复杂度：

O(n的d次方)

空间复杂度：

O(n*d)      因为退栈操作，不会保存已经失败的节点

## Question 2 (4 points): Breadth First Search

```
frontier = [(util.Queue(),[])]
expanded = []

frontier.append(problem.getStartState())

while len(frontier)!=0:
    state, preAct = frontier.pop()
    if problem.isGoalState(state):
        return preAct
    if not state in expanded:
        childern = problem.expand(state)
        for child in childern:
            if not child in expanded:
                frontier.append((child[0],preAct+child[1]))
```

BFS总是优先拓展 代价更小的节点（将所有的代价看作1）

时间复杂度：

O(n的d次方)

空间复杂度：

O(n的d次方)

## Question 3 (4 points): A* search

A*搜索 f(n)=g(n)+h(n)

g(n)指从起始节点出发到达第n个节点的真实代价

h(n)指从第n个节点到最近的目标节点的代价的估计

h*(n)指实际代价

可纳性：需保证0<h(n)<h*(n)     

一致性：需保证 当n1 是 n的后继节点时，有 h(n)-h(n1)<=cost_edge(n到n1)

```
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # 初始化
    frontier = util.PriorityQueue()  # 这是提供好的最小优先队列
    expanded = set()
    frontier.push((problem.getStartState(), [], 0), 0)

    while not frontier.isEmpty():
        (state, preAct, preCost) = frontier.pop()
        if problem.isGoalState(state):
            return preAct
        # 如果该状态没有被拓展过
        if state not in expanded:
            # 扩展该节点
            children = problem.expand(state)
            expanded.add(state)  # 做好标记
            # 图搜索所以需要查看扩展好的节点是否已经被拓展 否则加入frontier  权值由启发函数给出
            for child in children:
                if child[0]not in expanded:
                    cost = preCost + child[2] + heuristic(child[0], problem)
                    frontier.push((child[0], preAct+[child[1]], preCost + child[2]), cost)
```



当启发函数等于0时，退化成UCS一致代价搜索，当代价都是1时，就成了BFS

## Question 4 (3 points): Finding All the Corners

定义到达四个角的问题描述

```
class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and child function
    """

    def __init__(self, startingGameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0 # DO NOT CHANGE; Number of search nodes expanded
        # Please add any code here which you would like to use
        # in initializing the problem
        """
        定义状态空间为: (当前位置, [已经经过的四个角落的位置])
        """
        self.stateSpace = (self.startingPosition, ())  # tuple才可以hash 加入set()
        self.startingGameState = startingGameState
        "*** YOUR CODE HERE ***"

    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        "*** YOUR CODE HERE ***"
        return self.stateSpace

    def isGoalState(self, state):
        """
        Returns whether this search state is a goal state of the problem.
        """
        "*** YOUR CODE HERE ***"
        # (position, visit_nodes) = state
        # for corner in self.corners:
        #     if corner not in visit_nodes:
        #         return False
        return len(state[1]) == 4

    def expand(self, state):
        """
        Returns child states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (child,
            action, stepCost), where 'child' is a child to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that child
        """

        children = []
        for action in self.getActions(state):
            # Add a child state to the child list if the action is legal
            # You should call getActions, getActionCost, and getNextState.
            "*** YOUR CODE HERE ***"
            next_state = self.getNextState(state, action)
            stepCost = self.getActionCost(state, action, next_state)
            children.append((next_state, action, stepCost))

        self._expanded += 1 # DO NOT CHANGE
        return children

    """
    返回当前状态可以进行的合法 action
    """
    def getActions(self, state):
        possible_directions = [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]
        valid_actions_from_state = []
        for action in possible_directions:
            x, y = state[0]
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                valid_actions_from_state.append(action)
        return valid_actions_from_state

    """
    返回从一个状态采取某个action的花费
    """
    def getActionCost(self, state, action, next_state):
        assert next_state == self.getNextState(state, action), (
            "Invalid next state passed to getActionCost().")
        return 1

    def getNextState(self, state, action):
        assert action in self.getActions(state), (
            "Invalid action passed to getActionCost().")
        x, y = state[0]
        dx, dy = Actions.directionToVector(action)
        nextx, nexty = int(x + dx), int(y + dy)
        "*** YOUR CODE HERE ***"

        for corner in self.corners:
            if corner == (nextx, nexty):
                if corner not in state[1]:
                    return (nextx, nexty), tuple(list(state[1]) + [(nextx, nexty)])
        return (nextx, nexty), state[1]



    def getCostOfActionSequence(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)
```

## Question 5 (3 points): Corners Problem: Heuristic

定义启发函数

这里的启发函数设置为了到四个角落的实际迷宫距离的最大值

很明显是可纳的

而且，h(n1)-h(n)=cos_edge(n到n1) 也是一致的

```
def cornersHeuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)
    "*** YOUR CODE HERE ***"
    """
    admissible 用曼哈顿距离得出 h>0
    启发函数 是从当前节点到目标状态的估计
    这里我们就用max(到四个节点的距离) 作为启发函数
    consistency 当前状态的启发值 应小于等于 孩子节点的启发值加上cost(当前状态，孩子节点)
    """
    (position, visit_nodes) = state
    """
    曼哈顿距离拓展节点太多了  Heuristic resulted in expansion of 33112 nodes
    """
    # for corner in corners:
    #     if corner not in visit_nodes:
    #         heur = max(heur, util.manhattanDistance(corner, position))
    """
    用下面提供好的迷宫距离函数  这不就h接近h* 了。。
    """
    unvisited = [corner for corner in corners if corner not in visit_nodes]
    if len(unvisited) == 0:
        return 0
    dis_list = []
    for corner in unvisited:
        dis_list.append(mazeDistance(corner, position, problem.startingGameState))
    if len(dis_list) > 0:
        return max(dis_list)    # 因为最终状态是取得四个食物  这里我们就用max(食物)做启发试试 978nodes
    return 0  # Default to trivial solution
```

## Question 6 (4 points): Eating All The Dots

设计吃掉所有dots的启发函数

同上，目标状态是吃完dot，我们就选当前状态到剩下dot的最大距离做启发

```
def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come
    up with an admissible heuristic; almost all admissible heuristics will be
    consistent as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the
    other hand, inadmissible or inconsistent heuristics may find optimal
    solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a Grid
    (see game.py) of either True or False. You can call foodGrid.asList() to get
    a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the
    problem.  For example, problem.walls gives you a Grid of where the walls
    are.

    If you want to *store* information to be reused in other calls to the
    heuristic, there is a dictionary called problem.heuristicInfo that you can
    use. For example, if you only want to count the walls once and store that
    value, try: problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access
    problem.heuristicInfo['wallCount']
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    # 判断是否达到目标状态
    foodList = foodGrid.asList()  # 食物list [(x,y)]
    if len(foodList) == 0:
        return 0

    # 用mazeDistance做启发
    cost = [mazeDistance(position, food, problem.startingGameState) for food in foodList]
    if len(cost) > 0:
        return max(cost)  # 最后 4137 nodes

    return 0
```

## Question 7 (3 points): Suboptimal Search

实现总是吃掉最近的dot，就简单采用bfs，用bfs最先得到的一定是最近的

```
def isGoalState(self, state):
    """
    The state is Pacman's position. Fill this in with a goal test that will
    complete the problem definition.
    """
    x,y = state

    "*** YOUR CODE HERE ***"
    return (x, y) in self.food.asList()
```

```
def findPathToClosestDot(self, gameState):
    """
    Returns a path (a list of actions) to the closest dot, starting from
    gameState.
    """
    # Here are some useful elements of the startState
    startPosition = gameState.getPacmanPosition()
    food = gameState.getFood()
    walls = gameState.getWalls()
    problem = AnyFoodSearchProblem(gameState)

    "*** YOUR CODE HERE ***"
    """
    bfs最先找到的点一定是最近的点
    """
    return search.bfs(problem)
```
