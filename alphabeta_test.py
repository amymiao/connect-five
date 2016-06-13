from alphaBeta import *

def heur_func():
    pass

def goal_func():
    pass

class arb_node():
    max_value = 0
    min_value = 1
    empty_value = -1

    def __init__(self, action, alpha, beta, min_node = False, value = None):
        self.action = action
        self.alpha = alpha
        self.beta = beta
        self.value = value
        self.min_node = min_node
        self.depth = float("inf")
        self.descs = list()
        self.debug_file = open("AlphaBetaDebug0.txt", "w")
        self.board_state = [[-1] * 10 for i in range(10)]

    def input_descs(self, descs):
        self.descs.extend(descs)

    def generate_descendant_states(self, goal, heur):
        return list(self.descs)

if __name__ == "__main__":
    node1 = arb_node("left", -1*float("inf"), float("inf"), value=4)
    node2 = arb_node("middle", -1*float("inf"), float("inf"), value=-9)
    node3 = arb_node("right", -1*float("inf"), float("inf"), value=-3)

    node4 = arb_node("left", -1*float("inf"), float("inf"), value=-16)
    node5 = arb_node("middle", -1*float("inf"), float("inf"), value=-16)
    node6 = arb_node("right", -1*float("inf"), float("inf"), value=-18)

    node7 = arb_node("left", -1*float("inf"), float("inf"), value=-2)
    node8 = arb_node("middle", -1*float("inf"), float("inf"), value=9)
    node9 = arb_node("right", -1*float("inf"), float("inf"), value=8)

    node10 = arb_node("left", -1*float("inf"), float("inf"), True)
    node10.input_descs([node1, node2, node3])
    node11 = arb_node("middle", -1*float("inf"), float("inf"), True)
    node11.input_descs([node4, node5, node6])
    node12 = arb_node("right", -1*float("inf"), float("inf"), True)
    node12.input_descs([node7, node8, node9])

    node13 = arb_node("root", -1*float("inf"), float("inf"))
    node13.input_descs([node10, node11, node12])

    tree = AlphaBetaTree(10, heur_func, goal_func, float("inf"))
    print(tree.alphaBetaPruning(node13))
    tree.complete_game()