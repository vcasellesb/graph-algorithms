# Depth-First Search Algorithms

## Trémaux Algorithm

In the book I'm using to study about graph algorithms this one is really poorly explained (in the pseudocode, it skips many important parts). A whole day just to get a grasp on how it works. I think it's an algorithm that is better suited for working with mazes. The book is **Graph Algorithms** by *Even*, *Shimon*

The implementation I've done is for undirected graphs. I just work with adjacency matrices, which I usually call "A". I will leave an `.npz` file called `DFS/tests/tests.npz`, where I've stored a couple graphs --better said, their adjacency matrices-- as `np.ndarray`s. I'm not very well-versed in the `Python` network science world (i.e. I don't know how users can specify a graph they wanna test out the algorithm on), but for now you can just overwrite the `DFS/tests/tests.npz` file with the `np.savez` function and entering your own adjacency matrices as args, and pass the `DFS/tremaux.py` file to your `Python` interpreter.