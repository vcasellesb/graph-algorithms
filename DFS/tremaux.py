from Graph import Graph, A
import random
import numpy as np
import time


class TremauxAlgorithm:

    def __init__(self, graph: Graph, start=None):
        self._isDone = False
        self.graph = graph

        if start is None:
            self.start = random.choice(self.graph.nodes)
        elif isinstance(start, int):
            self.start = self.graph.get_node_from_label(start)
        else: self.start = start

        self.n_step = 0
        self._current = self.start
        self.path = [self.start._toint()]

        self._initialize_node_passage_state()
    
    def _initialize_node_passage_state(self):

        """
        Initializes the dictionary where we'll 
        store the marks for our edges (or passages)
        """
        states = dict()

        for node in self.graph.nodes:
            states[node.label]=dict.fromkeys(node.passages)
            
        self.state = states
        
        return self
    
    def decide(self, neighbors: dict) -> int:
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
        else: raise Exception('It\'s done. All ')

    def step(self):
        """
        What should a step consist of?
        We see the candidates (neighbouring nodes), we see their states.
        We make a decision. I learn to code. Ha, ha.
        We make a decision based on the state of each candidate.
        RULE: The base of Tremaux's algorithm is to NEVER change a mark
        """

        neighbors = self._current.passages
        state_of_neighbors = self.state[self._current.label]
           
        next = self.decide(state_of_neighbors)

        # RULE is preserved
        if self.state[self._current.label][next] is None:
            self.state[self._current.label][next] = 'E'
        # RULE is preserved (all have to be None)
        if all(v is None for v in self.state[next].values()):
            self.state[next][self._current.label] = 'F'
                
        self._current = self.graph.get_node_from_label(next)
        self.path.append(next)
        
        self.n_step += 1

        return self
    
    def run(self):
        while True:
            try:
                print('\n**********************')
                print('Taking next step...')
                self.step()
                print(f'Moved to node {self._current.label}')
                time.sleep(2)
            except Exception:
                print('')
                print(f'We should be done. The Walker took the following path: ')
                print(f'{self.path}')
                exit()
        return

if __name__ == "__main__":
    graph = Graph(A)
    tr = TremauxAlgorithm(graph, start=0)
    tr.run()