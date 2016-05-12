"""Test the Create class.

This class tests functionality in the Create class.

CreateTests: test various functionality in the
Create class.

"""

import unittest

from StopWordGO.Graph import create_graph, algorithms

import numpy as np


class CreateTests(unittest.TestCase):
    """Test the Create class."""

    def setUp(self):
        """Initialize before every test."""
        self._filename = '../../TextReader/data/Moby_Dick.txt'
        self.graph = create_graph.Create(filename=self._filename)

    def tearDown(self):
        """Clean up after each test."""
        del self.graph

    def test_transitivity(self):
        _transitivity = 0.0240620296974
        self.assertAlmostEqual(_transitivity, self.graph.transitivity)


class AlgorithmsTest(unittest.TestCase):
    """Test the Algorithms functions."""

    def setUp(self):
        """Initialize before every test."""
        self._filename = '../../TextReader/data/Moby_Dick.txt'
        self.gr = create_graph.Create(filename=self._filename)
        self.graph = self.gr.graph
        self.identity = algorithms.sparse_identity(self.graph)

    def tearDown(self):
        """Clean up after each test."""
        del self.gr

    def test_sort_by_degree(self):
        _sorted_list = [('the', 6295), ('and', 4962)]
        self.assertEqual(_sorted_list,
                         algorithms.sort_by_degree(self.graph)[0:2])

    def test_sparse_transitivity(self):
        _transitivity = 0.0240620296974
        self.assertAlmostEqual(_transitivity,
                               algorithms.sparse_transitivity(self.graph))

    def test_sparse_identity(self):
        _I = algorithms.sparse_identity(self.graph).sum()
        _J = len(self.graph.nodes())
        _sum = 20210.0
        self.assertEqual(_I, _J)
        self.assertEqual(_I, _sum)

    def test_remove_list_from_identity(self):
        _node_list = [1, 4, 5]
        _I = algorithms.remove_list_from_identity(self.identity, _node_list)
        _I_sum = _I.sum()
        _sum = 20207
        self.assertEqual(_I_sum, _sum)

if __name__ == '__main__':
    unittest.main()
