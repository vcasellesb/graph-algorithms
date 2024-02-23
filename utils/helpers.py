from typing import Union
from Graph import Vertex, Graph
import random



## a few utils 

def help_start(start: Union[int, Vertex], graph: Graph, allowNone:bool=True) -> Vertex:

    """Allows abstraction for walk initiation"""
    
    if isinstance(start, Vertex): return start
    elif isinstance(start, int): return graph.get_node_from_label(start)
    elif start is None and allowNone: return random.choice(graph.nodes)
    else: raise Exception('Wrong start argument')

