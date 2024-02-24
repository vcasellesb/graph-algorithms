# Breadth-First Search Algorithms

## Naive BFS (BFS)

In this file I've implemented a very basic breadth-first search algorithm, according to `https://www.baeldung.com/cs/graph-number-of-shortest-paths`.

Basically, this algorithm works as follows. You start with a source node, lets say node $i$. We label the nodes adjacent (*neighbors*) to $i$ as 1, since that's their distance. We add them to a queue. Then we iterate until the queue is empty. Basically, at each iteration, we "get" the first node in the queue + remove it from the queue    