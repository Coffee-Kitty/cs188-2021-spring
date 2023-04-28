# multiAgents.py
# --------------
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
import math

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """
        在游戏"Pacman"中，当Pacman吃下大力丸（Power Pellet）时，所有的鬼魂（ghost）都会变得害怕，并且变成蓝色，
        此时Pacman可以吃掉它们获得额外的分数。这种状态通常被称为“吃豆人（Pacman）的超级状态（Super Mode）”。
        在这个状态下，鬼魂也不会再袭击Pacman，而是试图逃离他的视线。这种状态通常持续几秒钟，然后鬼魂会恢复正常。
        
        """

        # # 求出最近的鬼怪，计算危险值
        # nearestGhost = min([manhattanDistance(newPos, ghostState.configuration.pos) for ghostState in newGhostStates])
        # # 为了让吃豆人不要总是躲着鬼怪，我们只考虑距离2步以内的鬼怪造成的影响
        # # 为什么取-20？因为接下来我会把豆豆的启发值设置在10以内，两者相加一定为负数，这样就可以抵消豆豆对吃豆人的诱惑，^_^
        # # 为什么不是-10？因为如果下一步直接吃到豆豆，那个successorGameState.getScore()会算上吃到豆豆的10分
        # dangerScore = -20 if nearestGhost < 2 else 0
        #
        # # 如果豆豆还没有吃光，用最近的豆豆的坐标计算出一个启发值，优先考虑吃掉最近的豆豆
        # # 这个程序从字面上看，是用曼哈顿距离计算启发值，所以如果吃豆人和豆豆之间有墙的话……吃豆人就卡在墙后面了
        # # 但是，又因为有鬼怪的存在，它会驱动吃豆人离开卡死在墙后面的状态，勉强算是通过测试了
        # if len(newFood.asList()) > 0:
        #     nearestFood = (min([manhattanDistance(newPos, food) for food in newFood.asList()]))
        #     # 为什么启发值是“9/距离”呢？因为按照我的设计，这个值不能为负数，负数用来表示下一步可能遇到鬼怪
        #     # 同时，因为吃到隔壁的豆豆得9分(移动需要扣1分)，且距离越远启发值越小，按照这些规则，我就设计了这样一个启发函数
        #     # 如果下一个豆豆就在隔壁，距离为1，那么启发值为9，且距离放在分母，其值越大，启发值就越小，OK！
        #     foodHeuristic = 9 / nearestFood
        # else:
        #     foodHeuristic = 0
        #
        # # 把计算好的各种值加起来，并返回
        # # print("Action:",action,"Score:",successorGameState.getScore(),"Danger:",dangerScore,"Food:",foodHeuristic,"Total:",successorGameState.getScore()+foodHeuristic+dangerScore)
        # return  childGameState.getScore() + foodHeuristic + dangerScore

        """
        当ghost临近优先躲避ghost
        其次优先吃最近的豆豆
        设计如果ghost离2步近 -20   再设计吃豆豆 +10(由child.getScore()得出) 这样负数表示有潜在危险
        """
        score = childGameState.getScore()
        fod_dis = [manhattanDistance(newPos,food) for food in newFood.asList()]
        if len(fod_dis) > 0:
            min_fo_dis = min(fod_dis)
            score += 9 /min_fo_dis
        nearghost = min([manhattanDistance(newPos, ghost.configuration.pos) for ghost in newGhostStates])
        score -= 20 if nearghost < 2 else 0
        return score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def terminate(self, gamestate, depth):
        return gamestate.isWin() or gamestate.isLose() or depth == self.depth

    def get_min(self, gamestate, depth, agent_index=1):
        if self.terminate(gamestate, depth):
            return self.evaluationFunction(gamestate)
        # 获得鬼怪的下一步操作
        actions = gamestate.getLegalActions(agent_index)
        if len(actions) == 0:
            return self.evaluationFunction(gamestate)
        value = float("inf")
        # 遍历所有ghost 递归调用 得出最小值
        for action in actions:
            # 如果当前已经是最后一只鬼怪，那么下一轮就该是计算吃豆人的行为了，即调用MAX函数
            if agent_index == gamestate.getNumAgents() - 1:
                value = min(value,self.get_max(gamestate.getNextState(agent_index, action), depth + 1))
            else:
                value = min(value,self.get_min(gamestate.getNextState(agent_index, action), depth, agent_index + 1))
        return value

    def get_max(self, gamestate, depth, agent_index=0):
        if self.terminate(gamestate, depth):
            return self.evaluationFunction(gamestate)
        # pacman可以采取的动作
        # print(f"getMax depth{depth}")
        pac_actions = gamestate.getLegalActions(agent_index)
        if len(pac_actions) == 0:
            return self.evaluationFunction(gamestate)
        score = float("-inf")
        for action in pac_actions:
            value = self.get_min(gamestate.getNextState(0, action), depth, 1)
            if value is not None and value > score:
                score = value
        return score

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        """
        self.depth代表 max-min树的深度
        对于pacman 需要在各个ghost针对子动作采取动作后的值中挑一个最大的子动作
        对于ghost  需要在pacman针对子动作采取动作后的值中挑一个最小的
        """

        # 将最大值初始定义为负无穷大
        maxVal = float('-inf')
        bestAction = None
        for action in gameState.getLegalActions(0):
            # 求出接下来的所有MIN值，并和maxVal比较，求出MAX值
            value = self.get_min(gameState.getNextState(0, action), 0, 1)
            # 满足条件则更新maxVal值，并记下bestAction
            if value is not None and value > maxVal:
                maxVal = value
                bestAction = action
        return bestAction
        # 开始实际调用函数，
        # 注意：虽然要求最大利益的pcman走法，但这里必须调用min_value,
        # 因为这里实际模拟了最后的max_value操作，因为我们要返回的终极目标是getAction()-->action
        # 运用列表排序，十分巧妙的提取最大值所对应的action即最后return res[-1][0]
        # res = [(action, self.get_min(gameState.getNextState(0, action), 0, 1)) for action in
        #        gameState.getLegalActions(0)]
        # res.sort(key=lambda k: k[1])
        #
        # return res[-1][0]

        # util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        ghosts =[i for i in range(1, gameState.getNumAgents())]

        def term(state,depth):
            return state.isWin() or state.isLose() or depth == self.depth

        def get_min(state, depth, ghost,a,b):
            if term(state,depth):
                return self.evaluationFunction(state)
            # 针对pac采取动作后的state状态
            v = float("inf")
            actions = state.getLegalActions(ghost)
            for action in actions:
                if ghost == ghosts[-1]:
                    v = min(v, get_max(state.getNextState(ghost, action),depth+1,a,b))
                else:
                    v = min(v, get_min(state.getNextState(ghost, action), depth, ghost+1,a,b))
                if v < a:  # 如果得到一个比 阿尔法小的值 减支
                    return v
                b = min(b, v)
            return v
        def get_max(state,depth,a,b):
            if term(state, depth):
                return self.evaluationFunction(state)
            v = float("-inf")
            actions = state.getLegalActions(0)
            for action in actions:
                v = max(v, get_min(state.getNextState(0, action),depth,1,a,b))
                if v > b:
                    return v
                a = max(a, v)
            return v


        a=float("-inf")
        b=-a
        v=a
        actions = gameState.getLegalActions(0)
        res_act = None
        for action in actions:
            temp = get_min(gameState.getNextState(0,action),0,1,a,b)
            if temp > v:
                v = temp
                res_act = action
            if v > b:
                return v
            a = max(v,a)
        return res_act
        # util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def term(state, depth):
            return depth == self.depth or state.isWin() or state.isLose()

        def exp_value(state,depth,ghost_index=1):
            if term(state,depth):
                return self.evaluationFunction(state)
            actions = state.getLegalActions(ghost_index)
            v = 0
            p = 1.0 / len(actions)
            if len(actions) == 0:
                return self.evaluationFunction(state)
            for action in actions:
                next_state = state.getNextState(ghost_index,action)
                if ghost_index == state.getNumAgents() - 1:
                    v += p*get_max(next_state,depth+1)
                else:
                    v += p*exp_value(next_state,depth,ghost_index+1)
            return v

        def get_max(state,depth):
            if term(state,depth):
                return self.evaluationFunction(state)
            actions = state.getLegalActions(0)
            v = float("-inf")
            if len(actions) == 0:
                return self.evaluationFunction(state)
            for action in actions:
                next_state = state.getNextState(0, action)
                v = max(v, exp_value(next_state,depth,1))
            return v

        value = float("-inf")
        act = None
        actions = gameState.getLegalActions(0)
        for action in actions:
            next_state = gameState.getNextState(0, action)
            temp = exp_value(next_state,0,1)
            if temp > value:
                act = action
                value = temp
        return act
        # util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>

    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    walls = currentGameState.getWalls()

    # 如果不是新的ScaredTimes，则新状态为ghost：返回最低值

    newFood = newFood.asList()
    ghostPos = [(G.getPosition()[0], G.getPosition()[1]) for G in newGhostStates]
    scared = min(newScaredTimes) > 0

    if currentGameState.isLose():
        return float('-inf')

    if newPos in ghostPos:
        return float('-inf')

    # 如果不是新的ScaredTimes，则新状态为ghost：返回最低值

    closestFoodDist = sorted(newFood, key=lambda fDist: util.manhattanDistance(fDist, newPos))
    closestGhostDist = sorted(ghostPos, key=lambda gDist: util.manhattanDistance(gDist, newPos))

    score = 0

    fd = lambda fDis: util.manhattanDistance(fDis, newPos)
    gd = lambda gDis: util.manhattanDistance(gDis, newPos)

    if gd(closestGhostDist[0]) < 3: # 距离最近的ghost太近扣分
        score -= 300
    if gd(closestGhostDist[0]) < 2:
        score -= 1000
    if gd(closestGhostDist[0]) < 1:
        return float('-inf')

    if len(currentGameState.getCapsules()) < 2: # 鼓励吃胶囊
        score += 100

    if len(closestFoodDist) == 0 or len(closestGhostDist) == 0:
        score += scoreEvaluationFunction(currentGameState) + 10
    else:
        score += (scoreEvaluationFunction(currentGameState) + 10 / fd(closestFoodDist[0]) + 1 / gd(
            closestGhostDist[0]) + 1 / gd(closestGhostDist[-1]))

    return score


# Abbreviation
better = betterEvaluationFunction
