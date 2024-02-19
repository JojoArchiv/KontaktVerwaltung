'''
Created on 18.12.2023

@author: Jojo
'''
import unittest
from unittest.mock import MagicMock
from JoJo.KontaktVerwaltung.Services import KategorieRepository
from JoJo.KontaktVerwaltung.Domain import Kategorie
from mock.mock import Mock


class KategorienMockTest(unittest.TestCase):


    def setUp(self):
        
        self.mock_session = MagicMock()
        self.result = MagicMock()
        self.mock_session.execute.return_value = self.result
        self.result.scalars.return_value = [Kategorie(), Kategorie()]
        
        self.kategorie_repository = KategorieRepository(self.mock_session)


    def tearDown(self):
        pass


    def test_find_all(self):
        
        list_of_categories = self.kategorie_repository.find_all()
        
        self.assertEqual(2, len(list_of_categories))
        self.mock_session.execute.assert_called_once()
        self.result.scalars.assert_called_once()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()