# Graph Algorithms

I really like graphs. They have a soothing quality to them that I enjoy. They are self-contained, they are chill. They are cool. However, I know very little about them. I wanna change that. So I'm gonna try and implement some algorithms walking through them.

This repo is inspired by the books Graph Algorithms, by Shimon Even, and Network Science, by Albert Laszlo-Barabasi. I'm currently walking through both, searching info on graphs and trying to implement the algorithms that are usually used on them. I'll try to be as organized as possible, but I'm pretty chaotic, so yeah.

The code for the "Walkers", I'd love to be able to say that it was all from my tiny brain, but it is not. My main inspiration is `https://github.com/illiterati1/python_maze/`, where the author implements what the *Tremaux* algorithm (the first one I've tried to implement) for the purpose it's best known for, which is maze solving. Anyways, I've gotten some ideas about how to structure the code from there, so feel free to check it out.

Currently, all algorithms implemented are for unweighted, undirected graphs. In the future I'll implement weighted graphs.

## Usage
To try out an algorithm, you just have to run the following command:
```bash
python3 -m <modulename>.<filename>
```
Example:
```bash
python3 -m DFS.tremaux
```
Basically, this will run the algorithm specified on the graphs stored in `tests/tests.npz.`. In this file, I've stored a couple adjacency matrices as `np.ndarray`s. I'm not very well-versed in the `Python` network science world (i.e. I don't know how users can specify a graph they wanna test out the algorithm on), but for now you can just overwrite the `DFS/tests/tests.npz` file with the ```numpy np.savez``` function and entering your own adjacency matrices as args.