from collections import deque

class Node:
    def __init__(self, state, action=-1, cost=0, parent=None):
        self.State = state
        self.Action = action
        self.Cost = cost
        self.Parent = parent

def Test(node, goal, states):
    for index in range(len(states)):
        # checking that weather the initial state is in the states's list or not
        if goal == states[index]:
            if node.State == index:
                return True
            else:
                return False


MNT = str(input("Please Enter M N T : "))
MNT = MNT.split()
M = int(MNT[0])
N = int(MNT[1])
T = int(MNT[2])


states = []
Actions = []
transition_model = []
print("Please enter the all of the States : ")
for i in range(M):
    states.append(input())
print("Please enter the all of the actions")
for i in range(N):
    Actions.append(input())
print("Please Enter the Transition Model")
for i in range(M):
    row = []
    row = input().split()
    row = [int(z) for z in row]
    transition_model.append(row)
def search_problem(problem):

    for index in range(len(states)):

        if problem[0] == states[index]:
            FirstNode = Node(index)
            frontier = deque([FirstNode])
            Explored_Set = set()
    solution = []
    while True:
        if frontier is not None:
            node = frontier.popleft()
            Explored_Set.add(node.State)
            if Test(node, problem[1], states):
                return solution
            else:
                Ccrrent_node_children = transition_model[node.State]
                for child in range(len(Ccrrent_node_children)):
                    child_node = Node(int(Ccrrent_node_children[child]), child, node.Cost + 1, node)
                    if child_node.State not in Explored_Set and child_node not in frontier:
                        solution.append(Actions[child])
                        if Test(child_node, problem[1], states):
                            return solution
                        frontier.append(child_node)
                        break
        else:
            return None


def Main():
    print("Please Enter the test You want to Test : ")
    for Test_case in range(T):
        start = input().split("\t")
        sol = search_problem(start)
        for actions in range(len(sol)):
            print(sol[actions], end="")
            if actions is not len(sol) - 1:
                print("->", end="")
        print("")

Main()