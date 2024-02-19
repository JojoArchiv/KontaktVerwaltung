'''
Created on 09.11.2023

@author: Jojo
'''
import unittest
from JoJo.KontaktVerwaltung.Services import Page, Kontakt, RecordOrder, \
    KontakteRepository, DatenbankService, KategorieRepository
from sqlalchemy.orm.session import Session
from sqlalchemy.sql._selectable_constructors import select
import os
from JoJo.KontaktVerwaltung.Domain import GenderTypes


class Test(unittest.TestCase):

    def setUp(self):
        
        self.db_file = "C:\\Temp\\databasetest.db"
        try:
            os.remove(self.db_file)
        except FileNotFoundError:
            pass
        self.dbservice = DatenbankService("sqlite:///%s" % self.db_file)
        # self.dbservice = DatenbankService("sqlite:///")
        self.engine = self.dbservice.setup()
        self.session = Session(self.engine)
        self.kontakte_repository = KontakteRepository(self.session)
        self.kategorien_repository = KategorieRepository(self.session)
        
    def tearDown(self):
        
        self.session.commit()
        self.session.close()
        self.engine.dispose()
        try:
            os.remove(self.db_file)
        except FileNotFoundError:
            pass
        
    def testGetPage2(self):
        
        kontakt1 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Schulz")
        kontakt2 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller")
        kontakt3 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Maier")
        kontakt4 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker") 
        kontakt5 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Wiese")

        page = Page()
        page.page_idx = 1
        page.page_size = 2    

        page = self.kontakte_repository.get_page(page)
        self.assertEqual(page.page_size, len(page.kontakt_list))
        self.assertEqual(page.kontakt_list[0].nachname, "Müller")    
        self.assertEqual(page.kontakt_list[1].nachname, "Schulz")    
        self.assertEqual(page.number_of_pages, 3)    

    def testGetPage2a(self):
        
        kontakt1 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Schulz")
        kontakt2 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller")
        kontakt3 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Maier")
        kontakt4 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker") 

        page = Page()
        page.page_idx = 1
        page.page_size = 2    

        page = self.kontakte_repository.get_page(page)
        self.assertEqual(page.page_size, len(page.kontakt_list))
        self.assertEqual(page.kontakt_list[0].nachname, "Müller")    
        self.assertEqual(page.kontakt_list[1].nachname, "Schulz")    
        self.assertEqual(page.number_of_pages, 2)    

    def testSearchWithSearchString(self):
        
        kontakt1 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller-Thurgau", vornamen="Lisa")
        kontakt2 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller", vornamen="Lena")
        kontakt3 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Maier", vornamen="Leroy")
        kontakt4 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, mailadresse="lerche24@gmx.de") 
        kontakt5 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Wiese")
        
        page = Page()
        page.page_idx = 0
        page.page_size = 2  
        page.search_string = "Ler"
        page = self.kontakte_repository.get_page(page)
        self.assertEqual(page.kontakt_list[0].mailadresse, "lerche24@gmx.de")
        self.assertEqual(page.kontakt_list[1].vornamen, "Leroy")
        page.page_idx = 1
        page = self.kontakte_repository.get_page(page)
        self.assertEqual(page.kontakt_list[0].nachname, "Müller")    
        self.assertEqual(page.kontakt_list[1].nachname, "Müller-Thurgau")   
        
    def testWithKategorieFilter(self):
        
        kontakt1 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller-Thurgau", vornamen="Lisa")
        kontakt2 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller", vornamen="Lena")
        kontakt3 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Maier", vornamen="Leroy")
        kontakt4 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, mailadresse="lerche24@gmx.de") 
        kontakt5 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Wiese")
        kategorie1 = self.kategorien_repository.create(kategorienname="Nutzer")
        self.kontakte_repository.addKategorie(kontakt1, kategorie1)
        kategorie2 = self.kategorien_repository.create(kategorienname="Schüler")
        self.kontakte_repository.addKategorie(kontakt5, kategorie2)
        self.kontakte_repository.addKategorie(kontakt2, kategorie2)
        
        page = Page()
        page.page_idx = 0
        page.page_size = 6  
        page.kategory_filter = "Schüler"
        page = self.kontakte_repository.get_page(page)
        self.assertEqual(len(page.kontakt_list), 2)
        self.assertEqual(page.kontakt_list[0].nachname, "Müller")
        self.assertEqual(page.kontakt_list[1].nachname, "Wiese")
        self.assertEqual(page.number_of_pages, 1)   
        
    def testSearchWithSearchStringAndKategorieFilter(self):
        
        kontakt1 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller-Thurgau", vornamen="Lisa")
        kontakt2 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller", vornamen="Lena")
        kontakt3 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Maier", vornamen="Leroy")
        kontakt4 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, mailadresse="lerche24@gmx.de") 
        kontakt5 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Wiese")
        kategorie1 = self.kategorien_repository.create(kategorienname="Nutzer")
        self.kontakte_repository.addKategorie(kontakt1, kategorie1)
        kategorie2 = self.kategorien_repository.create(kategorienname="Schüler")
        self.kontakte_repository.addKategorie(kontakt5, kategorie2)
        self.kontakte_repository.addKategorie(kontakt2, kategorie2)

        page = Page()
        page.page_idx = 0
        page.page_size = 2
        page.search_string = "Ler"  
        page.kategory_filter = "Schüler"
        page = self.kontakte_repository.get_page(page)
        self.assertEqual(len(page.kontakt_list), 1)
        self.assertEqual(page.kontakt_list[0].nachname, "Müller")
        self.assertEqual(page.number_of_pages, 1)   


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
