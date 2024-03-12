'''
Created on 14.08.2023

@author: Jojo
'''
import unittest
from JoJo.KontaktVerwaltung.Services import DatenbankService, KategorieRepository,\
    IllegalIdException
from JoJo.KontaktVerwaltung.Domain import Kategorie
from sqlalchemy.orm.session import Session

class Test(unittest.TestCase):


    def setUp(self):
        
        dbservice = DatenbankService()
        engine = dbservice.setup()
        self.session = Session(engine)
        self.kategorien_service = KategorieRepository(self.session)
        
    def tearDown(self):
        
        self.session.close()


    def testCreate(self):
        
        kategorie = self.kategorien_service.create(kategorienname="Meine Kategorie")
        self.assertTrue(kategorie is not None)
        self.assertTrue(isinstance(kategorie, Kategorie))
        self.assertTrue(kategorie.id is not None)

    def testGet(self):
        
        kategorie = self.kategorien_service.create(kategorienname="Meine Kategorie")
        kategorie2 = self.kategorien_service.get(kategorie.id)
        self.assertTrue(kategorie2 is not None)
        self.assertTrue(isinstance(kategorie2, Kategorie))
        self.assertTrue(kategorie2.id is not None)
        self.assertEqual(kategorie.id, kategorie2.id)
        self.assertEqual(kategorie, kategorie2)
        
    def testFindAllKategorien(self):
        
        kategorie1 = self.kategorien_service.create(kategorienname="Spender_in")
        kategorie2 = self.kategorien_service.create(kategorienname="Fördermitglied")
        kategorie3 = self.kategorien_service.create(kategorienname="Studierende")
        kategorie4 = self.kategorien_service.create(kategorienname="Mitarbeitende")
        kategorie5 = self.kategorien_service.create(kategorienname="Referent_innen")
        
        kategorien_liste = self.kategorien_service.find_all()
        print("************************************************", kategorien_liste)
        
        self.assertEqual(len(kategorien_liste), 5)
        self.assertEqual("Fördermitglied", kategorien_liste[0].kategorienname)
        
    def testGetByKategorienname(self):
        
        kategorie1 = self.kategorien_service.create(kategorienname="Spender_in")
        kategorie2 = self.kategorien_service.create(kategorienname="Fördermitglied")
        kategorie3 = self.kategorien_service.create(kategorienname="Studierende")
        kategorie4 = self.kategorien_service.create(kategorienname="Mitarbeitende")
        kategorie5 = self.kategorien_service.create(kategorienname="Referent_innen")
        kategorien_liste = self.kategorien_service.get_by_kategorienname(kategorienname="Spender_in")
        self.assertEqual(kategorien_liste.kategorienname, "Spender_in")
        self.assertEqual(kategorien_liste.id, 1)
    
    def testGetFailsOnNotExistingID(self):

        exception_thrown = False
        try:        
            kategorie = self.kategorien_service.get(4711)
        except IllegalIdException as e:
            exception_thrown = True
            
        self.assertTrue(exception_thrown)

    def testGetFailsOnNone(self):

        exception_thrown = False
        try:        
            kategorie = self.kategorien_service.get(None)
        except IllegalIdException as e:
            exception_thrown = True
            
        self.assertTrue(exception_thrown)

    def testDelete(self):
        
        kategorie = self.kategorien_service.create(kategorienname="Meine Kategorie")
        self.kategorien_service.get(kategorie.id)
        self.kategorien_service.delete(kategorie)
        
        exception_thrown = False
        try:
            self.kategorien_service.get(kategorie.id)
        except IllegalIdException as e:
            exception_thrown = True
        
        self.assertTrue(exception_thrown)    
        
    def testDeleteByName(self):
        
        kategorie = self.kategorien_service.create(kategorienname="Meine Kategorie")
        self.kategorien_service.get(kategorie.id)
        self.kategorien_service.delete_by_name("Meine Kategorie")
        
        exception_thrown = False
        try:
            self.kategorien_service.get(kategorie.id)
        except IllegalIdException as e:
            exception_thrown = True
        
        self.assertTrue(exception_thrown)       
    
    def testDeleteByNameFailing(self):
        
        self.kategorien_service.delete_by_name("nicht existierende kategorie")
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()