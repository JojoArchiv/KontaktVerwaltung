'''
Created on 12.10.2023

@author: Jojo
'''
import unittest
from JoJo.KontaktVerwaltung.Domain import Kontakt

def getNachname(kontakt: Kontakt):
    
    return kontakt.nachname

class Test(unittest.TestCase):

    def setUp(self)->None:
        
        kontakt1 = Kontakt()
        kontakt1.id = 1
        kontakt1.nachname = "Maier"
        kontakt1.vorname = "Paul"
        
        kontakt2 = Kontakt()
        kontakt2.id = 2
        kontakt2.nachname = "Müller"
        kontakt2.vorname = "Klaus"
        
        kontakt3 = Kontakt()
        kontakt3.id = 3
        kontakt3.nachname = "Schulz"
        kontakt3.vorname = "Erwin"
        
        self.kontakt_list = [kontakt1, kontakt2, kontakt3]

    def testSortByNachname(self):
        
        self.kontakt_list.sort(key=getNachname)
        self.assertEqual(1, self.kontakt_list[0].id)
        self.assertEqual(2, self.kontakt_list[1].id)
        self.assertEqual(3, self.kontakt_list[2].id)

    def testSortByVorname(self):
        
        self.kontakt_list.sort(key=lambda kontakt: kontakt.vorname)
        self.assertEqual(3, self.kontakt_list[0].id)
        self.assertEqual(2, self.kontakt_list[1].id)
        self.assertEqual(1, self.kontakt_list[2].id)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()