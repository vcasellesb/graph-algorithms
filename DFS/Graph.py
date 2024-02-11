import numpy as np
from tremaux import A

class Graph(object):

    def __init__(self, A: np.ndarray):
        
        # Adjacency matrix (should be square matrix)
        self.A = A

        # we generate all nodes
        self.nodes = list()
        for n in range(len(A[0])):
            passages = self._set_passages(A=A, label=n)
            v = Vertix(label=n, passages=passages)
            self.nodes.append(v)


    def _set_passages(self, A: np.ndarray, label: int):

        # we get the vertices this one is connected to
        conn = np.nonzero(A[label])[0]

        return set(conn)       



class Vertix(object):

    def __init__(self, label: int, passages: set):
        self.label = label
        self._visited = False
        self.passages = passages 
        



if __name__ == "__main__":

    graph = Graph(A)

    for node in graph.nodes:
        print(f'Node with label: {node.label}')
        print(f'This node has the following passages: {node.passages}')

        # I'm the fucking best

