from typing import Union, List, Tuple
import numpy as np

# This is just me playing around with the homework for Chapter two of Albert Laszlo-Barabasi's book on network science
def extract_degree_vec(A: np.ndarray, n: Union[int, None] = None) -> np.ndarray:
    """
    We use "linear algebra" to extract the degree ($k_i$) of node $i$ (given an adjacency matrix).
    I've extended the function to be able to get the n-length neighbors of node $i$s degree, up to n=2.
    Usage:
    * To get the degree vector of node i, don't specify parameter "n".
    * To get the degree vector of the neighbors of node i, set n=1
    * To get the degree vector of the second order neighbors of node i, set n=2
    * else, je ne se pas

    I don't know how to extend it to n=3... if anyone knows please hit me up at vcasellesb@uoc.edu
    TODO: Implement this as a Graph object method? maybe?
    """

    ## To get the degree of node i using A is easy, just do this:
    N = A.shape[0]
    ones = np.ones((N, 1))
    k = A.dot(ones).ravel()
    # you can also get it like this:
    k_v2 = np.sum(A, axis=1) # it doesn't actually matter axis 0 or 1...
    assert np.all(k == k_v2)

    # in case you want the vector w the degree of the node i
    if not n: return k
    elif n == 1:
        # if you want the degree of the neighbors of node i, then things get a lil fun but not very much
        # there are also many ways...
        # way 1:
        A_2 = np.linalg.matrix_power(A, n=n+1)
        k_neigh_1 = A_2.dot(ones).ravel()

        # also we could just sum A^2
        k_neigh_1_v2 = np.sum(A_2, axis=1)
        assert np.all(k_neigh_1 == k_neigh_1_v2)
        return k_neigh_1
    
    elif n==2:
        # this is just me trying stuff. I'm not sure wheter this is a solution.
        # I don't even know if this could qualify as a solution. Basically, to get the 
        # vector with the degrees of second neighbors of node i
        # we have to multiply the vector with the degrees by the matrix with the second
        # neighbors of node i. I do it like this:
        A_sum = np.zeros(A.shape)
        for i in range(1, n):
            A_sum += np.linalg.matrix_power(A, n=i)
        
        A_n = np.linalg.matrix_power(A, n)
        A_res = A_n - A_sum
        A_res = np.clip(A_res, 0, 1)
        np.fill_diagonal(A_res, 0)
        return A_res.dot(k)
    
    else: raise NotImplementedError('Sorry, I don\'t know how to get the degree vector of n>2 neighbors... :(')

def extract_triang(A: np.ndarray) -> int:
    """
    This one I had to look up. I was trying to solve it using only the trace
    -- for example counting how many "traces" with offset over 2 there were 
    in the adj matrix, but it doesn't work like that.
    You should first understand the problem, then try and solve it. Not just rushing 
    to solve it. Bad bad bad. It's actually pretty straightforward. A triangle means that each
    member of the triangle has two 3-length paths to itself. So if you do A*A*A == A^3, however many 
    2s there are in the diagonal is the number of triangle components there are. Since there are three
    members in a triangle, you have to divide that number by 3. This is equivalent to computing the trace
    and dividing by 6.
    """   

    # Trying out my logic
    diag = np.diag(A.dot(A.dot(A)))
    diag = np.sum(diag>=2) / 3
    assert diag == np.trace(A.dot(A.dot(A))) / 6

    return int(np.trace(A.dot(A.dot(A))) / 6)

def A_to_link_list(A: np.ndarray) -> List[Tuple[int]]:
    """
    I think the main difficulty of this problem is how to codify the link list. I've tried
    using a set of sets, but Python doesn't allow unhashable types in sets.
    Scouring the internet, I've found that networkX uses tuples to store links.
    But how should we deal with undirected links? Just store one (since the other link is esentially the same)?
    """
    arr1, arr2 = np.nonzero(A)
    # we check if there's any node with no links
    uniq = len(np.unique(arr1))
    which = None
    if uniq != A.shape[0]:
        which = set(np.unique(np.where(~A.any(axis=1))))

    l = [(i, j) for i, j in zip(arr1, arr2)]
    if which:
        for s in which:
            l.append((s, None))
    return l

def link_list_to_A(link_list: List[Tuple[int]]) -> np.ndarray:
    """
    We assume that all nodes have links. Otherwise, they won't be included
    in the adj matrix.
    TODO: Handle missing nodes.
    """
    dim1 = dim2 = len(np.unique([i[0] for i in link_list]))
    A = np.zeros((dim1, dim2))
    for t in link_list:
        s, d = t
        if d is None:
            A[s] = np.zeros((dim1,))
            continue
        A[s, d] = 1       
    return A

def clust_coef(A: np.ndarray) -> float:
    """
    What do we need here? The clustering coefficient is the number of links
    between the neighbors of node i divided by k_i * (k_i - 1) where k_i is the degree
    of node i.

    k_i is easy to get. Refer to extract_degree_vec. 
    The difficult part is getting the links between neighbors of node i

    TODO: Fix this BS
    """
    l_of_ls = list()

    ## This is the ugliest thing I've ever seen. And I have mirrors in my house. FIX!!!!!!!
    for node_i in A[0]:
        l = 0
        neigh = set(np.nonzero(A[node_i])[0])
        for n in neigh:
            neigh_of_neigh = set(np.nonzero(A[n])[0])
            for n_n in neigh_of_neigh:
                if n_n in neigh and n_n != node_i:
                    l += 1

        l_of_ls.append(l)

    
    l = np.array(l_of_ls)
    k_i = extract_degree_vec(A)
    denom = (k_i*(k_i-1))
    return np.divide(l, denom, out=np.zeros_like(l, dtype=float), where=denom!=0)
    

if __name__ == "__main__":
    testfile = np.load('tests/tests.npz')
    for i, ar in enumerate(testfile.files):
        A = testfile[ar]

        print(clust_coef(A))
        continue
        n = 2
        if n and n<2:
            message = 'of neighbor of node i'
        elif n>1:
            message = 'of second order neighbor of node i'
        else: message = "of node i"
        print(f'The degree vector {message} of graph {i+1} is: \n {extract_degree_vec(A, n=n)}')
        print(f'I believe that the number of links in graph {i+1} is given by {int(np.sum(extract_degree_vec(A)) / 2)}')
        # I'm still the best

        print(f'There are {extract_triang(A)} triangles in graph {i+1}')
        print('*****************************\n')