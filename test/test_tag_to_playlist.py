import unittest
from src import config
import test.fakeconfig as fakeconfig
from src.tag_to_playlist import tag_to_playlist as lib

class TestTagToPlaylist(unittest.TestCase):
    def test_connect_to_spotify(self):
        spotlib1 = lib(config)
        self.assertTrue(spotlib1.connect_to_spotify())
        spotlib2 = lib(fakeconfig)
        self.assertFalse(spotlib2.connect_to_spotify())
     



if __name__ == '__main__':
    unittest.main()