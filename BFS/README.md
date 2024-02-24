# Breadth-First Search Algorithms

## Naive BFS (BFS)

In this file I've implemented a very basic breadth-first search algorithm, according to `https://www.baeldung.com/cs/graph-number-of-shortest-paths`.

Basically, this algorithm works as follows. You start at the source node, lets say node $i$, which has distance $0$ and $1$ shortest path going to it. All other nodes have distance $\infty$. We then iterate through the nodes adjacent (*neighbors*) to the current node (at the first step is $i$) and, if their distance to $i$ is higher than the [distance **from the current node to $i$] $+ 1$**, then we assign their distance to that value ([the distance from the current node to $i$] $+ 1$). Once we've done that, if the node hadn't been visited yet, you add it to the queue. Then we iterate until the queue is empty, "getting" the node at the front of the queue at each iteration, following the same logic.

I know I've probably made no sense, so if you have trouble understanding my explanation, please refer to the link at the top of the README and/or read my explanation while going through the code. I feel like it's pretty self-explanatory.