'''
Created on 14.08.2023

@author: Jojo
'''
import unittest
from JoJo.KontaktVerwaltung.Services import DatenbankService, KontakteRepository, \
    IllegalIdException, KategorieRepository
from JoJo.KontaktVerwaltung.Domain import Kontakt, GenderTypes, Adresse, \
    TelefonNummernTyp
from sqlalchemy.orm.session import Session
import tempfile
import os


class Test(unittest.TestCase):

    def setUp(self):
        
        self.db_file = "C:\\Temp\\database.db"
        try:
            os.remove(self.db_file)
        except FileNotFoundError:
            pass
        self.dbservice = DatenbankService("sqlite:///%s" % self.db_file)
        #self.dbservice = DatenbankService("sqlite:///")
        self.engine = self.dbservice.setup()
        self.session = Session(self.engine)
        self.kontakte_repository = KontakteRepository(self.session)
        self.kategorien_repository = KategorieRepository(self.session)

    def tearDown(self):
        
        self.session.commit()
        self.session.close()
        self.engine.dispose()
        #os.remove(self.db_file)

    def testCreate(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller")
        self.assertTrue(kontakt is not None)
        self.assertTrue(isinstance(kontakt, Kontakt))
        self.assertTrue(kontakt.id is not None)

    def testGet(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller")
        kontakt2 = self.kontakte_repository.get(kontakt.id)
        self.assertTrue(kontakt2 is not None)
        self.assertTrue(isinstance(kontakt2, Kontakt))
        self.assertTrue(kontakt2.id is not None)
        self.assertEqual(kontakt.id, kontakt2.id)
        self.assertEqual(kontakt.nachname, kontakt2.nachname)

    def testGetFailsOnNotExistingID(self):

        exception_thrown = False
        try: 
            kontakt = self.kontakte_repository.get(4711)
        except IllegalIdException as e:
            exception_thrown = True
            
        self.assertTrue(exception_thrown)

    def testGetFailsOnNone(self):

        exception_thrown = False
        try: 
            kontakt = self.kontakte_repository.get(None)
        except IllegalIdException as e:
            exception_thrown = True
            
        self.assertTrue(exception_thrown)

    def testDelete(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.DIVERS)
        self.assertTrue(kontakt is not None)
        self.kontakte_repository.delete(kontakt)
        exception_thrown = False
        try:
            self.kontakte_repository.get(kontakt.id)
        except IllegalIdException as e:
            exception_thrown = True
        
        self.assertTrue(exception_thrown)       

    def testDeleteWithSimpleJoin(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.DIVERS)
        adresse = self.kontakte_repository.createAdresse(kontakt)
        spendeninfo = self.kontakte_repository.createSpendeninformation(kontakt, spendenhoehe=300, spendenjahr=1956)
        bankdaten = self.kontakte_repository.createBankdaten(kontakt, iban = "DE0987654321", BIC="GENODEM1GLS", kreditinstitut="GLS Bank")
        telefonnummern = self.kontakte_repository.createTelefonnummer(kontakt, telefonnummer="0761/3435", telefon_nummern_typ=TelefonNummernTyp.FESTNETZ_PRIVAT, praeferiert=True, telefonnummer2="01578392774", telefon_nummern_typ2=TelefonNummernTyp.HANDY_PRIVAT)
        self.kontakte_repository.addKategorie(kontakt, self.kategorien_repository.create(kategorienname="Test"))
        self.assertTrue(kontakt is not None)
        self.kontakte_repository.delete(kontakt)
        self.session.commit()
        self.session.close()
        self.engine.dispose()
        
        self.engine = self.dbservice.create_engine()
        self.session = Session(self.engine)
        self.kontakte_repository = KontakteRepository(self.session)
        
        exception_thrown = False
        try:
            self.kontakte_repository.get(kontakt.id)
        except IllegalIdException as e:
            exception_thrown = True
        
        self.assertTrue(exception_thrown)       
        
    def testCreateAdresse(self):
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Müller")
        # kontakt2 = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker")
        adresse = self.kontakte_repository.createAdresse(kontakt, strasse="Eschholzstrasse", hausnummer=30, plz=79106, wohnort="Freiburg")
        # adresse3 = self.kontakte_repository.createAdresse(strasse="Breisacher Straße", kontakt_id=kontakt.id)
        
        self.assertEqual(adresse.kontakt_id, kontakt.id)
        
        self.session.flush()

        gelesener_kontakt = self.kontakte_repository.get(kontakt.id)
        
        self.assertEqual(1, len(gelesener_kontakt.adressen))
        self.assertEqual("Eschholzstrasse", gelesener_kontakt.adressen[0].strasse)
        # print(kontakt2, adresse3)

    def testCreateSpendeninformation(self):
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker")
        spendeninformation = self.kontakte_repository.createSpendeninformation(kontakt, spendenhoehe=2000, spendenjahr=2020)
        
        self.assertEqual(spendeninformation.kontakt_id, kontakt.id)
        
        self.session.flush()
        
        gelesener_kontakt = self.kontakte_repository.get(kontakt.id)
        
        self.assertEqual(1, len(gelesener_kontakt.spendeninformationen))
        self.assertEqual(2000, gelesener_kontakt.spendeninformationen[0].spendenhoehe)
        
    def testCreateBankdaten(self):
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker")
        bankdaten = self.kontakte_repository.createBankdaten(kontakt, iban="DE1234567890", kreditinstitut="GLS Bank") 
    
        self.assertEqual(bankdaten.kontakt_id, kontakt.id)
        
        self.session.flush()
        
        gelesener_kontakt = self.kontakte_repository.get(kontakt.id)
        
        self.assertEqual(1, len(gelesener_kontakt.bankdaten))
        self.assertEqual("DE1234567890", gelesener_kontakt.bankdaten[0].iban)
        
    def testCreateTelefonnummer(self):
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker")
        telefonnummer = self.kontakte_repository.createTelefonnummer(kontakt, telefonnummer="07613333", telefon_nummern_typ=TelefonNummernTyp.FESTNETZ_PRIVAT)
    
        self.assertEqual(telefonnummer.kontakt_id, kontakt.id)
        
        self.session.flush()
        
        gelesener_kontakt = self.kontakte_repository.get(kontakt.id)
        
        self.assertEqual(1, len(gelesener_kontakt.telefonnummern))
        self.assertEqual("07613333", gelesener_kontakt.telefonnummern[0].telefonnummer)
        
    def testAddKategorie(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker")
        kategorie = self.kategorien_repository.create(kategorienname="Testkategorie")
        self.kontakte_repository.addKategorie(kontakt, kategorie)
        
        self.session.flush()
        self.session.expire_all()
        
        gelesener_kontakt = self.kontakte_repository.get(kontakt.id)
        
        self.assertEqual(1, len(gelesener_kontakt.kategorien))
        self.assertEqual("Testkategorie", gelesener_kontakt.kategorien[0].kategorienname)
        
    def testFindByNachname(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker")
        
        self.session.commit()
        self.session.close()
        self.engine.dispose()
        
        self.engine = self.dbservice.create_engine()
        self.session = Session(self.engine)
        self.kontakte_repository = KontakteRepository(self.session)
        
        gelesener_kontakt = self.kontakte_repository.find_by_nachname("Bäcker")
        self.assertEqual(1, len(gelesener_kontakt))
        print(gelesener_kontakt)
        self.assertEqual("Bäcker", gelesener_kontakt[0].nachname)
    
    def testFindByKategorie(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker")
        kategorie = self.kategorien_repository.create(kategorienname="Testkategorie")
        self.kontakte_repository.addKategorie(kontakt,kategorie)
        
        self.session.flush()
        self.session.expire_all()
        
        gelesener_kontakt = self.kontakte_repository.find_by_kategorie("Testkategorie")
        kategorien = kontakt.kategorien
        self.assertEqual(1, len(gelesener_kontakt))
        print(gelesener_kontakt)
        self.assertEqual("Bäcker", gelesener_kontakt[0].nachname)
        self.assertEqual("Testkategorie", kategorien[0].kategorienname)
        
    def testFindBySpendeninformation(self):
        
        kontakt = self.kontakte_repository.create(gender=GenderTypes.UNKNOWN, nachname="Bäcker") 
        spendeninformation = self.kontakte_repository.createSpendeninformation(kontakt, spendenhoehe=300, spendenjahr=2020, spendenbescheinigung=False)
        
        self.session.flush()
        self.session.expire_all()
        
        gelesener_kontakt = self.kontakte_repository.find_by_spendeninformation(2020)
        spendeninformationen = kontakt.spendeninformationen
        self.assertEqual(1, len(gelesener_kontakt))
        print(gelesener_kontakt)
        self.assertEqual("Bäcker", gelesener_kontakt[0].nachname)
        self.assertEqual(2020, spendeninformationen[0].spendenjahr)
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
