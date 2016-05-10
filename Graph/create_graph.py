'''Convert text to bigram graph'''


from StopWordGO.TextReader import text_reader
from StopWordGO.Graph import algorithms as algos
import networkx as nx


class Create(object):
    """Create graph object"""
    def _bigram_to_graph(self):
        '''Import NX and convert bigram
        to graph'''
        BiGramGraph = nx.Graph()
        for e in self.bigram:
            BiGramGraph.add_edge(*e)
        self.graph = BiGramGraph

    def __init__(self, filename):
        self.tr = text_reader.TextReader(filename=filename)
        self.tr.read_file()
        self.tr.text_array()
        self.tr.create_bigram()
        self.bigram = self.tr.bigram
        self._bigram_to_graph()
        self.transitivity = algos.sparse_transitivity(self.graph)
