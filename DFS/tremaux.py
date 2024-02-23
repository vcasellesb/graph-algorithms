from Graph import Graph, Vertex
import random
import numpy as np
import time
from typing import Union
from utils.helpers import help_start

class TremauxAlgorithm:

    def __init__(self, DELAY:int=1):

        self.DELAY = DELAY
        self._isDone = False
        self.n_step = 0
    
    def _initialize_node_passage_state(self, graph: Graph):

        """
        Initializes the dictionary where we'll 
        store the marks for our edges (or passages)
        """
        states = dict()

        for node in graph.nodes:
            states[node.label]=dict.fromkeys(node.passages)
            
        self.state = states
        
        return self
    
    def decide(self, neighbors: dict) -> Union[int, None]:
        """
        Neighbors is a dictionary with node labels as keys, 
        states of nodes as values
        """

        empties = [k for k in neighbors.keys() if neighbors[k] is None]

        if len(empties) >= 1: return random.choice(empties)
        
        # if this runs then we have no empty passage.
        # we apply the same logic as before
        effed = [k for k in neighbors.keys() if neighbors[k] == "F"]

        if len(effed) >= 1: return random.choice(effed)
        else: return None

    def step(self, graph: Graph):
        """
        What should a step consist of?
        We see the candidates (neighbouring nodes), we see their states.
        We make a decision. I learn to code. Ha, ha.
        We make a decision based on the state of each candidate.
        RULE 1: The base of Tremaux's algorithm is to NEVER change a mark
        """

        neighbors = self._current.passages
        state_of_neighbors = self.state[self._current.label]
           
        next = self.decide(state_of_neighbors)

        if next is None:
            self._isDone = True
            return
        # RULE 1 is preserved
        if self.state[self._current.label][next] is None:
            self.state[self._current.label][next] = 'E'
        # RULE 1 is preserved (all have to be None)
        if all(v is None for v in self.state[next].values()):
            self.state[next][self._current.label] = 'F'
                
        self._current = graph.get_node_from_label(next)
        self.path.append(next)
        
        self.n_step += 1

        return self
    
    def run(self, start: Union[int, Vertex, None], graph: Graph):

        # Should all this be done by the run method? Should something be moved to init?
        self.start = help_start(start=start, graph=graph)
        self._current = self.start
        self.path = [self.start._toint()] # initialize the path variable
        self._initialize_node_passage_state(graph)

        while not self._isDone:
            step = self.step(graph=graph)
            if step is not None:
                print('\n**********************')
                print('Taking next step...')
                print(f'Moved to node {self._current.label}')
            if self.DELAY is not None:
                time.sleep(self.DELAY)
        print('\n************************')
        print(f'\nWe should be done. The Walker took the following path: \n')
        print(f'{" -> ".join([str(n) for n in self.path])}')
        print('\nSee ya')

if __name__ == "__main__":
    testfile = np.load('tests/tests.npz')
    for ar in testfile.files:
        A = testfile[ar]
        graph = Graph(A)
        tr = TremauxAlgorithm()
        tr.run(start=0, graph=graph)