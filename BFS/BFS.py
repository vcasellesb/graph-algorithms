from math import inf
from Graph import Graph, Vertex
from typing import Tuple, Union
from collections import deque
import numpy as np
from utils.helpers import help_start


##########################
# Naive implementation of a BFS algorithm as seen on
# https://www.baeldung.com/cs/graph-number-of-shortest-paths
# Please don't roast me. This is done with the sole purpose
# of learning about graphs and understanding algorithms
# by implementing them. For supersuper sure there are better 
# ways of doing this. I'm just trying to learn.


# How does this algorithm work?
# We need two arrays (dictionaries), one to store the 
# distances, one to store the paths (both for each node).

class naiveBFS:
    # Should I give the adjacency matrix / graph at initialization of the walker object?
    # or when calling the run() method?
    def __init__(self):

        # queue where we'll store the nodes
        self._queue = deque()


    def _initialize_ds_ps(self, graph: Graph) -> Tuple[dict]:
        """
        We initialize the distances and paths arrays as infinity 
        and 0 for each node, respectively
        """
        distances = dict()
        paths = dict()
        for node in graph.nodes:
            distances[node._toint()] = inf
            paths[node._toint()] = 0

        return distances, paths

    def start(self, source: Vertex):
        """
        At start of the walk, we do three things:
            * add the starting node (or source) to the queue
            * set dist[source] to 0
            * set path[source] to 1
        """
        
        self._queue.append(source)

        lab = source._toint()
        source._visited = True
        self._distances[lab] = 0
        self._paths[lab] = 1

    def run(self, graph: Graph, source: Union[int, Vertex], dest: Vertex):

        """
        TODO: SOLVE HOW SOURCE AND DEST ARE GIVEN
        """

        self._distances, self._paths = self._initialize_ds_ps(graph)

        source = help_start(start=source, graph=graph, allowNone=False)
        self.start(source=source)

        while len(self._queue) > 0:
            # This gets first element in queue and removes it. Neat
            current = self._queue.popleft()

            for neigh in current.passages:
                neigh = graph.get_node_from_label(neigh)

                if not neigh._visited:
                    self._queue.append(neigh)
                    neigh._visited = True
                
                # This is ugly AF                
                if self._distances.get(neigh._toint()) > \
                    self._distances.get(current._toint()) + 1:

                    self._distances[neigh._toint()] = self._distances[current._toint()] + 1
                    self._paths[neigh._toint()] = self._paths[current._toint()]
                
                elif self._distances.get(neigh._toint()) == \
                    self._distances.get(current._toint()) + 1:

                    self._paths[neigh._toint()] += self._paths[current._toint()]
        
        return self._paths[dest._toint()]


if __name__ == "__main__":

    testfile = np.load('tests/tests.npz')
    for ar in testfile.files:
        A = testfile[ar]
        graph = Graph(A)
        bfs = naiveBFS()        
        results = bfs.run(graph, source=0, dest=graph.get_node_from_label(3))
        print(results)
            