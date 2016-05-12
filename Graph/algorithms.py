"""Graph algorithms"""

import networkx as nx
from scipy.sparse import tril, triu, identity
import numpy as np
from operator import itemgetter


def nodes_to_index(Graph):
    nodes_index = {}
    return nodes_index


def graph_to_sparse(Graph):
    A = nx.to_scipy_sparse_matrix(Graph)
    return A


def remove_list_from_identity(I, node_list):
    for node in node_list:
        I[node][node] = 0
    return I


def sparse_identity(Graph):
    I = identity(len(Graph.nodes()))
    return I


def sparse_transitivity(Graph):
    A = graph_to_sparse(Graph)
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
