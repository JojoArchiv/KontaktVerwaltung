'''
Created on 30.08.2023

@author: Jojo
'''
import unittest
from sqlalchemy.engine.create import create_engine
from JoJo.KontaktVerwaltung.Services import KontakteRepository,\
    KategorieRepository, DatenbankService, IllegalIdException
from sqlalchemy.orm.session import Session
from JoJo.KontaktVerwaltung.Domain import GenderTypes, TelefonNummernTyp
import os



class IntegrationsTest(unittest.TestCase):
    
    def testKontakt(self):  
        
        self.setup_db()
        self.CreateKontakt()
        self.FindByNachnameOrKategorie()
        self.CreateSecondKategorieForOneKontakt()
        self.DeleteKontakt()
        self.CreateTwoKontakteAndOneKategorie()
        self.FindBySpendeninformation()
        self.tear_down_db()
        
    def CreateKontakt(self):
        
        kontakte_repository, kategorien_repository = self.reopen_session()
        
        kontakt = kontakte_repository.create(nachname="Wiese", vornamen="Lisa Marie", mailadresse="lisa_marie.wiese@web.de", gender=GenderTypes.FEMALE)
        kontakt_id = kontakt.id
        adresse = kontakte_repository.createAdresse(kontakt, strasse="Breisacher Str.", hausnummer=75, plz="79106", wohnort="Freiburg", land="The Länd")
        spendeninformation = kontakte_repository.createSpendeninformation(kontakt, spendenhoehe=50, spendenjahr=2001, spendenbescheinigung=True)
        bankdaten = kontakte_repository.createBankdaten(kontakt, iban = "DE0987654321", BIC="GENODEM1GLS", kreditinstitut="GLS Bank")
        telefonnummern = kontakte_repository.createTelefonnummer(kontakt, telefonnummer="0761/3435", telefon_nummern_typ=TelefonNummernTyp.FESTNETZ_PRIVAT, praeferiert=True, telefonnummer2="01578392774", telefon_nummern_typ2=TelefonNummernTyp.HANDY_PRIVAT)
        kategorie = kategorien_repository.create(kategorienname="Vereinsmitglied")
        kontakte_repository.addKategorie(kontakt, kategorie)
        
    def FindByNachnameOrKategorie(self):
        
        kontakte_repository, kategorien_repository = self.reopen_session()
        
        kontakt_liste = kontakte_repository.find_by_nachname("Wiese")
        self.assertTrue(kontakt_liste is not None)
        self.assertEqual(1, len(kontakt_liste))
        self.assertEqual("Wiese", kontakt_liste[0].nachname)
        
        kontakt_liste = kontakte_repository.find_by_kategorie("Vereinsmitglied")

        self.assertTrue(kontakt_liste is not None)
        print(len(kontakt_liste))
        self.assertEqual(1, len(kontakt_liste))
        self.assertEqual("Vereinsmitglied", kontakt_liste[0].kategorien[0].kategorienname)
        
    def CreateSecondKategorieForOneKontakt(self):
        
        kontakte_repository, kategorien_repository = self.reopen_session()
        
        print("\n\n\n*************************************\n\n\n")
        kontakt = kontakte_repository.get(1)
        
        kategorie2 = kategorien_repository.create(kategorienname="Nutzer")
        kontakte_repository.addKategorie(kontakt, kategorie2)
        kontakt_liste = kontakte_repository.find_by_kategorie("Nutzer")
        self.assertTrue(kontakt_liste is not None)
        self.assertEqual(1, len(kontakt_liste))
        print("\n\n\n*************************************\n\n\n")
        
    def DeleteKontakt(self):
    
        kontakte_repository, kategorien_repository = self.reopen_session()
        
        kontakt = kontakte_repository.get(1)
        self.assertEqual(kontakt.id, kontakt.id)
        kontakte_repository.delete(kontakt)
        
        kontakte_repository, kategorien_repository = self.reopen_session()

        exception_thrown = False 
        try:
            kontakte_repository.get(kontakt.id)
        except IllegalIdException as e:
            exception_thrown = True 
            
        self.assertTrue(exception_thrown)
        
        kontakt_liste = kontakte_repository.find_by_kategorie("Vereinsmitglied")
        self.assertEqual(0, len(kontakt_liste))

    def CreateTwoKontakteAndOneKategorie(self):
        
        kontakte_repository, kategorien_repository = self.reopen_session()
        
        kontakt = kontakte_repository.create(nachname="Wiese", vornamen="Lisa Marie", mailadresse="lisa_marie.wiese@web.de", gender=GenderTypes.FEMALE)
        spendeninformation = kontakte_repository.createSpendeninformation(kontakt, spendenhoehe=50, spendenjahr=2001, spendenbescheinigung=True)
        kontakt2 = kontakte_repository.create(nachname="Wiese", vornamen= "Lukas", gender=GenderTypes.MALE)
        spendeninformation2 = kontakte_repository.createSpendeninformation(kontakt2, spendenhoehe=100, spendenjahr=2001)
        kategorie = kategorien_repository.create(kategorienname="Spender")
        kontakte_repository.addKategorie(kontakt, kategorie)
        kontakte_repository.addKategorie(kontakt2, kategorie)
        
        kontakte_repository, kategorien_repository = self.reopen_session()
        
        kontakt_liste = kontakte_repository.find_by_kategorie("Spender")

        self.assertTrue(kontakt_liste is not None)
        self.assertEqual(2, len(kontakt_liste))
        
    def FindBySpendeninformation(self):
        
        kontakte_repository, kategorien_repository = self.reopen_session()
        
        kontakt_liste = kontakte_repository.find_by_spendeninformation(2001)
        self.assertEqual(2, len(kontakt_liste))
        kontakt = kontakt_liste[0]
        spendeninformationen = kontakt.spendeninformationen
        self.assertEqual("Wiese", kontakt.nachname)
        self.assertEqual(2001, spendeninformationen[0].spendenjahr)     

    def setup_db(self): 
        
        self.db_file = "C:\\Temp\\databasetest.db"
        try:
            os.remove(self.db_file)
        except FileNotFoundError:
            pass

        self.dbservice = DatenbankService("sqlite:///%s" % self.db_file)

        self.engine = self.dbservice.setup()
        self.session = Session(self.engine)
        
        kontakte_repository = KontakteRepository(self.session)
        kategorien_repository = KategorieRepository(self.session)
        
        return kontakte_repository, kategorien_repository

    def tear_down_db(self):
        
        self.session.commit()
        self.session.close()
        self.engine.dispose()
      
        try:
            os.remove(self.db_file)
        except FileNotFoundError:
            pass
        
    def reopen_session(self):

        self.session.commit()

        self.session.close()
        
        
        self.engine.dispose()
        
        self.engine = self.dbservice.create_engine()
        
        self.session = Session(self.engine)
        
        kontakte_repository = KontakteRepository(self.session)
        kategorien_repository = KategorieRepository(self.session)

        return kontakte_repository, kategorien_repository
            
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testIntegration']
    unittest.main()