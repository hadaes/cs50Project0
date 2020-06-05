class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():

    discovered = []

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
        x = (node.action, node.state)
        self.discovered.append(x)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def discovered_tuple(self, x):
        if x in self.discovered:
            return 1
        else:
            return 0

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
