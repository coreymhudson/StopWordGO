"""Graph algorithms"""

import networkx as nx
from scipy.sparse import tril, triu
import numpy as np
from operator import itemgetter


def sparse_transitivity(Graph):
    A = nx.to_scipy_sparse_matrix(Graph)
    k = A.sum(axis=0)
    k_minus_1 = k - 1
    Wv = np.sum(np.multiply(k, k_minus_1) / 2.)
    L = tril(A)
    U = triu(A)
    B = L.dot(U)
    C = A.multiply(B)
    triangles = C.sum() / 2.
    transitivity = 3.0 * triangles / Wv
    return transitivity


def sort_by_degree(Graph):
    return sorted(Graph.degree_iter(),
                  key=itemgetter(1), reverse=True)
