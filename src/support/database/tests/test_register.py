import unittest
from shutil import copy
from os import remove
from .. import register_item

testsupport = "C:\\Users\\user1\\Documents\\Codes\\Spotify_Records\\src\\support\\database\\registry.csv"

class TestRegistry(unittest.TestCase):
    def test_read(self):
        test = "spotify:track:0oufSLnKQDoBFX5mgkDCgR"  #trust by Brent Faiyaz
        df = register_item.readRegistry(testsupport)
        self.assertEquals("Trust",df.at[test,'Name'])

    def test_read_badItem(self):
        test = "BADVALUE"  #trust by Brent Faiyaz
        df = register_item.readRegistry(test)
        self.assertIsInstance(df,FileNotFoundError)

class TestFind(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = register_item.readRegistry(testsupport)
    
    @classmethod
    def tearDownClass(cls):
        cls.df = None

    def testfindItem(self):
        test = "spotify:track:0oufSLnKQDoBFX5mgkDCgR"  #trust by Brent Faiyaz
        answer = register_item.findItem(self.df,test)
        self.assertTrue(answer)
        self.assertIsInstance(answer,str)

    def testfindItemDoesntExist(self):
        test="DOESNTEXIST"
        answer = register_item.findItem(self.df,test)
        self.assertFalse(answer)

class TestAddRegistry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.destination =  "C:\\Users\\user1\\Documents\\Codes\\Spotify_Records\\src\\support\\database\\registry_copy.csv"
        copy(testsupport,cls.destination)
    
    @classmethod
    def tearDownClass(cls):
        cls.destination =  "C:\\Users\\user1\\Documents\\Codes\\Spotify_Records\\src\\support\\database\\registry_copy.csv"
        remove(cls.destination)

    def testAdding(self):
        test = "TEST"
        newDf = register_item.Add2Registry(self.destination,test)
        self.assertEquals(test,newDf.loc[test].name)

    def testAddingOptionals(self):
        test = "TEST2"
        newDf = register_item.Add2Registry(self.destination,test,RFID="DUMMY CODE")
        self.assertEquals("DUMMY CODE",str(newDf.at[test,"RFID Code"]))

if __name__ == "__main__":
    unittest.main()