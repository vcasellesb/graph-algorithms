import numpy as np
from typing import Set

########################################
# Here, I'll store the base Graph class
########################################

class Vertex(object):

    def __init__(self, label: int, passages: set):
        self.label = label
        self._visited = False ## This should be specified when initializing each walker. Bad puppy, Vicent
        self.passages = passages # this is called passages but it may as well be called neighbours. Tomato, tomatoe
    
    def __str__(self):
        return f'{self.label}'
    
    def _toint(self):
        return self.label

class Graph(object):

    # TODO: Uncouple Graph and Vertex from Tremaux Walker

    def __init__(self, A: np.ndarray):
        # Adjacency matrix (should be square matrix)
        self.A = A

        # we generate all nodes
        self.nodes = list()
        for n in range(len(A[0])):
            passages = self._set_passages(A=A, label=n)
            v = Vertex(label=n, passages=passages)
            self.nodes.append(v)

    def _set_passages(self, A: np.ndarray, label: int) -> Set:

        # we get the vertices this one is connected to
        conn = np.nonzero(A[label])[0]

        return set(conn)

    def get_node_from_label(self, label: int) -> Vertex:
        """Makes it easy to find nodes"""

        for node in self.nodes:
            if node.label == label:
                return node
        
        raise Exception('Node not found')
        
A = np.array([[0, 1, 0, 1],
              [1, 0, 1, 1],
              [0, 1, 0, 0],
              [1, 1, 0, 0]])

if __name__ == "__main__":

    graph = Graph(A)
    for node in graph.nodes:
        print(f'Node with label: {node.label}')
        print(f'This node has the following passages: {node.passages}')

        # I'm the fucking best