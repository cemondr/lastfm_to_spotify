import unittest
from src import config
import test.fakeconfig as fakeconfig
from src.tag_to_playlist import tag_to_playlist as lib

class TestTagToPlaylist(unittest.TestCase):

    def test_connect_to_lastfm(self):
        lib1 = lib(config)
        self.assertTrue(lib1.connect_to_lastfm())
        lib2 = lib(fakeconfig)
        self.assertFalse(lib2.connect_to_lastfm())


    # This test will ask you to copy paste the redirected url (twice). Do it!
    def test_connect_to_spotify(self):
        lib1 = lib(config)
        self.assertTrue(lib1.connect_to_spotify())
        lib2 = lib(fakeconfig)
        self.assertFalse(lib2.connect_to_spotify())
     



if __name__ == '__main__':
    unittest.main()