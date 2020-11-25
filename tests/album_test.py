import unittest
from models.album import Album
from models.artist import Artist

class TestTask(unittest.TestCase):
    
    def setUp(self):
        self.the_artist = Artist("Prince")
        self.the_album = Album("Not a Good Time", self.the_artist, "Purple Sound")
    
    
    def test_album_has_title(self):
        self.assertEqual("Not a Good Time", self.the_album.title)
        
        
    def test_album_has_artist(self):
        self.assertEqual("Prince", self.the_album.artist.name)
       
        
    def test_album_has_genre(self):
        self.assertEqual("Purple Sound", self.the_album.genre)
    
    
   