'''Pull in a corpus and process it.

This class takes a text file and processes the data into an array of text.
To do this it also has functions that allow for the text to have punctuation removed.
There are two output forms: An array of text and a bigram array of each pair of words
in the corpus.

'''

import string
from itertools import tee, izip


class TextReaderException(Exception):

    """Use this class to raise exceptions"""
    pass


class TextReader(object):

    """Transform text into data structures"""

    def __init__(self, filename=None):
        """Initialize the TextReader class"""
        self.filename = filename

    def _remove_extraneous_characters(self, document):
        '''Remove all the extraneous characters from the document'''
        _table = string.maketrans("", "")
        return ' '.join(document.replace('\n', ' ').replace('\r',
                        ' ').replace('\t', ' ').replace('\s+',
                        ' ').translate(_table, string.punctuation).split())

    def _lower_case(self, document):
        return document.lower()

    def read_file(self):
        if self.filename:
            doc = open(self.filename).read()
            doc = self._remove_extraneous_characters(doc)
            doc = self._lower_case(doc)
            self.doc = doc
        else:
            raise ValueError('Need to initialize TextReader with filename')

    def text_array(self):
        self.text_array = self.doc.split()

    def _pairwise(self, _text_array):
        _a, _b = tee(_text_array)
        next(_b, None)
        return izip(_a, _b)

    def create_bigram(self):
        bigram = []
        for v, w in self._pairwise(self.text_array):
            bigram.append((v, w))
        self.bigram = bigram
