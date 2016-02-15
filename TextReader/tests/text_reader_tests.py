"""Test the TextReader class.

This class tests functionality in the TextReader class.

TextReaderTests: test various functionality in the
TextReader class.

"""

import unittest

from StopWordGO.TextReader import text_reader


class TextReaderTests(unittest.TestCase):
    """Test the TextReader class."""

    def setUp(self):
        """Initialize before every test."""
        self._filename = '../data/Moby_Dick.txt'
        tr = text_reader.TextReader(filename=self._filename)
        tr.read_file()
        self.doc = tr.doc
        tr.text_array()
        self.text_array = tr.text_array
        tr.create_bigram()
        self.bigram = tr.bigram

    def tearDown(self):
        """Clean up after each test."""
        del self.doc
        del self.text_array
        del self.bigram

    def test_read_file(self):
        """Ensure that file was read."""
        _test_read = self.doc.split()[100:105]
        _test_array = self.text_array[100:105]
        _test_Moby_Dick = ['by', 'daniel', 'lazarus', 'and', 'jonesey']
        _test_Moby_Dick_bigram = [('by', 'daniel'), ('daniel', 'lazarus'), ('lazarus', 'and'), ('and', 'jonesey'), ('jonesey', 'moby')]
        _test_bigram = self.bigram[100:105]
        self.assertEqual(_test_read, _test_Moby_Dick)
        self.assertEqual(_test_array, _test_Moby_Dick)
        self.assertEqual(_test_bigram, _test_Moby_Dick_bigram)

if __name__ == '__main__':
    unittest.main()
