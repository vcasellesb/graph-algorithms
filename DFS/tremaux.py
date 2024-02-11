import numpy as np

## we define a graph (i.e. an adjacency matrix)

A = np.array([[0, 1, 0, 1],
              [1, 0, 1, 1],
              [0, 1, 0, 0],
              [1, 1, 0, 0]])


def add_to_dict(dict, key, value):

    if dict.get(key) is not None:
        dict[key].append(value)
    else:
        dict[key] = [value]
    return

def check_if_in_dict(dict, key, value):

    """
    Checks if a key-value pairing exists in dict.
    """

    if dict.get(key) is not None:
        if value in dict.get(key):
            return True
        else:
            return False
    else:
        return False
    
def marked_passages_in_v(E, F, v):
    marked = 0  
    if E.get(v) is not None:
        marked += len(E.get(v))
    if F.get(v) is not None:
        marked += len(F.get(v))
    return marked

def choose_next_candidate(cand_list, v, E_dict):

    if E_dict.get(v) is None:
        return np.random.choice(cand_list)
    
    cand_not_seen = [c for c in cand_list if c not in E_dict.get(v)]
    print(cand_not_seen)
    return np.random.choice(cand_not_seen) if len(cand_not_seen)>1 else cand_not_seen[0]
    

def tremaux(A: np.ndarray, s: int):
    """
    This function implements Depth First Search as seen 
    in Graph Algorithms, by Shimon Even.
    
    Parameters:
        A (np.ndarray): Adjacency matrix.
        s (int): starting vertix.
        
    Returns:
        TBD
    """
    
    v = s
    print(f'Starting in {v}')
    E = dict() # E stores all paths from v visited
    F = dict() # F stores all paths leading to v visited

    # we get all the passages from v
    cand = np.nonzero(A[v])[0]

    umk_pas_v = len(cand)

    path = list()
    path.append(v)
    while umk_pas_v > 0 or F.get(v) is not None:
        cand = np.nonzero(A[v])[0]
        cand_chosen = choose_next_candidate(cand, v, E) 
        umk_pas_v = len(cand) - marked_passages_in_v(E, F, v)
        print('******************************')
        print(f'current v: {v}')
        print(f'current candidates: {cand}')
        print(f'Unmarked passages in v: {umk_pas_v}')
        print(f'Path: {path}')
        print(f'E dict: {E}')
        print(f'F dict: {F}')

        u = cand_chosen
        print('u chosen', u)
        if not check_if_in_dict(E, v, u):
            add_to_dict(E, v, u)
            print(f'E.get(u) is {E.get(u)}')
            print(f'F.get(u) is {F.get(u)}')
            if (E.get(u) is None and F.get(u) is None):
                add_to_dict(F, u, v)
                path.append(u)
                print(f'Moving to {u}')
                v=u
            else:
                add_to_dict(E, u, v)
        else:
            print(f'Moving to {u}')
            path.append(u)
            v = u
    

    return path, E, F

# tremaux(A, 0)